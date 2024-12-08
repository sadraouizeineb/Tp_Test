from django import forms
from .models import Livre

class LivreForm(forms.ModelForm):
    class Meta:
        model = Livre
        fields = ['titre', 'auteur', 'date_publication', 'disponible']
        widgets = {
            'titre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Titre du livre'}),
            'auteur': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Auteur'}),
            'date_publication': forms.DateInput(attrs={'type': 'date',  'class': 'form-control', }),
            'disponible': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
