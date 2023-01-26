from os import name
from django.urls import path
from . import views

urlpatterns = [
    path('home/list/', views.getlist),
    path('home/', views.gethome, name='home'),
    path('submit/', views.post, name='submit'),
    path('home/sell/', views.display),
    path('home/recommend', views.get_recommendation),
    path('home/recommend/result', views.get_crop_result, name='result'),
]