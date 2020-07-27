from django import forms
from .models import Book, Author, Genre


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        # tuple are in round parenthesis
        # they are like lists in Python
        # once we put something in a tuple, we cannot change the tuple anymore
        fields = ('title', 'desc', 'ISBN', 'pageCount', 'genre', 'category',
                  'tags', 'authors', 'owner')


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ('first_name', 'last_name', 'dob')


# SearchForm inherits from `forms.Form`, not `forms.ModelForm`
# This is because the search form doesn't have any models
# meaning it does not refer to any tables in our SQL database
class SearchForm(forms.Form):
    # the requried is `False` so that if the user leaves it blank
    # it will return all the books
    title = forms.CharField(max_length=100, required=False)

    # Genre.objects.all() is eqv to "SELECT * FROM Genre"
    # take the results of Genre.objects.all and populate the <select>
    genre = forms.ModelChoiceField(queryset=Genre.objects.all(),
                                   required=False)

    min_page_count = forms.IntegerField(required=False)
