from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import images
from django import forms

class ImageForm(forms.ModelForm):
    
    class Meta:
        model = images
        fields = ['name' , 'image']
