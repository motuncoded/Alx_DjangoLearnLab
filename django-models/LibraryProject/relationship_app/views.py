from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView
from .models import Book, Library

# Function-based view: list all books
def list_books(request):
    books = Book.objects.select_related('author').all()
    return render(request, 'list_books.html', {'books': books})

# Class-based view: show details of a specific library
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'library_detail.html'
    context_object_name = 'library'