# Create a Book

```python
from bookshelf.models import Book
Book.objects.create(title="1984", author="George Orwell", published_year=1949)
