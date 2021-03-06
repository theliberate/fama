# Generated by Django 3.2 on 2021-05-31 21:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stacje', '0010_alter_spolkamediowa_adressiedziby'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='adres',
            options={'verbose_name_plural': 'Adresy'},
        ),
        migrations.AddField(
            model_name='siecradiowa',
            name='spolkaMediowa',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='stacje.spolkamediowa', verbose_name='Spółka mediowa'),
        ),
        migrations.AlterField(
            model_name='miasto',
            name='wojewodztwo',
            field=models.CharField(choices=[('WM', 'WARMIŃSKO-MAZURSKIE'), ('PL', 'PODLASKIE'), ('OS', 'OPOLSKIE'), ('PR', 'POMORSKIE'), ('ZP', 'ZACHODNIO-POMORSKIE'), ('WP', 'WIELKOPOLSKIE'), ('SK', 'ŚWIĘTOKRZYSKIE'), ('SL', 'ŚLĄSKIE'), ('DS', 'DOLNOŚLĄSKIE'), ('KP', 'KUJAWSKO-POMORSKIE'), ('LO', 'ŁÓDZKIE'), ('LBE', 'LUBELSKIE'), ('LBU', 'LUBUSKIE'), ('MZ', 'MAZOWIECKIE'), ('MP', 'MAŁOPOLSKIE'), ('PK', 'PODKARPACKIE'), ('OP', 'OGÓLNOPOLSKIE')], max_length=30, verbose_name='Województwo'),
        ),
        migrations.AlterField(
            model_name='prezenter',
            name='opis',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='prezenter',
            name='pseudonim',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='siecradiowa',
            name='adresSiedziby',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='stacje.adres', verbose_name='Adres siedziby'),
        ),
        migrations.AlterField(
            model_name='spolkamediowa',
            name='dataZakonczenia',
            field=models.DateField(blank=True, null=True, verbose_name='Data zakończenia działalności'),
        ),
        migrations.AlterField(
            model_name='spolkamediowa',
            name='okresDzialalnosci',
            field=models.DurationField(blank=True, null=True, verbose_name='Okres działalności'),
        ),
        migrations.AlterField(
            model_name='stacjaradiowa',
            name='okresDzialalnosci',
            field=models.DurationField(blank=True, null=True, verbose_name='Okres działalności'),
        ),
        migrations.AlterField(
            model_name='stacjaradiowa',
            name='spolkaMediowa',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='stacje.spolkamediowa', verbose_name='Spółka mediowa'),
        ),
        migrations.AlterField(
            model_name='stacjaradiowa',
            name='zatrudnieni',
            field=models.ManyToManyField(blank=True, null=True, through='stacje.ZatrudnieniPrezenterzy', to='stacje.Prezenter'),
        ),
        migrations.AlterField(
            model_name='uzytkownik',
            name='ulubioneSieci',
            field=models.ManyToManyField(blank=True, null=True, through='stacje.UlubioneSieci', to='stacje.SiecRadiowa', verbose_name='Ulubione sieci'),
        ),
        migrations.AlterField(
            model_name='uzytkownik',
            name='ulubioneStacje',
            field=models.ManyToManyField(blank=True, null=True, through='stacje.UlubioneStacje', to='stacje.StacjaRadiowa', verbose_name='Ulubione stacje'),
        ),
    ]
