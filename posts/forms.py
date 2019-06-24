from django import forms
from .models import Post

#class PostForm (forms.Form):

class PostModelForm (forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'description', 'image', 'slug']