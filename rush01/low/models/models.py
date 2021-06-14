# models.py
from django.db import models
from django.contrib.auth.models import User
# from ..forms.comment import CommentForm

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

class Comment(models.Model):
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE, null=False)
    content = models.TextField('reple')
    create_date = models.DateTimeField(auto_now=True)
    article = models.ForeignKey(Article, null=True, blank=True, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.content

class ReComment(models.Model):
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE, null=False)
    content = models.TextField()
    create_date = models.DateTimeField(auto_now=True)
    comment_id = models.ForeignKey(Comment, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.content

    def get_replay(self):
        from ex.forms.comment import CommentForm
        form = CommentForm()
        form.feilds['id'] = self.id
        return form

class Profile(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE, null=False, primary_key=True)
    name = models.CharField(max_length=64, null=False)
    surname = models.CharField(max_length=64, null=False)
    email = models.EmailField(null=False)
    description = models.TextField(null=False)
    picture = models.ImageField(blank=True, upload_to="images", null=True)
