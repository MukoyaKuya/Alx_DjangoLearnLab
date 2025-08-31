# Update a Book

```python
from bookshelf.models import Book

# Retrieve the book
book = Book.objects.get(title="1984")

# Update fields
book.author = "Eric Arthur Blair"
book.publication_year = 1950
book.save()

# Check updated record
Book.objects.all()
# <QuerySet [<Book: 1984 by Eric Arthur Blair (1950)>]>
