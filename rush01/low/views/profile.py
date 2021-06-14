from django.http import request
from ..models import models
from typing import Any
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import DatabaseError
from django.shortcuts import redirect
from ..forms.profile import ProfileForm
from django.views.generic import FormView,DetailView
from django.contrib.auth import login
from django.contrib import messages
from django.urls import reverse_lazy


class Profile(LoginRequiredMixin, FormView):
    template_name = "profile.html"
    form_class = ProfileForm
    success_url = reverse_lazy('profile')

    def get_initial(self):
        user = models.Profile.objects.get(user_id=self.request.user.id)
        self.initial = {
            "name": user.name,
            "surname": user.surname,
            "email": user.email,
            "description": user.description,
            "picture": user.picture,
        }
        return self.initial.copy()
    def form_valid(self, form):
        profile = form.save(commit=False)
        profile.user_id = self.request.user.id
        profile.save()
        return super().form_valid(form)

    # def form_valid(self, form: ProfileForm):
    #     name = form.cleaned_data['name']
    #     surname = form.cleaned_data['surname']
    #     email = form.cleaned_data['email']
    #     description = form.cleaned_data['description']
    #     picture = form.cleaned_data['picture']
    #     try:
    #         models.Profile.objects.create(
    #             user=self.request.user,
    #             name=name,
    #             surname=surname,
    #             email=email,./m
    #             description=description,
    #             picture=picture
    #         )
            
    #     except DatabaseError as e:
    #         messages.success(
    #             self.request, "Unsuccessful make profile. DatabaseError")
    #         return redirect('index')
    #     messages.success(self.request, "Successful make profile.")
    #     return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(
            self.request, "Unsuccessful profile. Invalid information.")
        return super().form_invalid(form)