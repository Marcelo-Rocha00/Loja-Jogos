from rest_framework import serializers
from .models import Jogo, Desenvolvedor , Distribuidora , Usuario

class JogoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Jogo
        fields = '__all__'
        
class DesenvolvedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Desenvolvedor
        fields = '__all__'
    
class DistribuidoraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Distribuidora
        fields = '__all__'
        
class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'