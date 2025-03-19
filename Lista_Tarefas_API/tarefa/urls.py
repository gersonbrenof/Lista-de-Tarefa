from django.contrib import admin
from django.urls import path, include
from tarefa.api.views import RegistrarUsuarioView, LoginView
urlpatterns = [
   path('api/cadastrar/', RegistrarUsuarioView.as_view(), name='cadastrar'),
   path('api/login/', LoginView
        .as_view(), name='login'),
]
