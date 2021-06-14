from django import forms
class UpdateForm(forms.Form):
    titles = forms.ChoiceField(choices=(), required=True)
    texts = forms.CharField(required=True)
    def __init__(self, choices, *args, **kwargs):
        super(UpdateForm, self).__init__(*args, **kwargs)
        self.fields['titles'].choices = choices