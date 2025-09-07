# Deleting a Book from the Bookshelf

To delete a book object from the database, first import the `Book` model, then use the `.delete()` method.

```python
from bookshelf.models import Book

# Get the book you want to delete
book = Book.objects.get(title="Nineteen Eighty-Four")

# Delete the book
book.delete()
