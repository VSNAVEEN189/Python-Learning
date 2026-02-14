from datetime import date
from django.shortcuts import render
from django.template.loader import render_to_string
from django.http import Http404, HttpResponseNotFound
from django.urls import reverse
# Create your views here.

# Making the code more dynamically using dictionary, We can keep on adding more blocks.
# blog_names = {
#     "python-intro": "IntroPython Post",
#     "django-basics": "Django basics blog posts",
#     "python-oops": "Object Oriented Programming with python",
#     "regx": "Regular Expressions in Python",
#     "tkinter": None
# }

blog_details = [
    {
        "slug": "python-intro",
        "image": "Python.jpeg",
        "date": date(2025, 10, 15),
        "title": "Python Introduction",
        "preview": """"Python is an open-source, high-level programming language that is used widely.
        Applications of pyhton are software development, data science, AI & ML, etc""",
        "Content": #Will be used in individual blog post page
        """Python is a versatile, high-level programming language known for its simple, English-like syntax and interpreted nature, making it ideal for rapid development""",
    }
    ,
    {
        "slug": "django-basics",
        "image": "django.jpeg",
        "date": date(2025, 10, 20),
        "title": "Django Basics",
        "preview": """Django is a high-level Python web framework that encourages rapid development and clean, pragmatic design.
        It follows the model-template-views (MTV) architectural pattern.""",
        "Content":
        """Django is a high-level Python web framework that promotes rapid development and clean, pragmatic design. It follows the model-template-views (MTV) architectural pattern, which is a variation of the traditional MVC pattern.""",
    }
    ,
    {
        "slug": "python-oops",
        "image": "oops.png",
        "date": date(2024, 10, 16),
        "title": "Python OOPs",
        "preview": """Object-oriented programming (OOP) is a programming paradigm that uses objects and classes to structure code.
        Python supports OOP principles such as encapsulation, inheritance, and polymorphism.""",
        "Content":
        """Object-oriented programming (OOP) is a programming paradigm that uses objects and classes to structure code. Python supports OOP principles such as encapsulation, inheritance, and polymorphism.""",
    }
    ,
    {
        "slug": "regx",
        "image": "regex.jpeg",
        "date": date(2025, 10, 19),
        "title": "Regular Expressions in Python",
        "preview": """Regular expressions (regex) are a powerful tool for pattern matching and text manipulation in Python.
        The re module provides functions for working with regular expressions.""",
        "Content":
        """Regular expressions (regex) are a powerful tool for pattern matching and text manipulation in Python. The re module provides functions for working with regular expressions.""",
    }
]


def home_page(request):
    sorted_blogs= sorted(blog_details, key=lambda post:post["date"], reverse=True)  #Sorting the blogs based on date in descending order to get the latest blogs first.
    latest_blogs = sorted_blogs[:2]  #Getting the latest 2 blogs from the sorted list.
    return render(request, "blogs/index.html", {"l_blogs": latest_blogs})  #Directly rendering html template without loading it first.
   
   
    # res_data = render_to_string("blogs/index.html")   #Rendering html template
    # return HttpResponse(res_data)

def blogpost(request):
    list_item = ""
    # blog_list = list(blog_names.keys())   #Getting all the keys from dictionary in form of list.
    return render(request, "blogs/allposts.html", {"blogs": blog_details})
    #We remove blog list and use blog_details list of dictionary to get all the details of blogs in one go and pass it to template directly. 

    # for b in blog_list: 
    #     blog_path = reverse("blog-post", args=[b])  #Using reverse function to get the url of blog post dynamically
    #     list_item += f'<li><a href="{blog_path}">{b.capitalize()}</a></li>'

    # res_data = f'<ul>{list_item}</ul>'
    # # """
    # # <ul>
    # #   <li><a href="/blogs/allposts/python-intro">Python Intro</a></li>
    # #   <li><a href="/blogs/allposts/django-basics">Django Basics</a></li>
    # # </ul>
    # # """
    # return HttpResponse(res_data)

# def python_intro(request):
#     return HttpResponse("Python Post of our Blogs")

# def django_basic(request):
#     return HttpResponse("Django basics blog posts")

# def python_oops(request):
#     return HttpResponse("Object Oriented Programming with python")

def process_blog_name(blog):
    # "python-intro" = ["python", "intro"]  ==> "python intro" => "Python Intro"
    blog_list = blog.split("-")
    return " ".join(blog_list)



def get_blog_by_slug(blog_url):
    for blog in blog_details:
        if blog["slug"] == blog_url:
            return blog
    return None



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
    try:                              #To avoiding the error if blog not found in dictionary
        res = get_blog_by_slug(blog)  #Getting the blog details by slug from the list of dictionary
        return render(request, "blogs/posts.html", {
            "post": res})  #Rendering the template for blog post
            # "blog_text": res, "blog_name": process_blog_name(blog)})  #Rendering the template for blog post
    except Exception:  
        raise Http404()
    
    #    res_data = render_to_string("404.html")  #Rendering the 404 template if blog not found in dictionary directly
    #    return HttpResponseNotFound(res_data)
    
    # Straight forward we can use http404
        # raise Http404()  # Raising 404 error if blog not found in dictionary
    # else:
    #    return HttpResponseNotFound(res_data)





# def blog_post_by_number(request, blog):
#     return HttpResponse(blog)
