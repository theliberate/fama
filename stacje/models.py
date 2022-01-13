from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from django.utils.text import slugify
from django.views.generic import edit

class Prezenter(models.Model):
	class Meta:
		verbose_name_plural = "Prezenterzy"
	imie = models.CharField(max_length=50, verbose_name="Imię")
	nazwisko = models.CharField(max_length=50)
	pseudonim = models.CharField(max_length=50, blank=True, null=True)
	opis = models.TextField(blank=True, null=True)
	def __str__(self):
		return self.imie+" "+self.nazwisko
		
class StacjaRadiowa(models.Model):
	class Meta:
		verbose_name = "Stacja radiowa"
		verbose_name_plural = "Stacje radiowe"
	nazwa = models.CharField(max_length=50)
	czestotliwosc = models.CharField(max_length=10, verbose_name="Częstotliwość")
	dataZalozenia = models.DateField(verbose_name="Data założenia")
	dataZakonczenia = models.DateField(blank=True, null=True, verbose_name="Data zakończenia działalności")
	okresDzialalnosci = models.DurationField(blank=True, null=True, verbose_name="Okres działalności")
	link = models.URLField(max_length=150, blank=True, null=True)
	zatrudnieni = models.ManyToManyField("Prezenter", blank=True, null=True, through="ZatrudnieniPrezenterzy")
	spolkaMediowa = models.ForeignKey("SpolkaMediowa", blank=True, null=True, on_delete=models.PROTECT, verbose_name="Spółka mediowa")
	siecRadiowa = models.ForeignKey("SiecRadiowa", blank=True, null=True, on_delete=models.PROTECT, verbose_name="Sieć radiowa")
	kategoria = models.ManyToManyField("Kategoria", blank=True, null=True, through="KategorieStacji")
	miasto = models.ManyToManyField("Miasto", blank=True, null=True, through="StacjeWMiescie")
	url = models.SlugField(max_length=500, blank=True, editable=False)
	def save(self, *args, **kwargs):
		self.url = slugify(self.nazwa)
		super(StacjaRadiowa, self).save(*args, **kwargs)
	def __str__(self):
		return self.nazwa
		
class ZatrudnieniPrezenterzy(models.Model):
	stacja = models.ForeignKey("StacjaRadiowa", on_delete=models.PROTECT)
	zatrudnionyPrezenter = models.ForeignKey("Prezenter", on_delete=models.PROTECT)
	
class KategorieStacji(models.Model):
	stacja = models.ForeignKey("StacjaRadiowa", blank=True, null=True, on_delete=models.SET_NULL)
	kategoria = models.ForeignKey("Kategoria", blank=True, null=True, on_delete=models.SET_NULL)
	
class StacjeWMiescie(models.Model):
	stacja = models.ForeignKey("StacjaRadiowa", blank=True, null=True, on_delete=models.SET_NULL)
	miasto = models.ForeignKey("Miasto", blank=True, null=True, on_delete=models.SET_NULL)
	
class SpolkaMediowa(models.Model):
	class Meta:
		verbose_name = "Spółka mediowa"
		verbose_name_plural = "Spółki mediowe"
	nazwa = models.CharField(max_length=50, unique=True)
	dataZalozenia = models.DateField(verbose_name="Data założenia")
	dataZakonczenia = models.DateField(blank=True, null=True, verbose_name="Data zakończenia działalności")
	okresDzialalnosci = models.DurationField(blank=True, null=True, verbose_name="Okres działalności")
	prezes = models.ForeignKey("Prezes", blank=True, on_delete=models.RESTRICT)
	adresSiedziby = models.OneToOneField("Adres", blank=True, null=True, on_delete=models.CASCADE, verbose_name="Adres siedziby")
	url = models.SlugField(max_length=500, blank=True, editable=False)
	def save(self, *args, **kwargs):
		self.url = slugify(self.nazwa)
		super(SpolkaMediowa, self).save(*args, **kwargs)
	def __str__(self):
		return self.nazwa
	
class SiecRadiowa(models.Model):
	class Meta:
		verbose_name = "Sieć radiowa"
		verbose_name_plural = "Sieci radiowe"
	nazwa = models.CharField(max_length=50, unique=True)
	dataZalozenia = models.DateField(verbose_name="Data założenia")
	dataZakonczenia = models.DateField(blank=True, null=True, verbose_name="Data zakończenia działalności")
	okresDzialalnosci = models.DurationField(blank=True, null=True, verbose_name="Okres działalności")
	prezes = models.ForeignKey("Prezes", blank=True, null=True, on_delete=models.RESTRICT)
	adresSiedziby = models.OneToOneField("Adres", blank=True, null=True, on_delete = models.CASCADE, verbose_name="Adres siedziby")
	spolkaMediowa = models.OneToOneField("SpolkaMediowa", blank=True, null=True, on_delete = models.CASCADE, verbose_name="Spółka mediowa")
	url = models.SlugField(max_length=500, blank=True, editable=False)
	def save(self, *args, **kwargs):
		self.url = slugify(self.nazwa)
		super(SiecRadiowa, self).save(*args, **kwargs)
	def __str__(self):
		return self.nazwa
	
