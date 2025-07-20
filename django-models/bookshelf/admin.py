from django.contrib import admin
from .models import Book

class BookAdmin(admin.ModelAdmin):
    # Fields to display in the list view
    list_display = ('title', 'author', 'publication_year')
    
    # Enable search by title and author
    search_fields = ('title', 'author')
    
    # Add filters for publication_year
    list_filter = ('publication_year',)

# Register the Book model with the custom admin class
admin.site.register(Book, BookAdmin)