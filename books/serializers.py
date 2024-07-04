from rest_framework import serializers
from .models import *

class BooksListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"

class GenresListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = "__all__"