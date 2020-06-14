from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path("",views.open,name="open"),
    path("register/",views.Register,name="register"),
     path("TEMPLOGIN/",views.TEMPLOGIN,name="reg"),
      path("start/",views.Start,name="start"),
path("login/",views.login,name="login"),

    ]