from rest_framework import status
from rest_framework.response import Response
from rest_framework import viewsets
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import UsuarioSerializer, LoginSerializer, TarefaSerializer, Tarefa
from rest_framework.permissions import  AllowAny, IsAuthenticated
from rest_framework.exceptions import PermissionDenied

class RegistrarUsuarioView(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        serializer = UsuarioSerializer(data=request.data)
        
        if serializer.is_valid():
            usuario = serializer.save()
            
            # aqui gera o token de acesso
            
            refresh = RefreshToken.for_user(usuario.usuario)
            access_token = str(refresh.access_token)
            
            return Response({
                'message': 'Usuario Cadastrado com sucesso',
                'access': access_token,
                'refresh': str(refresh)
            }, status.HTTP_201_CREATED)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
    
    
class LoginView(APIView):
        permission_classes = [AllowAny]
        def post(self, request):
            serializer = LoginSerializer(data=request.data)
            if serializer.is_valid():
                return Response(serializer.validated_data, status.HTTP_200_OK)
            return Response(status.HTTP_401_UNAUTHORIZED)

class TarefaViewSet(viewsets.ModelViewSet):
   # queryset = Tarefa.objects.all()
    serializer_class = TarefaSerializer 
    permission_classes = [IsAuthenticated] 
    
    
    def get_objet(self):
        try:
            obj = super().get_object()
        except Tarefa.DoesNotExist:
            raise PermissionDenied("Não é possivel acessar essa tarefa por favo de acessar uma valida")
    
    def get_queryset(self):
        
        return Tarefa.objects.filter(usuario = self.request.user.usuario)
    
    def perform_create(self, serializer):
        """Salva a tarefa associando ao usuário logado"""
        
        serializer.save(usuario=self.request.user.usuario)  # Salva a ta
    
    def perform_destroy(self, instance):
        # pega o usuario logado
        usuario_logado = self.request.user.usuario
         # verificar se o usuario esat logado
        if instance.usuario != usuario_logado:
            raise PermissionDenied("Não é possivek deletar essa tarefa por favo deletar uma valida")
        
        instance.delete()
        