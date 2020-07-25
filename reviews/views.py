from django.shortcuts import render, HttpResponse
from .forms import ReviewForm


# Create your views here.
def index(request):
    # return HttpResponse("Reviews")
    return render(request, 'reviews/index.template.html')


# three things to do for the "C" part of the CRUD
# 1. the view
# 2. the template
# 3. the url
def create_review(request):
    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Review is created")
        else:
            return HttpResponse("Form has error")
    else:
        form = ReviewForm()
        return render(request, 'reviews/create_review.template.html', {
            "form": form
        })
