# views.py
from django.views.generic import ListView
from low.models.models import Article
from django.core.paginator import Paginator

class ArticleListView(ListView):
    model = Article
    # context_object_name = 'article_list.html'
    template_name = 'article_list.html'
    paginate_by = 10
    queryset = Article.objects.all().order_by('-created')

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context["object_list"] = Article.objects.all().order_by('-created')
    #     return context

