from django.shortcuts import render
from django.http import Http404, HttpResponseRedirect
from django.urls import reverse
from urllib3 import request
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


# For POST
def blog_post(request, blog):
    post_data = Post.objects.get(slug=blog)  #Gets one query only 
    tag_caption = post_data.tags.all() 
    all_comments = post_data.comments.all().order_by("-id")  #To get all the comments for the blog post, we can use the related name "comments" that we defined in the comment model to get all the comments for the blog post.
                                            #displaying comments in descending order of their id, so that the latest comment will be displayed first.
    if request.method == "POST":  
        commented_data = request.POST        #Fetching the user input
        form = CommentForm(commented_data)  #To create an instance of the comment form with the data submitted by the user.
        if form.is_valid():                 #To check if the form is valid or not, it will return true if the form is valid and false if the form is not valid.
            comment = form.save(commit=False)    #To save the form data to the database, it will create a new comment in the database with the data submitted by the user.
            comment.post = post_data      #Assigning the post to the comment
            comment.save()               #Saving the comment to the database
            return HttpResponseRedirect(reverse("blog-post", args=[blog]))  #To redirect the user to the same blog post page after submitting the comment, it will redirect the user to the url of the blog post page with the slug of the blog post as an argument.
        return render(request, "blogs/posts.html", {
            "post": post_data, "tags": tag_caption, "comment_form": form, "comments": all_comments})  #Rendering the template for blog post with the form data if the form is not valid.
    else:         #For GET
        try:                                         #To avoiding the error if blog not found in dictionary
            form_data = CommentForm()                #To create an instance of the comment form to display it in the template.
            return render(request, "blogs/posts.html", {
                 "post": post_data, "tags": tag_caption, "comment_form": form_data, "comments": all_comments})  #Rendering the template for blog post
        except Exception:  
            raise Http404()
