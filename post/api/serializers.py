from rest_framework import serializers

from post.models import Tag, Category, Post


class TagSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Tag
        fields = 'all'


class CategorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Category
        fields = 'all'


class PostSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Post
        fields = 'all'