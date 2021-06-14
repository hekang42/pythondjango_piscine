from django.views.generic.base import RedirectView
from django.urls import reverse_lazy

class ArticleRedirectView(RedirectView):
    # url = 'http://127.0.0.1:8000/articles'
    url = reverse_lazy('articles')
    