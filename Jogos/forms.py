from django import forms
from .models import Usuario, Desenvolvedor,Distribuidora

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = '__all__'

class DesenvolvedorForm(forms.ModelForm):
    class Meta:
        model = Desenvolvedor
        fields = '__all__'
        
class DistribuidoraForm(forms.ModelForm):
    class Meta:
        model = Distribuidora
        fields = '__all__'
        
