from . import views
from django.urls import path

urlpatterns = [
    path('', views.TiposResiduosView.as_view(), name='tipos_residuos'),
    path('cadastro-local-coleta/', views.CadastroLocalColetaView.as_view(), name='cadastro_local_coleta'),
    path('busca-local-coleta/', views.BuscaLocalColetaView.as_view(), name='busca_local_coleta'),
    path('orientacoes/', views.OrientacoesView.as_view(), name='orientacoes'),
    path('resultado-busca/', views.ResultadoBuscaViews, name='resultado_busca'),
]
