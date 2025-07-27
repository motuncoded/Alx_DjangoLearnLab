from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import permission_required
from .models import Book

# ...existing imports...

@permission_required('bookshelf.can_create', raise_exception=True)
def add_book(request):
    # Logic to add a book
    pass

@permission_required('bookshelf.can_delete', raise_exception=True)
def delete_book(request, pk):
    # Logic to delete a book
    pass

def book_list(request):
    books = Book.objects.all()
    return render(request, 'bookshelf/book_list.html', {'books': books})

# ...existing code...
# filepath: c:\Users\Dell\Desktop\Alx_DjangoLearnLab\advanced_features_and_security\LibraryProject\bookshelf\views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import permission_required
from .models import Book

# ...existing imports...

@permission_required('bookshelf.can_create', raise_exception=True)
def add_book(request):
    # Logic to add a book
    pass

@permission_required('bookshelf.can_delete', raise_exception=True)
def delete_book(request, pk):
    # Logic to delete a book
    pass

def book_list(request):
    books = Book.objects.all()
    return render(request, 'bookshelf/book_list.html', {'books': books})