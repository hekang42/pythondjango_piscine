# views.py
from django.views.generic import ListView
from ..models.models import Article 
from django.contrib.auth.mixins import LoginRequiredMixin

class Publications(LoginRequiredMixin, ListView):
    model = Article
    # context_object_name = 'article_list.html'
    template_name = 'article_list.html'

    def get_queryset(self):
        print(self.request.user)
        return Article.objects.all().filter(author=self.request.user).order_by('-created')
    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context