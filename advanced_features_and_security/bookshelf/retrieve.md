# Retrieve the book just created
book = Book.objects.get(title="1984")
print(book)