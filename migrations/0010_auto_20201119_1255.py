# Generated by Django 3.1.2 on 2020-11-19 07:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flight', '0009_auto_20201119_1156'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='flight_date',
            field=models.DateField(blank=True),
        ),
    ]
