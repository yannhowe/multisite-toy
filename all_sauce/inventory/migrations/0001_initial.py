# Generated by Django 3.0.4 on 2020-03-18 13:39

import datetime
from django.db import migrations, models
import inventory.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sauce',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('category', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('location', models.CharField(max_length=50)),
                ('purchase_date', models.DateField(default=datetime.datetime.now)),
                ('expriy_date', models.DateField(default=inventory.models.Sauce.get_expiry_date)),
            ],
        ),
    ]
