# Generated by Django 4.2.4 on 2023-10-03 15:15

import django.contrib.auth.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0017_profile_delete_userprofile'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='date_modified',
            field=models.DateField(auto_now=True, verbose_name=django.contrib.auth.models.User),
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
    ]
