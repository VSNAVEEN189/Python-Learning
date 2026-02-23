from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)  #Shows when the post was created
    updated_at = models.DateTimeField(auto_now=True)      #Shows when the post was last updated
     
    def __str__(self):
        return self.title
    