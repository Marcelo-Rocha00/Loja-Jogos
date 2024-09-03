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
    path('usuario/', views.usuario_view, name='usuario'),
    path('usuario/success/', views.usuario_success, name='usuario_success'),
]
