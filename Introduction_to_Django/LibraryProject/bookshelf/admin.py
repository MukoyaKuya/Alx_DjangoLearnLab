from django.contrib import admin
from .models import Book  # import your model

# Basic registration
# admin.site.register(Book)

# --- Better: Create a custom admin class ---
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    # Fields you want to display in the list view
    list_display = ('title', 'author', 'publication_year')

    # Add filters (sidebar filtering)
    list_filter = ('publication_year', 'author')

    # Add a search box
    search_fields = ('title', 'author')
