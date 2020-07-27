from django.shortcuts import render, HttpResponse, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from .models import Book, Author
from .forms import BookForm, AuthorForm, SearchForm

# Create your views here.
# A view (in other words, a view function) refers to a function
# that is called when its corrosponding URL is visited in the browser


# ALL view functions must take in the variable request as the first argumernt
def index(request):
    form = SearchForm(request.GET)

    if request.GET:
        # create a query that is always true
        query = ~Q(pk__in=[])  # This means TRUE
        # WHERE 1

        # if the user fills in the title and the title is not an empty string
        if 'title' in request.GET and request.GET['title']:
            title = request.GET['title']
            query = query & Q(title__icontains=title)
            # WHERE 1 and title LIKES "%{title}%"

        if 'genre' in request.GET and request.GET['genre']:
            genre_id = request.GET['genre']
            query = query & Q(genre=genre_id)

        if 'min_page_count' in request.GET and request.GET['min_page_count']:
            min_page_count = request.GET['min_page_count']
            page_query = Q(pageCount__gte=min_page_count)
            query = query & page_query

        # select all the books
        # SELECT * FROM Books
        books = Book.objects.all()

        # SELECT * FROM Books WHERE 1 and title LIKES "%{title}%"
        # make sure to reassign back to the query set
        books = books.filter(query)

        return render(request, 'books/index.template.html', {
            'form': form,
            'books': books
        })
    else:
        # if the user never submit form, then just display the books:
        books = Book.objects.all()
        return render(request, 'books/index.template.html', {
            'form': form,
            'books': books
        })

    # form = SearchForm(request.GET)

    # # SELECT * FROM Books
    # # books is a QUERY SET
    # books = Book.objects.all()

    # # A query object represents a fragment of a SQL query
    # # means: WHERE title LIKE "%ring%"
    # subquery = Q(title__icontains="fire")

    # # Genre ID 1 is fantasy
    # # Genre ID  2 is science-fic
    # genre_filter = Q(genre=1)  # WHERE genre = 1

    # # books = books.filter(subquery)
    # books = books.filter(subquery)
    # # means: SELECT * FROM Books where Genre =1 AND Title LIKE "%ring%"

    # return render(request, 'books/index.template.html', {
    #     'form': form,
    #     'books': books
    # })


def show_books(request):
    # SELECT * FROM Books
    all_books = Book.objects.all()
    return render(request, 'books/all_books.template.html', {
        'books': all_books
    })


def view_book(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    return render(request, 'books/details.template.html', {
        "book": book
    })


@ login_required
def create_book(request):

    # check if we are submitting the form
    if request.method == "POST":
        print(request.POST)

        # create the BooKForm by filling it with data from the user's
        # submission
        form = BookForm(request.POST)
        # create a model based on the data in the form
        form.save()

        # the book is created
        messages.success(request, "New book has been created")

        # redirect back to the show_books view function
        return redirect(reverse(show_books))

    else:
        # create an instance of the class BookForm and store it in the form
        # variable
        form = BookForm()
        return render(request, 'books/create_book.template.html', {
            'form': form
        })


def show_authors(request):
    all_authors = Author.objects.all()
    return render(request, 'books/all_authors.template.html', {
        'authors': all_authors
    })


def create_author(request):
    # check if has been form has been submitted with data
    # if it has been submited with data, then request.method should be "POST"
    if request.method == "POST":
        # user has submitted the data
        form = AuthorForm(request.POST)
        form.save()

        return redirect(reverse(show_authors))
    else:
        # if user has not submitted data, it's a GET request,
        # so we will just show an empty form
        form = AuthorForm()
        return render(request, 'books/create_author.template.html', {
            'form': form
        })


def update_author(request, author_id):
    # retrieve the author because we either need to update it,
    # or to show it in a form
    author = get_object_or_404(Author, pk=author_id)

    # if the user has submitted the form
    if request.method == "POST":
        form = AuthorForm(request.POST, instance=author)
        form.save()
        return redirect(reverse(show_authors))
    else:
        # if the user didn't submit the form
        form = AuthorForm(instance=author)
        return render(request, 'books/edit_author.template.html', {
            'form': form,
            'author': author
        })


def edit_book(request, book_id):

    # retrieve the book that we want to edit
    book = get_object_or_404(Book, pk=book_id)

    # if the form is submitted, process the update
    if request.method == "POST":
        # the user has submitted data by extracting it from the request.POST
        # and passing it to the form
        form = BookForm(request.POST, instance=book)
        form.save()
        return redirect(reverse(show_books))

    else:
        # if there is no form submitted, then we display the form

        # populate the form with the existing data from the book
        form = BookForm(instance=book)
        return render(request, 'books/edit_book.template.html', {
            'form': form
        })


def delete_book(request, book_id):

    book = get_object_or_404(Book, pk=book_id)

    # if the form is submitted
    if request.method == "POST":
        book.delete()
        return redirect(reverse(show_books))
    else:
        # if no form is submitted (that is, just to see the confirmation)
        return render(request, 'books/confirm_delete_book.template.html', {
            'book': book
        })
