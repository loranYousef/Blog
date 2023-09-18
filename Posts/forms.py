from django import forms
from .models import Post
from .models import Kontakt




class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title','content','author','tags','image']


class KontakttForm(forms.ModelForm):
    class Meta:
        model = Kontakt
        fields = '__all__'