"""
Form classes for user authentication and registration.

This module provides form classes for handling user signup and login functionality:
- SignUpForm: Extended user registration with profile information
- CustomLoginForm: Login form with styled widgets
"""

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UserProfile


class SignUpForm(UserCreationForm):
    """
    Extended user registration form that includes profile information.

    This form extends Django's UserCreationForm to include additional fields
    for both the User model and the associated UserProfile model. On save,
    it creates both a User instance and its associated UserProfile.

    Fields:
        User model fields:
            - username (from UserCreationForm)
            - password1 (from UserCreationForm)
            - password2 (from UserCreationForm)
            - email (required)
            - first_name (required)
            - last_name (required)
        
        Profile fields:
            - profile_picture (optional): Image upload field for user avatar
            - is_doctor (optional): Boolean flag for doctor/patient role
            - address_line1 (required): Primary address line
            - city (required): City name
            - state (required): State name
            - pincode (required): Postal code
    
    Methods:
        save(commit=True): Creates and saves a User instance and its
            associated UserProfile with the form's cleaned data.
            Returns the created User instance.
    """
    # Extra user fields
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)

    # Profile fields
    profile_picture = forms.ImageField(required=False)
    is_doctor = forms.BooleanField(required=False)
    address_line1 = forms.CharField(max_length=255)
    city = forms.CharField(max_length=100)
    state = forms.CharField(max_length=100)
    pincode = forms.CharField(max_length=100)

    class Meta:
        model = User
        fields = [
            "first_name", "last_name", "username",
            "email", "password1", "password2",
            "profile_picture", "is_doctor",
            "address_line1", "city", "state", "pincode",
        ]

    def save(self, commit=True):
        user = super().save(commit=commit)
        UserProfile.objects.create(
            user=user,
            profile_picture=self.cleaned_data.get("profile_picture"),
            is_doctor=self.cleaned_data.get("is_doctor"),
            address_line1=self.cleaned_data.get("address_line1"),
            city=self.cleaned_data.get("city"),
            state=self.cleaned_data.get("state"),
            pincode=self.cleaned_data.get("pincode"),
        )
        return user

class CustomLoginForm(forms.Form):
    """
    Custom login form for user authentication.

    A simple login form that captures username and password for authentication.
    Styling can be applied through template-level classes or form widget attributes.

    Fields:
        username (CharField): Text input for username
        password (CharField): Password input field with masked entry

    Note:
        This form provides basic fields only. Form styling and validation
        messages are handled at the template level.
    """
    username = forms.CharField(required=True)
    password = forms.CharField(required=True, min_length=8)

