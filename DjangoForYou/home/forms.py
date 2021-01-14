from django import forms
from home.models import Post, BlogComment

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ("author","title","body","read_time",)
