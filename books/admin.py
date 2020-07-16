from django.contrib import admin
# from the models.py in the same direction as admin.py, import in Book
from .models import Book, Author

# Register your models here.
admin.site.register(Book)
admin.site.register(Author)
