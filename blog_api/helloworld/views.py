from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet   #Posting api 
from helloworld.serializers import PostSerializer
from helloworld.models import Post
# Create your views here.

class HelloWorldView(APIView):

    def get(self, request):
        return Response({"message": "Hello, World!"})
    # Posting api
class PostView(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
