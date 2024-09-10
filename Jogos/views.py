from django.shortcuts import render, redirect
from .forms import UsuarioForm, DesenvolvedorForm, DistribuidoraForm
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
        form = UsuarioForm()  # Inicializa o formulário vazio para GET requests
    
    return render(request, 'Jogos/usuario_Forms.html', {'form': form})

def desenvolvedor_view(request):
    if request.method == 'POST':
        form = DesenvolvedorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('desenvolvedor_success')
    else:
        form = DesenvolvedorForm()
    
    return render(request, 'Jogos/desenvolvedor_forms.html', {'form': form} )
  
 
def distribuidora_view(request):
    if request.method == 'POST':
        form = DistribuidoraForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('distribuidora_success')
    else:
        form = DistribuidoraForm()
        
    return render(request, 'Jogos/distribuidora_forms.html', {'form': form})


def usuario_success(request):
    return render(request, 'Jogos/usuario_success.html')

def desenvolvedor_success(request):
    return render(request, 'Jogos/desenvolvedor_success.html')

def distribuidora_success(request):
    return render(request, 'Jogos/distribuidora_success.html')

    
    #criação de uma pagina html com 3 botão para redirecionar o usuario para sua pagina de cadastro
def escolha_usuario(request):
    return render(request, 'Jogos/escolha_usuario.html')
