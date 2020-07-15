from django.shortcuts import render, HttpResponse


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
