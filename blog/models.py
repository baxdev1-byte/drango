from django.db import models

class Post(models.Model):
    #img
    #author
    title = models.CharField(max_length=100)
    content = models.TextField()
    #tag
    #categorie
    counted_views = models.IntegerField(default=0)
    status = models.BooleanField(default=False)
    published_date = models.DateTimeField(null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.title}: {self.content[:25]}'
