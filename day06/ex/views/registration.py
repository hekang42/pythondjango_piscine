from django.views.generic import FormView
from django.contrib.auth import login
from django.contrib import messages
from django.urls import reverse_lazy
from ..forms.newuserform import NewUserForm
from django.shortcuts import redirect


class Registration(FormView):
    template_name = "registration.html"
    form_class = NewUserForm
    success_url = reverse_lazy('index')
    def get(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return (redirect('index'))
        return super().get(request, *args, **kwargs)
     
    def form_valid(self, form: NewUserForm):
        user = form.save()
        login(self.request, user)
        messages.success(self.request, "Registration successful.")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(
            self.request, "Unsuccessful registration. Invalid information.")
        return super().form_invalid(form)