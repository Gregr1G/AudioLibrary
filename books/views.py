from rest_framework import generics, viewsets
from .serializers import *
from .models import *
from base.permisions import IsAuthor

class BooksViewSet(viewsets.ModelViewSet):
    serializer_class = BooksListSerializer
    permission_classes = [IsAuthor]

    def get_queryset(self):
        return Book.objects.filter(author=self.request.user)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class GenresListAPIView(generics.ListAPIView):
    serializer_class = GenresListSerializer
    queryset = Genre.objects.all()

class PublicBooksListView(viewsets.ReadOnlyModelViewSet):
    serializer_class = BooksListSerializer
    queryset = Book.objects.all()

class PublicBooksListFilteredView(viewsets.ReadOnlyModelViewSet):
    serializer_class = BooksListSerializer
    def get_queryset(self):
        return Book.objects.filter(genre_name=self.kwargs["pk"])