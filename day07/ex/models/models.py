# models.py
from django.db import models
from django.contrib.auth.models import User

class Article(models.Model) :
    title = models.CharField(max_length=64, null=False)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE, null=False)
    created = models.DateTimeField(auto_now=True, auto_now_add=False)
    synopsis = models.CharField(max_length=312, null=False)
    content = models.TextField(null=False)

    def __str__(self):
        return self.title

class UserFavouriteArticle(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE, null=False)
    article = models.ForeignKey(
        Article,
        on_delete=models.CASCADE, null=False)
    
    def __str__(self):
        return self.article.title


    # class Meta:
    #     ordering = ["-name"]
