# Generated by Django 4.2.4 on 2023-11-21 14:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0063_profile_is_live_livesession'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='is_live',
        ),
        migrations.DeleteModel(
            name='LiveSession',
        ),
    ]
