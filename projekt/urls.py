from stacje import views
from django.urls import include, path
from django import forms
from django.contrib.auth import views as view

"""projekt URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin

urlpatterns = [
	path('admin/', admin.site.urls),
	path("", views.StartPage, name="startpage"),
    path("login/", view.LoginView.as_view(), name="login"),
    path("logout/", views.Wyloguj, name="logout"),
    path("register/", views.SignUpView.as_view(), name="rejestracja"),
    path("mainpage/", views.MainPage, name="mainpage"),
    path("historia/", views.Historia, name="historia"),
	path("artykuly/", views.ListaArtykulow.as_view(), name = "artykuly"),
	path("artykuly/dodaj/", views.dodajArtykul, name = "pisanieArtykulu"),
    path("artykuly/<int:pk>/edytuj/", views.WidokEdycjiArtykulu.as_view(template_name="projekt/edycjaArtykulu.html"), name = "edycjaArtykulu"),
    path("artykuly/<int:pk>/usun/", views.WidokUsunieciaArtykulu.as_view(template_name="projekt/usuwanieArtykulu.html"), name = "usuwanieArtykulu"),
	path("artykuly/<int:pk>/<slug:url>/", views.SzczegolyArtykulu.as_view(), name = "artykulSzczegoly"),
    path("users/", views.ListaUzytkownikow.as_view(), name = "uzytkownicy"),
	path("user/<int:pk>/<slug:url>/", views.ProfilUzytkownika.as_view(), name = "profilUzytkownika"),
    path("user/<int:pk>/<slug:url>/edytuj/", views.WidokEdycjiUzytkownika.as_view(template_name='projekt/edit.html'), name = "edycjaUzytkownika"),
    path("user/<int:pk>/<slug:url>/usun/", views.WidokUsunieciaUzytkownika.as_view(template_name='projekt/delete.html'), name = "usuniecieUzytkownika"),
    path("sieci/<int:pk>/<slug:url>/", views.ProfilSieci.as_view(), name = "profilSieci"),
    path("stacje/<int:pk>/<slug:url>/", views.ProfilStacji.as_view(), name = "profilStacji"),
    path("stacje/", views.ListaStacji.as_view(), name = "stacje"),
    path("sieci/", views.ListaSieci.as_view(), name = "sieci"),
    path("spolki/", views.ListaSpolek.as_view(), name = "spolki"),
    path("spolki/<int:pk>/<slug:url>/", views.SzczegolySpolki.as_view(), name = "szczegolySpolki"),
    path("stacje/dodaj/", views.dodajStacje, name = "dodajStacje"),
    path("sieci/dodaj/", views.dodajSiec, name = "dodajSiec"),
    path("spolki/dodaj/", views.dodajSpolke, name = "dodajSpolke"),
    path("spolki/<int:pk>/<slug:url>/edytuj/", views.EdycjaSpolki.as_view(template_name="projekt/edycja.html"), name = "edycjaSpolki"),
    path("spolki/<int:pk>/<slug:url>/usun/", views.UsuwanieSpolki.as_view(template_name="projekt/usuwanieSpolki.html"), name = "usuwanieSpolki"),
    path("stacje/<int:pk>/<slug:url>/edytuj/", views.EdycjaStacji.as_view(template_name="projekt/edycjaStacji.html"), name = "edycjaStacji"),
    path("stacje/<int:pk>/<slug:url>/usun/", views.UsuwanieStacji.as_view(template_name="projekt/usuwanieStacji.html"), name = "usuwanieStacji"),
    path("sieci/<int:pk>/<slug:url>/edytuj/", views.EdycjaSieci.as_view(template_name="projekt/edycja.html"), name = "edycjaSieci"),
    path("sieci/<int:pk>/<slug:url>/usun/", views.UsuwanieSieci.as_view(template_name="projekt/usuwanieSieci.html"), name = "usuwanieSieci"),
]
