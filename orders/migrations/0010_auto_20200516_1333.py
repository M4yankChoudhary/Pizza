# Generated by Django 3.0.6 on 2020-05-16 13:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0009_auto_20200516_1330'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pizza',
            name='pizza_topping',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pizza_top', to='orders.PizzaTopping'),
        ),
    ]
