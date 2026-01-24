from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def blogpost(request):
    return HttpResponse("All blog posts!")

