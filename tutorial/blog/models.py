# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Category(models.Model):

	name = models.CharField(max_length=200)

	def __unicode__(self):
		return self.name


class Post(models.Model):

	author = models.ForeignKey(User, related_name='posts')
	category = models.ForeignKey(Category, related_name='categories')
	title = models.CharField(max_length=150)
	content = models.TextField()

	def __unicode__(self):
		return self.title


class Comment(models.Model):

	post = models.ForeignKey(Post, related_name='p_comments')
	author = models.ForeignKey(User, related_name='a_comments')
	content = models.TextField()

	def __unicode__(self):
		return self.author