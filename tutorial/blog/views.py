# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import Category, Post, Comment
from .serializers import CategorySerializer, CommentSerializer, PostSerializer
from rest_framework.viewsets import ModelViewSet


# Create your views here.
class CategoryView(ModelViewSet):
	queryset = Category.objects.all()
	serializer_class = CategorySerializer


class CommentView(ModelViewSet):
	queryset = Comment.objects.all()
	serializer_class = CommentSerializer


class PostView(ModelViewSet):
	queryset = Post.objects.all()
	serializer_class = PostSerializer