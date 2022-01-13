from django.http.response import Http404
from django.shortcuts import render
from django.contrib import auth
from django.http import HttpResponseRedirect
from django.urls.base import reverse_lazy
from django.views import generic, View
from django.urls import reverse
from django.contrib.auth.forms import AuthenticationForm
from django import forms
from django.utils.text import slugify
from django.views.generic.edit import DeleteView, UpdateView
from django.contrib.auth import logout

from .models import *
from .forms import *

def MainPage(request):
	return render(request, "projekt/mainpage.html")
	
class ProfilUzytkownika(generic.DetailView):
	model = Uzytkownik
	context_object_name = "User"
	template_name = "projekt/profil.html"
	
class ProfilPrezentera(generic.DetailView):
	model = Prezenter
	template_name = "projekt/prezenter.html"
	
class ProfilStacji(generic.DetailView):
	model = StacjaRadiowa
	context_object_name = "Stacja"
	template_name = "projekt/stacja.html"
	
class ProfilSpolki(generic.DetailView):
	model = SpolkaMediowa
	context_object_name = "Spolka"
	template_name = "projekt/spolka.html"
	
class ProfilSieci(generic.DetailView):
	model = SiecRadiowa
	context_object_name = "Siec"
	template_name = "projekt/siec.html"
	
class OpisProgramu(generic.DetailView):
	model = Program
	template_name = "projekt/program.html"

def dodajArtykul(request):
	form = ArtykulFormularz(request.POST or None)
	form.instance.autor = request.user
	form.instance.url = slugify(form.instance.tytul)
	
	if(request.method == "POST"):
		if(form.is_valid()):
			form.save()
		return HttpResponseRedirect("/artykuly/")
	context = {"form": form,}
	return render(request, "projekt/dodawanieArtykulu.html", context)

def dodajStacje(request):
	form = Stacja(request.POST or None)
	if form.instance.dataZalozenia is not None and form.instance.dataZakonczenia is not None:
		form.instance.okresDzialanosci = form.instance.dataZakonczenia - form.instance.dataZalozenia
	form.instance.url = slugify(form.instance.nazwa)
	
	if(request.method == "POST"):
		if(form.is_valid()):
			form.save()
		return HttpResponseRedirect("/stacje/")
	context = {"form": form,}
	return render(request, "projekt/dodawanieStacji.html", context)

def dodajSiec(request):
	form = Siec(request.POST or None, prefix="siec")
	adres = Adres(request.POST or None, prefix="adres")
	if form.instance.dataZalozenia is not None and form.instance.dataZakonczenia is not None:
		form.instance.okresDzialanosci = form.instance.dataZakonczenia - form.instance.dataZalozenia
	form.instance.url = slugify(form.instance.nazwa)
	
	if(request.method == "POST"):
		if(form.is_valid() and adres.is_valid()):
			form.save(commit=False).adresSiedziby = adres.save()
			form.save()
		return HttpResponseRedirect("/sieci/")
	context = {"form": form, "adres": adres}
	return render(request, "projekt/dodawanie.html", context)

def dodajSpolke(request):
	form = Spolka(request.POST or None, prefix="spolka")
	adres = Adres(request.POST or None, prefix="adres")
	if form.instance.dataZalozenia is not None and form.instance.dataZakonczenia is not None:
		form.instance.okresDzialanosci = form.instance.dataZakonczenia - form.instance.dataZalozenia
	form.instance.url = slugify(form.instance.nazwa)
	
	if(request.method == "POST"):
		if(form.is_valid() and adres.is_valid()):
			form.cleaned_data["adresSiedziby"] = adres.save()
			form.save()
		return HttpResponseRedirect("/spolki/")
	context = {"form": form, "adres": adres}
	return render(request, "projekt/dodawanie.html", context)
	
class SzczegolyArtykulu(generic.DetailView):
	model = Artykul
	context_object_name = "Artykul"
	template_name = "projekt/artykul.html"

class SzczegolySpolki(generic.DetailView):
	model = SpolkaMediowa
	context_object_name = "Spolka"
	template_name = "projekt/spolka.html"

def StartPage(request):
	if not request.user.is_authenticated:
		return render(request, "projekt/start.html")
	else:
		return render(request, "projekt/mainpage.html")

class ListaArtykulow(generic.ListView):
	model = Artykul
	context_object_name = "artykuly"
	template_name = "projekt/artykuly.html"

	def get_queryset(self):
		return Artykul.objects.order_by("dataWstawienia")
	
class ListaStacji(generic.ListView):
	model = StacjaRadiowa
	context_object_name = "Stacja"
	template_name = "projekt/stacje.html"
	def get_queryset(self):
		return StacjaRadiowa.objects.order_by("nazwa")
	
class ListaSieci(generic.ListView):
	model = SiecRadiowa
	context_object_name = "Siec"
	template_name = "projekt/sieci.html"
	def get_queryset(self):
		return SiecRadiowa.objects.order_by("nazwa")

class ListaSpolek(generic.ListView):
	model = SpolkaMediowa
	context_object_name = "Spolka"
	template_name = "projekt/spolki.html"

	def get_queryset(self):
		return SpolkaMediowa.objects.order_by("nazwa")

class ListaUzytkownikow(generic.ListView):
	model = Uzytkownik
	context_object_name = "User"
	template_name = "projekt/uzytkownicy.html"
	def get_queryset(self):
		return Uzytkownik.objects.order_by("username")

class ListaUzytkownikow(generic.ListView):
	model = SpolkaMediowa
	context_object_name = "SpolkaMediowa"
	template_name = "projekt/spolki.html"
	def get_queryset(self):
		return Uzytkownik.objects.order_by("nazwa")

class SignUpView(generic.CreateView):
	form_class = OtwieranieKonta
	template_name = 'projekt/rejestracja.html'
	def get_success_url(self):
		return "../login"

def Historia(request):
	return render(request, "projekt/historia.html")

class WidokEdycjiUzytkownika(UpdateView):
	model = Uzytkownik
	form_class = ZmianaDanychKonta
	def get_success_url(self):
		return "../../"

class WidokUsunieciaArtykulu(DeleteView):
	model = Artykul
	def get_success_url(self):
		return "../../"

class WidokEdycjiArtykulu(UpdateView):
	model = Artykul
	form_class = ArtykulFormularz
	def get_success_url(self):
		return "../../"

class WidokUsunieciaUzytkownika(DeleteView):
	model = Uzytkownik
	def get_success_url(self):
		return "../../../.."

class EdycjaSieci(UpdateView):
	model = SiecRadiowa
	form_class = Siec
	def get_success_url(self):
		return "../../"

class UsuwanieSieci(DeleteView):
	model = SiecRadiowa
	def get_success_url(self):
		return "../../"

class EdycjaSpolki(UpdateView):
	model = SpolkaMediowa
	form_class = Spolka
	def get_success_url(self):
		return "../../../"

class UsuwanieSpolki(DeleteView):
	model = SpolkaMediowa
	def get_success_url(self):
		return "../../../../"

class EdycjaStacji(UpdateView):
	model = StacjaRadiowa
	form_class = Stacja
	def get_success_url(self):
		return "../../../"

class UsuwanieStacji(DeleteView):
	model = StacjaRadiowa
	def get_success_url(self):
		return "../../../../"

def Wyloguj(request):
	logout(request)
	return HttpResponseRedirect("/")

def BrakDostepu(request):
	return render(request, "projekt/brakdostepu.html")