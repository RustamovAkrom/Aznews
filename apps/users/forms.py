from django import forms
from .models import User


class UserProfileForm(forms.ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        "type":"text", "name":"first_name", "placeholder":"First Name", "class":"single-input",
        "onfocus":"this.placeholder = ''", "onblur":"this.placeholder = 'First Name'"
    }))
    last_name = forms.CharField(widget=forms.TextInput(attrs={
        "type":"text", "name":"last_name", "placeholder":"Last Name","class":"single-input",
        "onfocus":"this.placeholder = ''", "onblur":"this.placeholder = 'Last Name'"
    }))
    username = forms.CharField(widget=forms.TextInput(attrs={
        "type":"text", "name":"username", "placeholder":"Username","class":"single-input",
        "onfocus":"this.placeholder = ''", "onblur":"this.placeholder = 'Username'", "required":None
    }))
    website = forms.URLField(widget=forms.URLInput(attrs={
        "type":"url", "name":"website", "placeholder":"Website","class":"single-input",
        "onfocus":"this.placeholder = ''", "onblur":"this.placeholder = 'Website'"
    }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        "type":"email", "name":"EMAIL", "placeholder":"Email address","class":"single-input",
        "onfocus":"this.placeholder = ''", "onblur":"this.placeholder = 'Email address'"
    }))
    address = forms.CharField(widget=forms.TextInput(attrs={
        "type":"text", "name":"address", "placeholder":"Address","class":"single-input",
        "onfocus":"this.placeholder = ''", "onblur":"this.placeholder = 'Email address'"
    }))
    bio = forms.CharField(widget=forms.Textarea(attrs={
        "placeholder":"Bio","class":"single-input",
        "onfocus":"this.placeholder = ''", "onblur":"this.placeholder = 'Bio'"
    }))
    class Meta:
        model = User
        fields = ("avatar", 
                  "first_name", 
                  "last_name", 
                  "username", 
                  "website",
                  "bio",
                  "email",
                  "address",
                  "city",
                  "country", )