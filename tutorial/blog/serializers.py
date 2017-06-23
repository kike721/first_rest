from blog.models import Category, Post, Comment
from rest_framework import serializers


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = Category
        fields = ('url', 'name')


class PostSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = Post
        fields = ('url', 'author', 'category', 'title', 'content')


class CommentSerializer(serializers.HyperlinkedModelSerializer):

	class Meta:
		model = Comment
		fields = ('url', 'post', 'author', 'content')