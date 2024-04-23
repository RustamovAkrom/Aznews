from django import forms
from apps.shared.models import AnonimusUserEmails
from .models import Comment, Post

class SaveAnonimousUserEmailForm(forms.ModelForm):
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
        

class WriteCommentForm(forms.ModelForm):
    message = forms.CharField(widget=forms.Textarea(attrs={
        "class":"form-control w-100", "name":"comment", "id":"comment", "cols":"30", "rows":"9"
    }))
    class Meta:
        model = Comment
        fields = ("message", )


class CreatePostForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={
        "type":"text", "name":"title", "placeholder":"Title", "class":"single-input",
        "onfocus":"this.placeholder = ''", "onblur":"this.placeholder = 'Title'"
    }))
    descriptions = forms.CharField(widget=forms.TextInput(attrs={
        "type":"text", "name":"descriptions", "placeholder":"Descriptions", "class":"single-input",
        "onfocus":"this.placeholder = ''", "onblur":"this.placeholder = 'Descriptions'"
    }))
    content = forms.CharField(widget=forms.Textarea(attrs={
        "type":"text", "name":"content", "placeholder":"Content", "class":"single-input",
        "onfocus":"this.placeholder = ''", "onblur":"this.placeholder = 'Content'"
    }))
    
    # categories = forms.CharField(widget=forms.TextInput(attrs={
    #     "type":"text", "name":"categori", "placeholder":"Categori", "class":"single-input",
    #     "onfocus":"this.placeholder = ''", "onblur":"this.placeholder = 'Categori'"
    # }))
    # tags = forms.CharField(widget=forms.TextInput(attrs={
    #     "type":"text", "name":"tags", "placeholder":"Tag", "class":"single-input",
    #     "onfocus":"this.placeholder = ''", "onblur":"this.placeholder = 'Tag'"
    # }))
    content_image = forms.FileField(widget=forms.FileInput(attrs={
        "type":"file", "name":"content_image", "placeholder":"Post image", "class":"single-input",
        "onfocus":"this.placeholder = ''", "onblur":"this.placeholder = 'Post image'"
    }))
    is_active = forms.BooleanField()

    class Meta:
        model = Post
        fields = ("title", "descriptions", "content", "categories", "tags", "content_image", "is_active")