class Miasto(models.Model):
	class Meta:
		verbose_name_plural = "Miasta"
	WOJEWODZTWA = (
		('WM', 'WARMIŃSKO-MAZURSKIE'),
		('PL', 'PODLASKIE'),
		('OS', 'OPOLSKIE'),
		('PR', 'POMORSKIE'),
		('ZP', 'ZACHODNIO-POMORSKIE'),
		('WP', 'WIELKOPOLSKIE'),
		('SK', 'ŚWIĘTOKRZYSKIE'),
		('SL', 'ŚLĄSKIE'),
		('DS', 'DOLNOŚLĄSKIE'),
		('KP', 'KUJAWSKO-POMORSKIE'),
		('LO', 'ŁÓDZKIE'),
		('LBE', 'LUBELSKIE'),
		('LBU', 'LUBUSKIE'),
		('MZ', 'MAZOWIECKIE'),
		('MP', 'MAŁOPOLSKIE'),
		('PK', 'PODKARPACKIE'),
		('OP', 'OGÓLNOPOLSKIE'),
	)	
	nazwa = models.CharField(max_length=50)
	wojewodztwo = models.CharField(max_length=30, choices=WOJEWODZTWA, verbose_name="Województwo")
	def __str__(self):
		return self.nazwa
	
class Prezes(models.Model):
	class Meta:
		verbose_name_plural = "Prezesowie"
	imie = models.CharField(max_length=50, verbose_name="Imię")
	nazwisko = models.CharField(max_length=50)
	def __str__(self):
		return self.imie+" "+self.nazwisko
	
class SlowoKluczowe(models.Model):
	class Meta:
		verbose_name = "Słowo kluczowe"
		verbose_name_plural = "Słowa kluczowe"
	nazwa = models.CharField(max_length=20, primary_key=True, unique=True)
	def __str__(self):
		return self.nazwa

class Artykul(models.Model):
	class Meta:
		verbose_name = "Artykuł"
		verbose_name_plural = "Artykuły"
	dataWstawienia = models.DateField(default = timezone.now, verbose_name="Data wstawienia")
	wyroznienie = models.BooleanField(default=False, verbose_name="Wyróżnienie")
	tytul = models.CharField(max_length=100, verbose_name="Tytuł")
	autor = models.ForeignKey("Uzytkownik", on_delete=models.CASCADE, default=None)
	tresc = models.TextField(verbose_name="Treść")
	url = models.SlugField(max_length=500, blank=True, editable=False)
	def save(self, *args, **kwargs):
		self.url = slugify(self.tytul)
		super(Artykul, self).save(*args, **kwargs)
	def __str__(self):
		return self.tytul
	
class Uzytkownik(AbstractUser):
	class Meta:
		verbose_name = "Użytkownik"
		verbose_name_plural = "Użytkownicy"
	username = models.CharField(max_length=30, verbose_name="Nazwa użytkownika", unique=True)
	email = models.EmailField(verbose_name="Adres e-mail")
	nazwa = models.CharField(max_length=30, editable=True, verbose_name="Imię")
	dataUtworzeniaKonta = models.DateField(default=timezone.now, verbose_name="Data utworzenia konta")
	ulubioneStacje = models.ManyToManyField("StacjaRadiowa", blank=True, null=True, through="UlubioneStacje", verbose_name="Ulubione stacje")
	ulubioneSieci = models.ManyToManyField("SiecRadiowa", blank=True, null=True, through="UlubioneSieci", verbose_name="Ulubione sieci")
	url = models.SlugField(max_length=100, blank=True, editable=True)
	bio = models.TextField(blank=True)
	def save(self, *args, **kwargs):
		self.url = slugify(self.username)
		super(Uzytkownik, self).save(*args, **kwargs)
	def __str__(self):
		return self.username

class UlubioneStacje(models.Model):
	uzytkownik = models.ForeignKey("Uzytkownik", blank=True, null=True, on_delete=models.CASCADE)
	stacja = models.ForeignKey("StacjaRadiowa", blank=True, null=True, on_delete=models.CASCADE)
		
class UlubioneSieci(models.Model):
	uzytkownik = models.ForeignKey("Uzytkownik", blank=True, null=True, on_delete=models.CASCADE)
	siec = models.ForeignKey("SiecRadiowa", blank=True, null=True, on_delete=models.CASCADE)
		
class Program(models.Model):
	class Meta:
		verbose_name_plural = "Programy"
	tytul = models.CharField(max_length=30, verbose_name="Tytuł")
	opis = models.TextField()
	godzinaRozpoczecia = models.TimeField(verbose_name="Godzina rozpoczęcia")
	godzinaZakonczenia = models.TimeField(verbose_name="Godzina zakończenia")
	prowadzacy = models.ManyToManyField("Prezenter", through="ProwadzacyProgramu", verbose_name="Prowadzący")
	nadawaneProgramy = models.ForeignKey("StacjaRadiowa", on_delete=models.CASCADE, verbose_name="Nadawane programy")
	def __str__(self):
		return self.tytul
		
class ProwadzacyProgramu(models.Model):
	prowadzacy = models.ForeignKey("Prezenter", on_delete=models.CASCADE)
	program = models.ForeignKey("Program", on_delete=models.CASCADE)
	
class Adres(models.Model):
	class Meta:
		verbose_name_plural = "Adresy"
	ulica = models.CharField(max_length=30)
	numerBudynku = models.CharField(max_length=10, verbose_name="Numer budynku")
	numerLokalu = models.IntegerField(blank=True, null=True, verbose_name="Numer lokalu")
	kodPocztowy = models.CharField(max_length=7, verbose_name="Kod pocztowy")
	miasto = models.CharField(max_length=50)
	def __str__(self):
		return self.ulica+" "+self.numerBudynku+" "+self.miasto
	
class Kategoria(models.Model):
	class Meta:
		verbose_name_plural = "Kategorie"
	nazwa = models.CharField(max_length=30, unique=True, primary_key=True)
	def __str__(self):
			return self.nazwa