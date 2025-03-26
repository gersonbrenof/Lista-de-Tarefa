
from django.contrib import admin
from django.urls import path, include,re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from tarefa.api.views import TarefaViewSet
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'Tarefas', TarefaViewSet , basename="Tarefas")
urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),  
    
    # Swagger UI
    path("api/swagger/", SpectacularSwaggerView.as_view(url_name="schema"), name="swagger-ui"),
    path('', include('tarefa.urls')),
     path('api/', include(router.urls)),
]
