# Generated by Django 3.0.6 on 2020-06-01 01:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0028_recivedorders'),
    ]

    operations = [
        migrations.AddField(
            model_name='pizzabase',
            name='image',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]