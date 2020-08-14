from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import CustomerProfile

class CreateUserForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ("username", "email", "first_name", "last_name", "password1", "password2")

    def clean_email(self):
        email = self.cleaned_data.get('email')

        try:
            match = User.objects.get(email = email)
        except User.DoesNotExist:
            return email

        raise forms.ValidationError('This email address is already in use.')

class CustomerForm(ModelForm):
    class Meta:
        model = CustomerProfile
        fields = '__all__'
        exclude = ['user']