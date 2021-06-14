from django import forms
class RemoveForm(forms.Form):
    titles = forms.ChoiceField(choices=(), required=True)
    def __init__(self, choices, *args, **kwargs):
        super(RemoveForm, self).__init__(*args, **kwargs)
        self.fields['titles'].choices = choices