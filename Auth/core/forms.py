from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UserProfile


class SignUpForm(UserCreationForm):
    # Extra user fields
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)

    # Profile fields
    profile_pricture = forms.ImageField(required=False)
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
            "profile_pricture", "is_doctor",
            "address_line1", "city", "state", "pincode",
        ]

    def save(self, commit=True):
        user = super().save(commit=commit)
        UserProfile.objects.create(
            user=user,
            profile_pricture=self.cleaned_data.get("profile_pricture"),
            is_doctor=self.cleaned_data.get("is_doctor"),
            address_line1=self.cleaned_data.get("address_line1"),
            city=self.cleaned_data.get("city"),
            state=self.cleaned_data.get("state"),
            pincode=self.cleaned_data.get("pincode"),
        )
        return user

class CustomLoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))

