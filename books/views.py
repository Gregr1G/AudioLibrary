from django.http import FileResponse, Http404
from rest_framework import generics, viewsets, views

from .serializers import *
from .models import *
from base.permisions import IsAuthor

class StreamingFileView(views.APIView):
    def get(self, request, pk):
        audio = generics.get_object_or_404(Book, id=pk)
        if os.path.exists(audio.file.path):
            return FileResponse(open(audio.file.path, 'rb'), filename=audio.file.path)
        else:
            return Http404

class DownloadFileView(views.APIView):
    def get(self, request, pk):
        audio = generics.get_object_or_404(Book, id=pk)
        if os.path.exists(audio.file.path):
            return FileResponse(open(audio.file.path, 'rb'), filename=audio.file.path, as_attachment=True)
        else:
            return Http404

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