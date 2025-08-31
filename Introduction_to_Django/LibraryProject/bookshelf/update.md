# Update a Book

To update an existing book in the bookshelf, modify its fields using the update command.

```python
book = bookshelf.get("1984")
book.title = "Nineteen Eighty-Four"
bookshelf.update(book)
