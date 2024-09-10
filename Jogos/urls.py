from django.urls import path
from . import views


from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import JogoViewSet, DesenvolvedorViewSet,DistribuidoraViewSet,UsuarioViewSet
from . import views

router = DefaultRouter()
router.register(r'Jogos', JogoViewSet)
router.register(r'Desenvolvedor',DesenvolvedorViewSet)
router.register(r'Distribuidora', DistribuidoraViewSet)
router.register(r'Usuario',UsuarioViewSet )


urlpatterns = [
    path('', include(router.urls)),
    path('escolha/', views.escolha_usuario, name='escolha'),
    
    path('usuario/', views.usuario_view, name='usuario'),  # Rota para o formulário de usuario
    
    path('desenvolvedor/', views.desenvolvedor_view, name ='desenvolvedor'),
    
    path('distribuidora/', views.distribuidora_view, name ='Distribuidora'),
    
    path('usuario/success/', views.usuario_success, 
    name='usuario_success'), # Pagina de successo de usuario
    
    path('desenvolvedor/success/', views.desenvolvedor_success, name='desenvolvedor_success'), #pagina de successo de desenvolvedor
    
    path('distribuidora/success/', views.distribuidora_success, name='distribuidora_success'), #pagina 
]