from django.contrib import admin

from.models import Post,Author,Tag

# Helps to create few filters in the admin panel
class PostAdmin(admin.ModelAdmin):
    list_filters = ("author", "tags", "date")
    list_display = ("title", "author", "date")
    prepopulated_fields = {"slug": ("title",)}
    
# Register your models here.

admin.site.register(Post, PostAdmin)
admin.site.register(Author) 
admin.site.register(Tag)