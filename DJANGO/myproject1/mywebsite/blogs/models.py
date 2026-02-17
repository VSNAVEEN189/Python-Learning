from django.db import models

# Create your models here.
# Which will interacrt with the database, we can create tables in the database using models.

class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()

# User defined method to get full name of the author, it is not a built-in method of django, we have to define it ourselves.
    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"
    
    def __str__(self):
        return self.get_full_name()
    


class Tag(models.Model):
    caption = models.CharField(max_length=20)
    # To get the full string representation of the tag name.
    def __str__(self):
        return self.caption
               


class Post(models.Model):
    title = models.CharField(max_length=200)
    preview = models.CharField(max_length=200)
    content = models.TextField()
    date = models.DateTimeField(auto_now=True) 
    slug = models.SlugField(unique=True)
    image = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True) #ForeignKey is used to create a relationship between two tables. It is used to create a one-to-many relationship. In this case, one author can have many posts.
    tags = models.ManyToManyField(Tag)        #ManyToManyField is used to create a many-to-many relationship. In this case, one post can have many tags and one tag can be associated with many posts.
    
