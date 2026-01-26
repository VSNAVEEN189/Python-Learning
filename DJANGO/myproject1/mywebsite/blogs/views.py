from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
# Create your views here.

# Making the code more dynamically using dictionary, We can keep on adding more blocks.
blog_names = {
    "python-intro": "<h1>Python Post</h1>",
    "django-basics": "<h1>Django basics blog posts</h1>",
    "python-oops": "<h1>Object Oriented Programming with python</h1>",
    "regx": "<h1>Regular Expressions in Python</h1>"
}

def home_page(request):
    return HttpResponse("<h1>Home Page of our Blogs</h1>")

def blogpost(request):
    return HttpResponse("<h1>All blog posts!</h1>")

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
    # if blog == "python-intro":
    #     res = "<h1>Python Post</h1>"
    # elif blog == "django-basics":
    #     res = "<h1>Django basics blog posts</h1>"
    # elif blog == "python-oops":
    #     res = "<h1>Object Oriented Programming with python</h1>"  
    # else:
    try:        #To avoiding the error if blog not found in dictionary
        res = blog_names[blog]
    except:    
       return HttpResponseNotFound("<h1>Blog not found</h1>")
    else:
       return HttpResponseNotFound(res)





# def blog_post_by_number(request, blog):
#     return HttpResponse(blog)
