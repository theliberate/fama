# Generated by Django 3.2 on 2021-05-31 21:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stacje', '0011_auto_20210531_2321'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stacjaradiowa',
            name='dataZakonczenia',
            field=models.DateField(blank=True, null=True, verbose_name='Data zakończenia działalności'),
        ),
        migrations.AlterField(
            model_name='stacjaradiowa',
            name='kategoria',
            field=models.ManyToManyField(blank=True, null=True, through='stacje.KategorieStacji', to='stacje.Kategoria'),
        ),
        migrations.AlterField(
            model_name='stacjaradiowa',
            name='link',
            field=models.URLField(blank=True, max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='stacjaradiowa',
            name='miasto',
            field=models.ManyToManyField(blank=True, null=True, through='stacje.StacjeWMiescie', to='stacje.Miasto'),
        ),
    ]
