# views.py
from django.views.generic import ListView
from low.models.models import Article
from django.core.paginator import Paginator
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
class ArticleListView(LoginRequiredMixin, ListView):
    model = Article
    # context_object_name = 'article_list.html'
    template_name = 'article_list.html'
    paginate_by = 10
    queryset = Article.objects.all().order_by('-created')
    login_url = reverse_lazy('login')
