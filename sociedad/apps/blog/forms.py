from django.forms import ModelForm
from django import forms
from .models import *


#class entradaform(ModelForm):
#	class Meta:
#		model = entrada

#RATING_CHOICES = ((1,1),(2,2),(3,3),(4,4),(5,5),)
#forms.CharField(widget=forms.RadioSelect(renderee = StarsRadioFieldRenderer, attrs = {'class'.'star'},choices = RATING_CHOICES))

#=========================  FORMULARIOS =====================================#

class FormularioComentario(ModelForm):
    class Meta:
        model = Comentar
        exclude = ["requerir"]

class FormularioEntrada(ModelForm):
    class Meta:
        model = entrada
#========================  END - FORTMULARIOS ================================#