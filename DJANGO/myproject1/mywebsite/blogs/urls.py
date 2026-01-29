from django.urls import path
from .import views
# We have to keep on adding urls here for every view we create in views.py of blogs app
urlpatterns = [
    path("", views.home_page),                           #Home page for blogs app  http:// and indidvidual urls also
    path("allposts", views.blogpost),
    # path("allposts/python-intro", views.python_intro),   #http://127.0.0.1:8000/blogs/allposts/python-intro
    # path("allposts/django-basics", views.django_basic),  #http://127.0.0.1:8000/blogs/allposts/django-basics
    # path("allposts/python-oops", views.python_oops),
    # Dynamic path segment to handle multiple urls with single view function
    # path("allposts/blog", views.blog_post),                #It tells django to handle any url after allposts/anything url
    # path("allposts/<int:blog>", views.blog_post_by_number),   #It tells django to convert the given value to integer.
    # path("allposts/<str:blog>", views.blog_post)            #It tells django to convert the given value to string.
    path("allposts/<str:blog>", views.blog_post, name="blog-post")            #It tells django to convert the given value to slug.
]    
