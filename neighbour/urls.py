from django.urls.conf import path
from . import views

urlpatterns=[
    path('',views.index,name='home'),
    path('hoods/',views.hoods,name='hoods'),
    path('newhood/', views.new_hood, name='newhood'),
    path('profile/<username>/', views.profile, name='profile'),
    path('my_hood/<id>', views.user_hood, name='my_hood'),
    path('leave-hood/<id>', views.leave_hood, name='leave_hood'),
    path('newbusiness/<id>/', views.new_business, name='newbusiness'),
]