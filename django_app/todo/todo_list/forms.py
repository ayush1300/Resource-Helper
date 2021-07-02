from django import forms
from .models import List, ComponentList


class ListForm(forms.ModelForm):
    class Meta:
        model = List
        fields = ["item", "completed"]
