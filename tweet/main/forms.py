from django import forms
from main.models import User, Tweet


class UserForm(forms.ModelForm):
	password = forms.CharField(widget = forms.PasswordInput)
	class Meta: 
		model = User

class TweetForm(forms.ModelForm):
	class Meta: 
		model = Tweet