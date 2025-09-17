from django.contrib.auth.decorators import permission_required
from django.contrib.auth.decorators import user_passes_test, login_required
from django.shortcuts import render
from .models import UserProfile


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

