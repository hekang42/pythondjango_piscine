from django import forms
from django.forms.widgets import Textarea
from ..models.models import Profile


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ("name", "surname", "email", "description", "picture")


    	