# Generated by Django 5.0.6 on 2024-06-15 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
    ]