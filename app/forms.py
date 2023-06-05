from django.forms import inlineformset_factory
from .models import MyModel, MyFile
from django import forms

class MyFileForm(forms.ModelForm):
    class Meta:
        model = MyFile
        fields = ['file']


MyFileFormSet = inlineformset_factory(MyModel, MyFile, form=MyFileForm, extra=1, can_delete=True)