# when the request reaches url has to be called ,
# path fuctions takes two arguments ones the url as a string second argument 
# should be function name which is to be called when the url is requested

from django.urls import path     
from.import views

urlpatterns = [
    path("blogs", views.blogs)  
]

# created url config for app1 

# myproject1.com/app1/blogs 
# If a request to django /blogs execute the blog view function from views.py file
