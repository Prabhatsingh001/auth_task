"""
Database models for the core application.

This module defines the extended user profile model that adds additional
fields to Django's built-in User model through a one-to-one relationship.
"""

from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    """
    Extended user profile model that adds additional fields to the User model.

    This model extends Django's built-in User model through a one-to-one
    relationship, adding fields for profile pictures, role identification,
    and address information.

    Attributes:
        user (OneToOneField): Link to Django's User model
        profile_picture (ImageField): User's profile photo, optional
            Stored in 'profile_pics/' directory
        is_doctor (BooleanField): Flags whether the user is a doctor
            Defaults to False (patient)
        address_line1 (CharField): Primary address line
        city (CharField): User's city
        state (CharField): User's state
        pincode (CharField): Postal/ZIP code

    Note:
        When a User is deleted, their UserProfile will be deleted automatically
        due to the CASCADE deletion rule on the OneToOneField.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    is_doctor = models.BooleanField(default=False)
    address_line1 = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    pincode = models.CharField(max_length=100)

    def __str__(self):
        return self.user.username

