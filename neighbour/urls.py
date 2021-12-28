from django.urls.conf import path
from . import views

urlpatterns=[
    path('',views.index,name='home'),
    path('hoods/',views.hoods,name='hoods')
]