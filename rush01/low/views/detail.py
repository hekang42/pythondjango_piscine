from django.views.generic import DetailView, FormView
from ..models.models import Article,Comment
from typing import Any
from django import http
from django.http.response import HttpResponseBase
from ..forms.favourite import FavouriteForm
from ..forms.comment import CommentForm
from django.views.generic import DetailView
from django.urls import reverse_lazy, reverse
from django.db import DatabaseError
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin


class Detail(DetailView, FormView):
    template_name = "detail.html"
    form_class = CommentForm
    model = Article
    pk_url_kwarg = 'article_id'
    def get_success_url(self): 
        return reverse('detail', args=[self.kwargs.get(self.pk_url_kwarg)])
        # return reverse('detail', kwargs={'pk': self.kwargs.get(self.pk_url_kwarg)})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        article = context['object']
        context["favouriteForm"] = FavouriteForm(article.id)
        context["comment_form"] = CommentForm
        return context

    def form_valid(self, form:CommentForm):
        content = form.cleaned_data['content']
        try:
            Comment.objects.create(
                content=content,
                author=self.request.user,
                article_id=self.kwargs.get(self.pk_url_kwarg)
                # 아티클 아이디 갖고오기. 개쩔어ㅓ
            )
        except DatabaseError as e:
            messages.error(
                self.request, "Unsuccessful comment. DatabaseError")
            messages.error(self.request,e)
            return redirect('index')
        messages.success(self.request, "Successful comment.")
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.error(
            self.request, "Unsuccessful Comment. Invalid information.")
        return super().form_invalid(form)