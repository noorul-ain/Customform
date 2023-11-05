from django.urls import path 
from . import views 

urlpatterns = [
    path('', views.Sign_up, name='Sign_up'),
    path('lg/', views.Login, name='login'),
    path('next/', views.Next, name='next'),
]
