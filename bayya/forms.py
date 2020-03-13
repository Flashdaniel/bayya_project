from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    name= forms.CharField(max_length=200, required=True)
    bitcoin_address = forms.CharField(max_length=30)

    class Meta:
        model = User
        fields = ('name', 'email', 'bitcoin_address' , 'password1', 'password2')
