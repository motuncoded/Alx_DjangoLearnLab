from bookshelf.models import Book
# Delete the book instance
book.delete()

# Confirm deletion by trying to retrieve all books
all_books = Book.objects.all()
print(all_books)