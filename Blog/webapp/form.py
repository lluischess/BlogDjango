from django import forms
from froala_editor.widgets import FroalaEditor
from .models import Article


class BlogForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['content']


class BlogForm2(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'content', 'image']
