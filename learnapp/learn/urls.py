from django.urls import path
from . import views

urlpatterns=[
    path('home',views.learn_home,name='home1')
    
]