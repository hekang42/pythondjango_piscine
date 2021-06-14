from django.views.generic import FormView
from ..models.models import Article,Comment,ReComment
from ..forms.comment import CommentForm
from django.contrib import messages
from django.urls import reverse_lazy, reverse
from django.shortcuts import redirect

class Recomment(FormView):
    template_name = "detail.html"
    form_class = CommentForm
    model = Comment
    pk_url_kwarg = 'comment_id'

    def get_success_url(self):
        return reverse('detail', args=[self.kwargs.get('article_id')])

    def form_valid(self, form:CommentForm):
        content = form.cleaned_data['content']
        try:
            parent= Comment.objects.get(pk=self.kwargs.get(self.pk_url_kwarg))
        except Comment.DoesNotExist:
            messages.error(
                self.request, "Unsuccessful comment. Nothing Comment")
            return redirect('index')
        try:
            ReComment.objects.create(
                content=content,
                author=self.request.user,
                comment_id=parent
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
        return redirect('detail', self.kwargs.get('article_id'))