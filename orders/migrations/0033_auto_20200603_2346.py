# Generated by Django 3.0.6 on 2020-06-03 23:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0032_recivedorders_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recivedorders',
            name='time',
            field=models.CharField(max_length=65),
        ),
    ]
