from django.urls import path
from .views import list_books

urlpatterns = [
    path('books/', list_books, name='list-books'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library-detail'),
]