from typing import Any
from django import forms
from .models import User
from django.core.exceptions import ValidationError


class UserProfileForm(forms.ModelForm):
    avatar = forms.FileField(widget=forms.FileInput(attrs={
        "type":"file", "name":"avatar", "placeholder":"Your avatar", "class":"single-input",
        "onfocus":"this.placeholder = ''", "onblur":"this.placeholder = 'Your avatar'"
    }))
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
        "onfocus":"this.placeholder = ''", "onblur":"this.placeholder = 'Address'"
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
        
    
class UserRegisterForm(forms.ModelForm):
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
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        "type":"email", "name":"EMAIL", "placeholder":"Email address","class":"single-input",
        "onfocus":"this.placeholder = ''", "onblur":"this.placeholder = 'Email address'"
    }))
    password1 = forms.CharField(max_length=50, widget=forms.PasswordInput(attrs={
        "type":"password", "name":"password", "placeholder":"Password 1","class":"single-input",
        "onfocus":"this.placeholder = ''", "onblur":"this.placeholder = 'Password 1'"
    }))
    password2 = forms.CharField(max_length=50, widget=forms.PasswordInput(attrs={
        "type":"password", "name":"password", "placeholder":"Password 2","class":"single-input",
        "onfocus":"this.placeholder = ''", "onblur":"this.placeholder = 'Password 2'"
    }))


    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "email", 
                  "password1", "password2")
        
    def save(self, commit = True):
        user = super().save(commit)
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")

        if password1 == password2:
            user.set_password(password1)
            user.save()
        else:
            raise ValidationError("Password must be match")
        

class UserLoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={
        "type":"text", "name":"username", "placeholder":"Username","class":"single-input",
        "onfocus":"this.placeholder = ''", "onblur":"this.placeholder = 'Username'", "required":None
    }))
    password = forms.CharField(max_length=50, widget=forms.PasswordInput(attrs={
        "type":"password", "name":"password", "placeholder":"Password","class":"single-input",
        "onfocus":"this.placeholder = ''", "onblur":"this.placeholder = 'Password'"
    }))
    