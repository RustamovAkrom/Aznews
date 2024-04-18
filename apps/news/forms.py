from django import forms
from .models import Contact


class DetailsContactForm(forms.Form):
    message = forms.CharField(widget=forms.Textarea(attrs={
        "class":"form-control w-100 error", "name":"message", 
        "id":"message", "cols":"30", "rows":"9", 
        "onfocus":"this.placeholder = ''", "onblur":"this.placeholder = 'Enter Message", 
        "placeholder":"Enter Message"
    }))
    name = forms.CharField(widget=forms.TextInput(attrs={
        "class":"form-control error", "name":"name", 
        "id":"name", "type":"text", "onfocus":"this.placeholder = ''", 
        "onblur":"this.placeholder = 'Enter your name'", "placeholder":"Enter your name"
    }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        "class":"form-control error", "name":"email", 
        "id":"email", "type":"email", "onfocus":"this.placeholder = ''", 
        "onblur":"this.placeholder = 'Enter your email'", "placeholder":"Enter your email"
    }))
    subject = forms.CharField(widget=forms.TextInput(attrs={
        "class":"form-control error", "name":"subject", 
        "id":"subject", "type":"text", "onfocus":"this.placeholder = ''", 
        "onblur":"this.placeholder = 'Enter subject'", "placeholder":"Enter subject"
    }))

    class Meta:
        model = Contact
        fields = ("message", "name", "email", "subject")
    