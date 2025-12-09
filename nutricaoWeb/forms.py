from django import forms
from .models import Nutricionista

class NutricionistaForm(forms.ModelForm):
    senha = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Nutricionista
        fields = ['nome_completo', 'email', 'crn', 'especialidade', 'senha']
