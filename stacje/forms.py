from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

class ArtykulFormularz(forms.ModelForm):
	class Meta:
		model = Artykul
		fields=("tytul", "tresc")

class OtwieranieKonta(UserCreationForm):
	class Meta:
		model = Uzytkownik
		fields = ("nazwa", "username", "email")
		
class ZmianaDanychKonta(UserChangeForm):
	class Meta:
		model = Uzytkownik
		fields = ("username", "email", "nazwa")

class Logowanie():
	class Meta:
		model = Uzytkownik
		fields = ("username",)

class Stacja(forms.ModelForm):
	class Meta:
		model = StacjaRadiowa
		fields=("nazwa", "czestotliwosc", "dataZalozenia", "dataZakonczenia", "link", "zatrudnieni", "spolkaMediowa", "siecRadiowa", "kategoria", "miasto")

class Siec(forms.ModelForm):
	class Meta:
		model = SiecRadiowa
		fields=("nazwa", "dataZalozenia", "dataZakonczenia", "prezes", "spolkaMediowa")
		exclude=("adres",)

class Spolka(forms.ModelForm):
	class Meta:
		model = SpolkaMediowa
		fields=("nazwa", "dataZalozenia", "dataZakonczenia", "prezes")
		exclude=("adres",)

class Adres(forms.ModelForm):
	class Meta:
		model = Adres
		fields = ("ulica", "numerBudynku", "numerLokalu", "kodPocztowy", "miasto")

class Program(forms.ModelForm):
	class Meta:
		model = Program
		fields = ("tytul", "opis", "godzinaRozpoczecia", "godzinaZakonczenia", "prowadzacy")

class Prezes(forms.ModelForm):
	class Meta:
		model = Prezes
		fields = ("imie", "nazwisko")

class Miasto(forms.ModelForm):
	class Meta:
		model = Miasto
		fields = ("nazwa", "wojewodztwo")