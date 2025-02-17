# Generated by Django 5.0.6 on 2024-07-03 18:44

import base.services
import django.core.validators
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='author',
        ),
        migrations.AlterField(
            model_name='book',
            name='avatar',
            field=models.ImageField(upload_to=base.services.get_book_avatar_upload_file, validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['jpg', 'png']), base.services.audio_size_validator]),
        ),
        migrations.AddField(
            model_name='book',
            name='author',
            field=models.ForeignKey(default=123, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
