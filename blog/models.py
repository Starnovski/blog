from django.db import models
from django.utils import timezone


class Category(models.Model):
    name = models.CharField(max_length=50)
    desc = models.TextField()

    def __str__(self):
        return self.name


class Post(models.Model):
    category = models.ForeignKey(Category, related_name= 'posts', on_delete= models.CASCADE)
    title = models.CharField(max_length=255)
    text = models.TextField()
    created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post, related_name = 'comments', on_delete = models.CASCADE,)
    author = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    body = models.TextField()
    created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title
