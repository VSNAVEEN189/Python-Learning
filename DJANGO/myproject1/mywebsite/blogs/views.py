from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
# Create your views here.


def home_page(request):
    return HttpResponse("Home Page of our Blogs")

def blogpost(request):
    return HttpResponse("All blog posts!")

# def python_intro(request):
#     return HttpResponse("Python Post of our Blogs")

# def django_basic(request):
#     return HttpResponse("Django basics blog posts")

# def python_oops(request):
#     return HttpResponse("Object Oriented Programming with python")

# Blogpost views will be called for every blog there , In future to support more blogs by adding more elif conditions.
# Used to capture the blog parameter 
# Same identifier as used in urls.py should be used in the view function parameter
def blog_post(request, blog):
    if blog == "python-intro":
        res = "Python Post"
    elif blog == "django-basics":
        res = "Django basics blog posts"
    elif blog == "python-oops":
        res = "Object Oriented Programming with python"  
    else:
        return HttpResponseNotFound("Blog not found")
    return HttpResponse(res)


def blog_post_by_number(request, blog):
    return HttpResponse(blog)
