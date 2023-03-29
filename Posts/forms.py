from django import forms
from .models import Post




class PostForm(forms.ModelForm):
    class class Meta:
        model = Post
        fields = '__all__'