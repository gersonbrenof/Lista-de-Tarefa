from django.contrib import admin
from django.urls import path, include
from tarefa.api.views import RegistrarUsuarioView
urlpatterns = [
   path('api/cadastrar/', RegistrarUsuarioView.as_view(), name='cadastrar'),
]
