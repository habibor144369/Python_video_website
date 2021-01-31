from django.urls import path
from . import views

urlpatterns = [
    path('', views.Index, name="index"),
    path('registration/', views.getRegistration, name="registration"),
    path('login/', views.getLogin, name="login"),
    path('logout/', views.getlogout, name="logout"),
    path('video/', views.VideoTutorial, name="video"),
    
]
