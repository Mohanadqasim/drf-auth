from django.shortcuts import render
from rest_framework import generics
from .models import Movie,Post
from .serializers import MovieSerializer,PostSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated
from .permissions import IsOwnerOrReadOnly

# Create your views here.
class MoviesList(generics.ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = [IsAuthenticated]

class MoviesDetail(generics.RetrieveUpdateDestroyAPIView): #RetrieveAPIView, RetrieveUpdateAPIView
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = [IsOwnerOrReadOnly]

class PostsList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [AllowAny]

class PostsDetail(generics.RetrieveUpdateDestroyAPIView): #RetrieveAPIView, RetrieveUpdateAPIView
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [AllowAny]