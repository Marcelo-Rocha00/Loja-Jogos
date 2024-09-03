from django.urls import path
from . import views


urlpatterns = [
    path('usuario/', views.usuario_view, name='usuario'),  # Rota para o formulário
    path('usuario/success/', views.usuario_success, name='usuario_success'),  # Rota para página de sucesso
]