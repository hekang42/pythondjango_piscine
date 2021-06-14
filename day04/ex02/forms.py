from django import forms

# from .models import 

class PersonForm(forms.Form):
    content = forms.CharField(label="text", required=True)
    # birth = forms.DateField(label='birth')
    # age = forms.IntegerField(label='age')