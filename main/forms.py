from django import forms
from main.models import Part

class PartForm(forms.ModelForm):
    class Meta:
        model = Part
        fields = ('name', 'content',)

class DeletePartForm(forms.ModelForm):
    class Meta:
        model = Part
        fields = ()