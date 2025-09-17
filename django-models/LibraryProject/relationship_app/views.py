from django.contrib.auth.decorators import permission_required
from django.contrib.auth.decorators import user_passes_test, login_required
from django.shortcuts import render
from .models import UserProfile
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import permission_required
from .models import Book

@permission_required('relationship_app.can_add_book', raise_exception=True)
def add_book(request):
    # your logic to add a book
    return render(request, 'relationship_app/add_book.html')

@permission_required('relationship_app.can_change_book', raise_exception=True)
def edit_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    # your logic to edit the book
    return render(request, 'relationship_app/edit_book.html', {'book': book})

@permission_required('relationship_app.can_delete_book', raise_exception=True)
def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    # your logic to delete the book
    book.delete()
    return redirect('book_list')

# Helper functions to check role
def is_admin(user):
    try:
        return user.is_authenticated and user.profile.role == UserProfile.ROLE_ADMIN
    except Exception:
        return False

def is_librarian(user):
    try:
        return user.is_authenticated and user.profile.role == UserProfile.ROLE_LIBRARIAN
    except Exception:
        return False

def is_member(user):
    try:
        return user.is_authenticated and user.profile.role == UserProfile.ROLE_MEMBER
    except Exception:
        return False

# Admin view (only for Admin role)
@user_passes_test(is_admin, login_url="login")
def admin_view(request):
    # you can add admin-specific context here
    return render(request, "relationship_app/admin_view.html", {"user": request.user})

# Librarian view (only for Librarian role)
@user_passes_test(is_librarian, login_url="login")
def librarian_view(request):
    return render(request, "relationship_app/librarian_view.html", {"user": request.user})

# Member view (only for Member role)
@user_passes_test(is_member, login_url="login")
def member_view(request):
    return render(request, "relationship_app/member_view.html", {"user": request.user})


