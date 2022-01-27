from django import forms
from .models import Book

class NewBookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author']

class RentBookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['author']
        widgets = {'author': forms.HiddenInput()}