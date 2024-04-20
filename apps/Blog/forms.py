from django import forms
from apps.shared.models import AnonimusUserEmails
from .models import Comment

class SaveAnonimousUserEmail(forms.ModelForm):
    email = forms.CharField(widget=forms.TextInput(attrs={
        "type":"email", 
        "class":"form-control",
        "onfocus":"this.placeholder = ''",
        "onblur":"this.placeholder = 'Enter email'",
        "placeholder":"Enter email",
        "required":None
        }))
    
    class Meta:
        model = AnonimusUserEmails
        fields = ("email", )
        

class WriteComment(forms.ModelForm):
    message = forms.CharField(widget=forms.Textarea(attrs={
        "class":"form-control w-100", "name":"comment", "id":"comment", "cols":"30", "rows":"9"
    }))
    class Meta:
        model = Comment
        fields = ("message", )