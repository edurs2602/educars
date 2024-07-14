from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['vehicle_id', 'about', 'location', 'description', 'price', 'images']
