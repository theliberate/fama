# Generated by Django 3.2 on 2021-05-26 10:14

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Uzytkownik',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('nazwa', models.CharField(max_length=30)),
                ('dataUtworzeniaKonta', models.DateField(default=django.utils.timezone.now)),
                ('url', models.SlugField(blank=True, max_length=100, unique=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Adres',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ulica', models.CharField(max_length=30)),
                ('numerBudynku', models.CharField(max_length=10)),
                ('numerLokalu', models.IntegerField(blank=True)),
                ('kodPocztowy', models.CharField(max_length=7)),
                ('miasto', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Kategoria',
            fields=[
                ('nazwa', models.CharField(max_length=30, primary_key=True, serialize=False, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='KategorieStacji',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kategoria', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='stacje.kategoria')),
            ],
        ),
        migrations.CreateModel(
            name='Miasto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nazwa', models.CharField(max_length=50)),
                ('wojewodztwo', models.CharField(choices=[('WM', 'WARMIŃSKO-MAZURSKIE'), ('PL', 'PODLASKIE'), ('OS', 'OPOLSKIE'), ('PR', 'POMORSKIE'), ('ZP', 'ZACHODNIO-POMORSKIE'), ('WP', 'WIELKOPOLSKIE'), ('SK', 'ŚWIĘTOKRZYSKIE'), ('SL', 'ŚLĄSKIE'), ('DS', 'DOLNOŚLĄSKIE'), ('KP', 'KUJAWSKO-POMORSKIE'), ('LO', 'ŁÓDZKIE'), ('LBE', 'LUBELSKIE'), ('LBU', 'LUBUSKIE'), ('MZ', 'MAZOWIECKIE'), ('MP', 'MAŁOPOLSKIE'), ('PK', 'PODKARPACKIE')], max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Prezenter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imie', models.CharField(max_length=50)),
                ('nazwisko', models.CharField(max_length=50)),
                ('pseudonim', models.CharField(blank=True, max_length=50)),
                ('opis', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Prezes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imie', models.CharField(max_length=50)),
                ('nazwisko', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Program',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tytul', models.CharField(max_length=30)),
                ('opis', models.TextField()),
                ('godzinaRozpoczecia', models.TimeField()),
                ('godzinaZakonczenia', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='SiecRadiowa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nazwa', models.CharField(max_length=50, unique=True)),
                ('dataZalozenia', models.DateField()),
                ('dataZakonczenia', models.DateField(blank=True)),
                ('okresDzialalnosci', models.DurationField(blank=True)),
                ('adresSiedziby', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='stacje.adres')),
                ('prezes', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.RESTRICT, to='stacje.prezes')),
            ],
        ),
        migrations.CreateModel(
            name='SlowoKluczowe',
            fields=[
                ('nazwa', models.CharField(max_length=20, primary_key=True, serialize=False, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='SpolkaMediowa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nazwa', models.CharField(max_length=50, unique=True)),
                ('dataZalozenia', models.DateField()),
                ('dataZakonczenia', models.DateField(blank=True)),
                ('okresDzialalnosci', models.DurationField(blank=True)),
                ('adresSiedziby', models.OneToOneField(blank=True, on_delete=django.db.models.deletion.CASCADE, to='stacje.adres')),
                ('prezes', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.RESTRICT, to='stacje.prezes')),
            ],
        ),
        migrations.CreateModel(
            name='StacjaRadiowa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nazwa', models.CharField(max_length=50)),
                ('czestotliwosc', models.CharField(max_length=10)),
                ('dataZalozenia', models.DateField()),
                ('dataZakonczenia', models.DateField(blank=True)),
                ('okresDzialalnosci', models.DurationField(blank=True)),
                ('link', models.URLField(blank=True, max_length=150)),
                ('kategoria', models.ManyToManyField(blank=True, null=True, through='stacje.KategorieStacji', to='stacje.Kategoria')),
            ],
        ),
        migrations.CreateModel(
            name='ZatrudnieniPrezenterzy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stacja', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='stacje.stacjaradiowa')),
                ('zatrudnionyPrezenter', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='stacje.prezenter')),
            ],
        ),
        migrations.CreateModel(
            name='UlubioneStacje',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stacja', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='stacje.stacjaradiowa')),
                ('uzytkownik', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UlubioneSieci',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('siec', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='stacje.siecradiowa')),
                ('uzytkownik', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='StacjeWMiescie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('miasto', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='stacje.miasto')),
                ('stacja', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='stacje.stacjaradiowa')),
            ],
        ),
        migrations.AddField(
            model_name='stacjaradiowa',
            name='miasto',
            field=models.ManyToManyField(blank=True, null=True, through='stacje.StacjeWMiescie', to='stacje.Miasto'),
        ),
        migrations.AddField(
            model_name='stacjaradiowa',
            name='spolkaMediowa',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, to='stacje.spolkamediowa'),
        ),
        migrations.AddField(
            model_name='stacjaradiowa',
            name='zatrudnieni',
            field=models.ManyToManyField(blank=True, null=True, through='stacje.ZatrudnieniPrezenterzy', to='stacje.Prezenter'),
        ),
        migrations.CreateModel(
            name='ProwadzacyProgramu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('program', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stacje.program')),
                ('prowadzacy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stacje.prezenter')),
            ],
        ),
        migrations.AddField(
            model_name='program',
            name='nadawaneProgramy',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stacje.stacjaradiowa'),
        ),
        migrations.AddField(
            model_name='program',
            name='prowadzacy',
            field=models.ManyToManyField(through='stacje.ProwadzacyProgramu', to='stacje.Prezenter'),
        ),
        migrations.AddField(
            model_name='kategoriestacji',
            name='stacja',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='stacje.stacjaradiowa'),
        ),
        migrations.CreateModel(
            name='Artykul',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dataWstawienia', models.DateField(default=django.utils.timezone.now)),
                ('wyroznienie', models.BooleanField(default=False)),
                ('tytul', models.CharField(max_length=100)),
                ('tresc', models.TextField()),
                ('url', models.SlugField(blank=True, editable=False, max_length=500, unique=True)),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='uzytkownik',
            name='ulubioneSieci',
            field=models.ManyToManyField(blank=True, null=True, through='stacje.UlubioneSieci', to='stacje.SiecRadiowa'),
        ),
        migrations.AddField(
            model_name='uzytkownik',
            name='ulubioneStacje',
            field=models.ManyToManyField(blank=True, null=True, through='stacje.UlubioneStacje', to='stacje.StacjaRadiowa'),
        ),
        migrations.AddField(
            model_name='uzytkownik',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions'),
        ),
    ]