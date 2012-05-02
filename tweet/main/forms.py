from django import forms
from main.models import User, Tweet
import pdb; pdb.set_trace() 


class UserForm(forms.ModelForm):
	class Meta: 
		model = User

class TweetForm(forms.ModelForm):
	class Meta: 
		model = Tweet