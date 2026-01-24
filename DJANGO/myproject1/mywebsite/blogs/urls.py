from django.urls import path
from .views import blogpost

urlpatterns = [
    path('allposts/', blogpost)
]
