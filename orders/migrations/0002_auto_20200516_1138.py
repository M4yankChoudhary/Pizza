# Generated by Django 3.0.6 on 2020-05-16 11:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pizza',
            name='base',
        ),
        migrations.AddField(
            model_name='pizza',
            name='name',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='pizzabase', to='orders.PizzaBase'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='pizza',
            name='size',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.PizzaSize'),
        ),
        migrations.CreateModel(
            name='PizzaTopping',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pizza_topping', models.CharField(max_length=60)),
                ('base', models.ManyToManyField(related_name='pizzatopping', to='orders.PizzaBase')),
                ('size', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pizzasize', to='orders.PizzaSize')),
            ],
        ),
        migrations.AlterField(
            model_name='pizza',
            name='pizza_topping',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pizzatopping', to='orders.PizzaTopping'),
        ),
    ]
