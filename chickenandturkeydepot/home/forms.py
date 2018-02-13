from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import MyUser


class SignUpForm(UserCreationForm):
	username = forms.CharField(max_length=30, help_text='Required.')
	first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
	last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
	email = forms.EmailField(max_length=254, help_text='Required, Valid email address.')

	class Meta:
		model = MyUser
		fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2',)




