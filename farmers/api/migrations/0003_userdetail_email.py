# Generated by Django 5.0.6 on 2024-06-11 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_remove_userdetail_userid_userdetail_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdetail',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
    ]
