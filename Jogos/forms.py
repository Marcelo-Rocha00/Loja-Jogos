from django import forms
from .models import Usuario, Desenvolvedor,Jogo,Distribuidora

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = '__all__'

class Desenvolvedor(forms.ModelForm):
    class Meta:
        model = Desenvolvedor
        fields = '__all__'
        
class Distribuidora(forms.ModelForm):
    class Meta:
        model = Distribuidora
        fields = '__all__'
        
class Jogo(forms.ModelForm):
    class Meta:
        model = Jogo
        fields = '__all__'