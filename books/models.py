from django.db import models
from django.core.validators import FileExtensionValidator
from base.services import *
from django.contrib.auth.models import User

class Genre(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name

class Book(models.Model):
    genre_name = models.ManyToManyField(Genre)
    title = models.CharField(max_length=100)
    desc = models.TextField()
    file = models.FileField(upload_to=get_audio_upload_file, validators=[FileExtensionValidator(allowed_extensions=["mp3"]), audio_size_validator], null=True, blank=True)
    avatar = models.ImageField(upload_to=get_book_avatar_upload_file, validators=[FileExtensionValidator(allowed_extensions=["jpg", "png"]), audio_size_validator], null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

