# Generated by Django 4.2.4 on 2023-10-15 17:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('social', '0043_alter_conversationmessage_unique_together_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Story',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, upload_to='stories')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('expiration_time', models.DateTimeField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('viewers', models.ManyToManyField(blank=True, related_name='viewed_stories', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
