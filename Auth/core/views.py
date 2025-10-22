"""
View functions for user authentication and dashboard access.

This module provides views for:
- User registration (signup)
- Authentication (login/logout)
- Dashboard access (with different views for doctors/patients)

All views use the 'accounts:' URL namespace and corresponding templates
in the core/templates directory.
"""

from django.shortcuts import render, redirect
from .forms import SignUpForm
from django.contrib.auth import authenticate, login,logout
from .forms import CustomLoginForm
from django.contrib.auth.decorators import login_required

def signup_view(request):
    """
    Handle user registration with profile creation.

    Displays and processes the signup form for new user registration.
    Creates both User and UserProfile instances on successful submission.

    Args:
        request (HttpRequest): The request object

    Returns:
        HttpResponse: Rendered signup form or redirect to login
        - GET: Renders 'signup.html' with empty SignUpForm
        - POST: If valid, creates user and redirects to login
               If invalid, renders form with validation errors
    """
    if request.method == "POST":
        form = SignUpForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("accounts:login")
    else:
        form = SignUpForm()
    return render(request, "signup.html", {"form": form})


def login_view(request):
    """
    Handle user authentication and login.

    Displays and processes the login form. On successful authentication,
    redirects to the dashboard. Failed login attempts display an error.

    Args:
        request (HttpRequest): The request object

    Returns:
        HttpResponse: Rendered login form or redirect to dashboard
        - GET: Renders 'login.html' with empty CustomLoginForm
        - POST: If valid credentials, redirects to dashboard
               If invalid, renders form with error message
    """
    if request.method == 'POST':
        form = CustomLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('accounts:dashboard')  # any page after login
            else:
                form.add_error(None, "Invalid username or password.")
    else:
        form = CustomLoginForm()
    return render(request, 'login.html', {'form': form})


@login_required
def logout_view(request):
    """
    Handle user logout.

    Logs out the current user and redirects to the login page.
    Protected by @login_required decorator.

    Args:
        request (HttpRequest): The request object

    Returns:
        HttpResponseRedirect: Redirects to login page
    """
    logout(request)
    return redirect("accounts:login")


@login_required
def dashboard_view(request):
    """
    Display user dashboard based on role.

    Shows different dashboard views for doctors and patients based on
    the user's is_doctor profile flag. Protected by @login_required.

    Args:
        request (HttpRequest): The request object

    Returns:
        HttpResponse: Rendered dashboard.html with user context
        - For doctors: Includes doctor-specific dashboard component
        - For patients: Includes patient-specific dashboard component

    Note:
        Template uses user.userprofile.is_doctor to determine which
        dashboard component to include.
    """
    user = request.user
    return render(request, "dashboard.html", {"user": user})


def home_view(request):
    """
    Display documentation homepage with route information.

    Shows all available routes, their purposes, and authentication
    requirements. Also displays current login status and quick links.

    Args:
        request (HttpRequest): The request object

    Returns:
        HttpResponse: Rendered home.html with current user context
    """
    return render(request, "home.html")