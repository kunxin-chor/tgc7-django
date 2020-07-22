from django.contrib import admin
# from the models.py in the same direction as admin.py, import in Book
from .models import Book, Author, Genre, Category, Tag

# Register your models here.
admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Genre)
admin.site.register(Category)
admin.site.register(Tag)
