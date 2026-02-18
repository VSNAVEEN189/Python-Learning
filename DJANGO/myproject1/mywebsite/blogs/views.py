from django.shortcuts import render
from django.http import Http404, HttpResponseNotFound
from .models import Post    #importing the post model to get the blog details.
from .forms import CommentForm  #importing the comment form to get the comment details from the user.

def home_page(request):
    latest_blogs = Post.objects.all().order_by("-date")[:2]
    return render(request, "blogs/index.html", {"l_blogs": latest_blogs})  #Directly rendering html template without loading it first.
    
   
# For all post page.
def blogpost(request):
    blog_details = Post.objects.all()  #Getting all the blog details from the database using the post model.
    return render(request, "blogs/allposts.html", {"blogs": blog_details})
    #We remove blog list and use blog_details list of dictionary to get all the details of blogs in one go and pass it to template directly


# For individual blog post page.
def blog_post(request, blog):
    try:                              #To avoiding the error if blog not found in dictionary
        post_data = Post.objects.get(slug=blog)  #Gets one query only 
        tag_caption = post_data.tags.all()  #To get all the tags associated with the blog post.
        form_data = CommentForm()  #To create an instance of the comment form to display it in the template.
        return render(request, "blogs/posts.html", {
            "post": post_data, "tags": tag_caption, "comment_form": form_data})  #Rendering the template for blog post
    except Exception:  
        raise Http404()
