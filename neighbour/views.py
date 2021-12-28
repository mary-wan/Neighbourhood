from django.shortcuts import redirect, render
from django.http  import HttpResponseRedirect,Http404
from . forms import UserRegisterForm,HoodForm
from .models import NeighbourHood
from django.contrib.auth.decorators import login_required
from django.urls import reverse


def index(request):
    return render(request,'all-neighbour/home.html')

def register(request):
    if request.user.is_authenticated:
    #redirect user to the profile page
        return redirect('home')
    if request.method=="POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            return redirect('login')
            
    else:
        form = UserRegisterForm()
    return render(request,"registration/register.html",{'form':form})

@login_required(login_url='login')
def hoods(request):
    hoods = NeighbourHood.objects.all()
    return render(request,"all-neighbour/hoods.html",{'hoods':hoods})

@login_required(login_url='login')
def new_hood(request):
    if request.method == 'POST':
        form = HoodForm(request.POST, request.FILES)
        if form.is_valid():
            hood = form.save(commit=False)
            # hood.admin = request.user.profile
            hood.save()
            return HttpResponseRedirect(reverse("hoods"))
    else:
        form = HoodForm()
    return render(request, 'all-neighbour/newhood.html', {'form': form})
    