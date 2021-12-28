from django.shortcuts import redirect, render
from . forms import UserRegisterForm
from .models import NeighbourHood


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

def hoods(request):
    hoods = NeighbourHood.objects.all()
    return render(request,"all-neighbour/hoods.html",{'hoods':hoods})