from django.urls import path
from . import views

urlpatterns = [
    path('inicio/', views.inicio, name='inicio'),
    path('teste1/', views.teste1, name='teste1'),
    path('teste2/', views.teste2, name='teste2'),
    path('testefinal/', views.testefinal, name='testefinal'),
    path('saibamais/', views.saibamais, name='saibamais'),
    path('avaliar/', views.avaliar_trilha, name='avaliar_trilha'),
]