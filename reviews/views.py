from django.shortcuts import render, HttpResponse, get_object_or_404
from .forms import ReviewForm
from books.models import Book

# Create your views here.


def index(request):
    # return HttpResponse("Reviews")
    return render(request, 'reviews/index.template.html')


# three things to do for the "C" part of the CRUD
# 1. the view
# 2. the template
# 3. the url
def create_review(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            # create a review based on the data in the form
            # BUT don't save to the database yet
            review = form.save(commit=False)

            # fill in the review's user id
            # RMEMEBR: request.user holds the user that is logged in

            # in other words, set the user of the review to be the
            # same as whichever user is logged in right now
            review.user = request.user

            # fill in which book the review is for
            review.book = book

            # save the review maually
            review.save()
            return HttpResponse("Review is created")
        else:
            return HttpResponse("Form has error")
    else:
        form = ReviewForm()
        return render(request, 'reviews/create_review.template.html', {
            "form": form,
            "book": book
        })
