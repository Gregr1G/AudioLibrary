from django.urls import path
from .views import *

urlpatterns = [
    path("books-list/", BooksViewSet.as_view({'get': 'list', 'post': 'create'})),
    path("books-list/<int:pk>/", BooksViewSet.as_view({'put': 'update', 'delete': 'destroy'})),

    path("public-genres-list/", GenresListAPIView.as_view()),
    path("public-books-by-genre/<int:pk>/", PublicBooksListFilteredView.as_view({'get': 'list'})),

    path("public-books-list/", PublicBooksListView.as_view({'get': 'list'})),
    path("public-books-list/<int:pk>/", PublicBooksListView.as_view({'get': 'retrieve'})),
]

