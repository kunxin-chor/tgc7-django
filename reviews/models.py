from django.db import models

# import the book model from the Reviews app
from books.models import Book

# Create your models here.


class Review(models.Model):
    title = models.CharField(max_length=255, blank=False)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    # because of the content of the review is likely to be super long
    # so we can use text field isntead of char field.
    content = models.TextField(blank=False)
    date = models.DateField(blank=False)

    def __str__(self):
        return self.title
