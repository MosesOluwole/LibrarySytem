# library/forms.py

from django import forms
from .models import Book, Member


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'isbn', 'published_date']


class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ['name', 'email']
