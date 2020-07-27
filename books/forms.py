from django import forms
from .models import Book, Author
from cloudinary.forms import CloudinaryJsFileField


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'
    cover = CloudinaryJsFileField()


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ('first_name', 'last_name', 'dob')
