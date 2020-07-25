from django.shortcuts import render, HttpResponse, get_object_or_404
from .forms import ReviewForm
from books.models import Book
from .models import Review
from .forms import CommentForm

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


def create_comment(request, review_id):
    review = get_object_or_404(Review, pk=review_id)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            # commit is False means that we are not saving to the database yet
            comment = form.save(commit=False)
            comment.review = review
            # request.user always refers to the current logged in user
            comment.user = request.user
            # actually save the new comment to database
            comment.save()
            return HttpResponse("Comment created")
        else:
            return HttpResponse("Problem with input")
    else:

        form = CommentForm()
        return render(request, 'reviews/create_comment.template.html', {
            "form": form,
            "review": review
        })
