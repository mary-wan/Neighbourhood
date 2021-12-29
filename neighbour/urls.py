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
    path('newpost/<id>/', views.new_post, name='newpost'),
    path('update_business/<id>/<bus_id>/business/', views.update_business, name='update_business'),
    path('delete_business/<id>/<bus_id>/', views.delete_business, name='delete_business'),
    path('update_post/<id>/<post_id>/post/', views.update_post, name='update_post'),
    path('delete_post/<id>/<post_id>/', views.delete_post, name='delete_post'),
    path('update_hood/<id>/', views.update_hood, name='update_hood'),
    path('search/', views.search_hood, name='search'),
    path('user_profile/<username>/', views.user_profile, name='user_profile'),
]