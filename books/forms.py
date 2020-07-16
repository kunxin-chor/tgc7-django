from django import forms
from .models import Book


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        # tuple are in round parenthesis
        # they are like lists in Python
        # once we put something in a tuple, we cannot change the tuple anymore
        fields = ('title', 'desc', 'ISBN', 'pageCount')
