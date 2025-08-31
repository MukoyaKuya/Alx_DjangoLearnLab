# Create a new Book
from bookshelf.models import Book
book = Book.objects.create(title="Django Basics", author="Delton", year=2025)
