from django.contrib import admin

from.models import Post,Author,Tag,Comment

# Helps to create few filters in the admin panel
class PostAdmin(admin.ModelAdmin):
    list_filters = ("author", "tags", "date")
    list_display = ("title", "author", "date")
    prepopulated_fields = {"slug": ("title",)}

class CommentAdmin(admin.ModelAdmin):
    # list_filters = ("post", "user_name", "user_email")
    list_display = ("user_name", "post") 

    
# Register your models here.

admin.site.register(Post, PostAdmin)
admin.site.register(Author) 
admin.site.register(Tag)
admin.site.register(Comment, CommentAdmin)