from django.urls import path
from . import views

urlpatterns = [
    path("aula/<int:aula_id>/", views.aularender, name="aularender"),
    path("admin/aula/nova/", views.cadastrar_aula, name="cadastrar_aula"),
    path("avaliacao-final/<int:aula_id>/", views.avaliacao_final, name="avaliacao_final"),
    path('admin/aula/nova/', views.cadastrar_aula, name='cadastrar_aula'),
]