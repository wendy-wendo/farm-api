# Generated by Django 5.0.6 on 2024-07-05 05:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_vendorproduct'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('buyers_email', models.EmailField(max_length=254)),
                ('sellers_email', models.EmailField(max_length=254)),
                ('qty', models.IntegerField(default=1)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('order_by', models.CharField(choices=[('buyer', 'Buyer'), ('farmer', 'Farmer')], default='buyer', max_length=15)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.product')),
            ],
        ),
    ]