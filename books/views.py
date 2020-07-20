from django.shortcuts import render, HttpResponse, redirect, reverse, get_object_or_404
from .models import Book, Author
from .forms import BookForm, AuthorForm

# Create your views here.
# A view (in other words, a view function) refers to a function
# that is called when its corrosponding URL is visited in the browser


# ALL view functions must take in the variable request as the first argumernt
def index(request):
    fname = "Paul"
    lname = "Chor"
    return render(request, 'books/index.template.html', {
        'first_name': fname,
        'last_name': lname
    })


def show_books(request):
    # SELECT * FROM Books
    all_books = Book.objects.all()
    return render(request, 'books/all_books.template.html', {
        'books': all_books
    })


def create_book(request):

    # check if we are submitting the form
    if request.method == "POST":
        print(request.POST)

        # create the BooKForm by filling it with data from the user's
        # submission
        form = BookForm(request.POST)
        # create a model based on the data in the form
        form.save()

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
