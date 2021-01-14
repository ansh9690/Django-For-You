from django.db import models
from django.contrib.auth.models import User
from django.forms import ModelForm
from django.utils import timezone
from django.shortcuts import reverse


class Post(models.Model):
    author = models.CharField(max_length=100)
    title = models.CharField(max_length=150)
    body = models.TextField()
    read_time = models.CharField(max_length=10)
    author_name = models.ForeignKey(User, default=None, on_delete=models.CASCADE)
    timeStamp = models.DateField(default=timezone.now)
    likes = models.ManyToManyField(User, related_name='blog_posts')

    def __str__(self):
        return self.title[0:20]
    
    def get_absolute_url(self):
        return reverse("home:post_detail", kwargs={
            'pk': self.id
        })
    
    def post_total_likes(self):
        return self.likes.count()



class BlogComment(models.Model):
    body = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name='comments')

    def __str__(self):
        return self.body[0:15] + "..." + "by " + self.user.username
    
    def comment_total_likes(self):
        return self.likes.count()



class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    body = models.TextField()
    timeStamp = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return f'Message from {self.name} - {self.email}'
    
class Subscriber(models.Model):
    email = models.CharField(max_length=50)
    
    def __str__(self):
        return self.email
    