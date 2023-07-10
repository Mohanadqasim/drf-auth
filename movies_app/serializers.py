from rest_framework import serializers
from .models import Movie,Post

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('id','owner','name','desc','created_at','updated_at')

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model=Post
        fields = ('title', 'desc')