# Generated by Django 3.0.6 on 2020-05-30 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0023_auto_20200529_1351'),
    ]

    operations = [
        migrations.CreateModel(
            name='RecivedOrders',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=65)),
                ('all_items', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
    ]
