from django.urls import path
from django.contrib.auth import views as view

from . import views

app_name = "stacje"
urlpatterns = [
	path("", views.StartPage, name="startpage"),
    path("login/", view.LoginView.as_view(), name="login"),
    path("register/", views.SignUpView.as_view(), name="rejestracja"),
    path("mainpage/", views.MainPage, name="mainpage"),
]