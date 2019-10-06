from django import forms
from .models import Coment

class Comentarios(forms.ModelForm):
    class Meta:
        model = Coment
        fields = ('nome','comentario')