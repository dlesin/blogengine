# -*- coding: utf-8 -*-

from django.db import models
# from django.db.models.signals import pre_save
# from django.conf import settings
# from django.utils.text import slugify
from django.contrib.auth import get_user_model
from django.shortcuts import reverse
# from transliterate import translit
from tinymce.models import HTMLField

User = get_user_model()


def image_folder(instance, filename):
    filename = instance.slug + '.' + filename.split('.')[1]
    return "{0}/{1}".format(instance.slug, filename)


class Author(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    profile_picture = models.ImageField()

    def __str__(self):
        return f"{self.id} - {self.user}"


class Category(models.Model):
    title = models.CharField(max_length=100)
    head_title = models.CharField(max_length=30, null=True)
    head_description = models.CharField(max_length=120, null=True)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('category_detail_url', kwargs={
            'slug': self.slug
        })


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    guest_user = models.CharField(max_length=30, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    post = models.ForeignKey(
        'Post', related_name='comments', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.post} | User - {self.user}"


class Post(models.Model):
    title = models.CharField(max_length=100)
    head_title = models.CharField(max_length=30)
    head_description = models.CharField(max_length=120)
    overview = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    content = HTMLField()
    comment_count = models.IntegerField(default=0)
    view_count = models.IntegerField(default=0)
    author = models.ForeignKey(
        Author, on_delete=models.CASCADE, null=True)
    thumbnail = models.ImageField(upload_to=image_folder)
    thumbnail_alt = models.CharField(max_length=30, null=True)
    categories = models.ManyToManyField(Category)
    featured = models.BooleanField(default=True)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail_url', kwargs={
            'slug': self.slug
        })


class Contact(models.Model):
    user = models.CharField(max_length=30, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    content = models.TextField()

    def __str__(self):
        return f"{self.user} - {self.content}"




