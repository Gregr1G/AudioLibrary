# Generated by Django 5.0.6 on 2024-07-02 23:09

import base.services
import django.core.validators
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('desc', models.TextField()),
                ('file', models.FileField(upload_to=base.services.get_audio_upload_file, validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['mp3']), base.services.audio_size_validator])),
                ('avatar', models.ImageField(upload_to=base.services.get_book_avatar_upload_file, validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['jpg']), base.services.audio_size_validator])),
                ('author', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
                ('genre_name', models.ManyToManyField(to='books.genre')),
            ],
        ),
    ]
