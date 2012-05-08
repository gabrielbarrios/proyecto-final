from django import forms
from main.models import User, Tweet


class UserForm(forms.ModelForm):
	password = forms.CharField(widget = forms.PasswordInput)

	class Meta: 
		model = User
		readonly_fields=('nick_name',)

class TweetForm(forms.ModelForm):
	class Meta: 
		model = Tweet