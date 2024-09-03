from django.shortcuts import render, redirect
from .forms import UsuarioForm
from rest_framework import viewsets
from .models import Jogo, Desenvolvedor , Distribuidora , Usuario
from .serializers import JogoSerializer, DesenvolvedorSerializer , DistribuidoraSerializer, UsuarioSerializer

#usado para criação de API
class JogoViewSet(viewsets.ModelViewSet):
    queryset = Jogo.objects.all()
    serializer_class = JogoSerializer
        
class DesenvolvedorViewSet(viewsets.ModelViewSet):
    queryset =  Desenvolvedor.objects.all()
    serializer_class = DesenvolvedorSerializer
    
class DistribuidoraViewSet(viewsets.ModelViewSet):
    queryset = Distribuidora.objects.all()
    serializer_class = DistribuidoraSerializer
    
class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    

def usuario_view(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('usuario_success')
         
    else:
        form = UsuarioForm()
    return render(request, 'Jogos/usuario_Forms.html', {'form': form})
    
    
def usuario_success(request):
    return render(request, 'Jogos/usuario_success.html')
    

