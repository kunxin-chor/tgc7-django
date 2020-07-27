from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Tag(models.Model):
    title = models.CharField(blank=False, max_length=255)

    def __str__(self):
        return self.title


class Genre(models.Model):
    title = models.CharField(blank=False, max_length=255)

    def __str__(self):
        return self.title


class Book(models.Model):
    title = models.CharField(blank=False, max_length=255)
    ISBN = models.CharField(blank=False, max_length=255)
    desc = models.TextField(blank=False)
    pageCount = models.IntegerField(blank=False)
    # relationship to genre
    # if the genre, all the books related to the genre will be deleted as well
    # aka. cascading delete
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)
    authors = models.ManyToManyField('Author')
    # set the owner relationship to be NULLABLE so that it is not complusory for all books to have an owner
    # with `null=True` the relationship is optional (i.e, can be set to NULL)
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    cost = models.DecimalField(max_digits=10, decimal_places=3, blank=False)

    def __str__(self):
        return self.title


class Author(models.Model):
    first_name = models.CharField(blank=False, max_length=80)
    last_name = models.CharField(blank=False, max_length=80)
    dob = models.DateField(blank=False)

    def __str__(self):
        return self.first_name + " " + self.last_name


class Category(models.Model):
    title = models.CharField(blank=False, max_length=255)

    def __str__(self):
        return self.title
