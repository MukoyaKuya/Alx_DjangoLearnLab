import django
import os

# Setup Django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "LibraryProject.settings")
django.setup()

from relationship_app.models import Author, Book, Library, Librarian


def run_queries():
    # Query 1: All books by a specific author
    author_name = "J.K. Rowling"
    author = Author.objects.filter(name=author_name).first()
    if author:
        books_by_author = author.books.all()
        print(f"Books by {author_name}: {[book.title for book in books_by_author]}")

    # Query 2: List all books in a library
    library_name = "Central Library"
    library = Library.objects.filter(name=library_name).first()
    if library:
        books_in_library = library.books.all()
        print(f"Books in {library_name}: {[book.title for book in books_in_library]}")

    # Query 3: Retrieve the librarian for a library
    if library and hasattr(library, "librarian"):
        print(f"Librarian at {library_name}: {library.librarian.name}")


if __name__ == "__main__":
    run_queries()
