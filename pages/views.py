from django.http import HttpResponse
from django.shortcuts import render
from pprint import pprint
import struct



# Create your views here.


def home_view(request, *args, **kwargs):
    print(args, kwargs)
    print(request.user)
    print(request.path)
    # return HttpResponse("<h1>Hello World</h1>")  # string of HTML code
    return render(request, "home.html", {})


def contact_view(request,*args, **kwargs):
    # return HttpResponse("<h1>Contact Page</h1>")
    return render(request, "contact.html", {})


def about_view(request,*args, **kwargs):
    # return HttpResponse("<h1>About Page</h1>")
    my_context = {
        "my_text": "this is about us",
        "my_number": 123,
        "my_list": [123,432432,234,123,4]
    }
    return render(request, "about.html", my_context)


def social_view(request,*args, **kwargs):
    # return HttpResponse("<h1>Social Page</h1>")
    return render(request, "home.html", {})
