from os import name
from django.urls import path
from . import views

urlpatterns = [
    path('home/list/', views.getlist),
    path('home/', views.gethome, name='home'),
    path('submit/', views.post, name='submit'),
    path('home/sell/', views.display),
]