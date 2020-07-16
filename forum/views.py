from django.shortcuts import render


# Create your views here.
def forum_home(request):
    return render(request, "forum/home.template.html")
