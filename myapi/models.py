from django.db import models
from django.contrib.auth.models import User


class Person(models.Model):
    name  = models.CharField(max_length=50)
    age   = models.PositiveSmallIntegerField()
    email = models.EmailField()
    
    def __str__(self):
        return self.name


class Post(models.Model):
    author  = models.ForeignKey(User, on_delete=models.CASCADE, related_name='post')

    title   = models.CharField(max_length=100)
    slug    = models.SlugField(max_length=200)
    body    = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.author} - {self.title[:20]}"
    

class Comment(models.Model):
    user     = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comment')
    post     = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comment')

    body     = models.TextField()
    approved = models.BooleanField(default=False)
    created  = models.DateTimeField(auto_now_add=True)
            
    def __str__(self):
        return f"{self.user} - {self.post.title[:20]}"
    
