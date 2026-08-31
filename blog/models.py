from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Post(models.Model):
    img = models.ImageField(upload_to='blog/', default='blog/default.jpg')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts', null=True)
    title = models.CharField(max_length=100)
    content = models.TextField()
    category = models.ManyToManyField(Category, related_name='blog_posts')
    tag = models.ManyToManyField(Tag, related_name='blog_posts')
    counted_views = models.IntegerField(default=0)
    status = models.BooleanField(default=False)
    published_date = models.DateTimeField(null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.title}: {self.content[:25]}'

    def get_absolute_url(self):
        return reverse("blog:blog_details", kwargs={'pid':self.id})

class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    author = models.ForeignKey(User, related_name='comments' ,on_delete=models.CASCADE)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.TextField()
    approved = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.author}: {self.subject[:25]}'