from ..models.models import Comment
from django import forms

class CommentForm(forms.Form):
    model = Comment
    content = forms.CharField(required=True)