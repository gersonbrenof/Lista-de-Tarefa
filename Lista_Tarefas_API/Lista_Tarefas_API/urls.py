
from django.contrib import admin
from django.urls import path, include,re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from tarefa.api.views import TarefaViewSet
schema_view = get_schema_view(
    openapi.Info(
        title="LIsta de Tarefa",
        default_version="v1",
        description="Documentação da API Lsita de Tarefa",
        terms_of_service="https://www.seusite.com/termos/",
        contact=openapi.Contact(email="suporte@seusite.com"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'Tarefas', TarefaViewSet , basename="Tarefas")
urlpatterns = [
    path('admin/', admin.site.urls),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('', include('tarefa.urls')),
     path('api/', include(router.urls)),
]
