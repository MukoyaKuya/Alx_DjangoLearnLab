# Delete a Book

To delete a book from the bookshelf, follow this example:

```python
bookshelf = [
    {"title": "Nineteen Eighty-Four", "author": "George Orwell"},
    {"title": "Animal Farm", "author": "George Orwell"},
]

# Delete the book "Nineteen Eighty-Four"
bookshelf = [book for book in bookshelf if book["title"] != "Nineteen Eighty-Four"]

print("Updated bookshelf:", bookshelf)
