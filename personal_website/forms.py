from django.contrib.auth.forms import AuthenticationForm as BaseAuthenticationForm
from django import forms

class AuthenticationForm(BaseAuthenticationForm):
	username = forms.CharField(
		widget=forms.TextInput(
			attrs={
				'class': 'form-control',
				'placeholder': 'Type your username',
			}
		)
	)

	password = forms.CharField(
		widget=forms.PasswordInput(
			attrs={
				'class': 'form-control',
				'placeholder':'Type your password'
			}
		)
	)
