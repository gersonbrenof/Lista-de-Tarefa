from rest_framework import status
from rest_framework.response import Response
from rest_framework import viewsets
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import UsuarioSerializer, LoginSerializer, TarefaSerializer, Tarefa
from rest_framework.permissions import  AllowAny, IsAuthenticated
from rest_framework.exceptions import PermissionDenied
from rest_framework.decorators import action
from django.utils.timezone import now
from django.shortcuts import get_object_or_404

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
            raise PermissionDenied("Não é possivel deletar essa tarefa por favo deletar uma valida")
        
        instance.delete()
        return Response({'mesage': 'tarefa delatada com sucesso'},status=status.HTTP_204_NO_CONTENT )
    @action(detail=True, methods=['post'])
    def finalizer_tarefa(self, request,pk=None):
        usuario_logado = self.request.user.usuario
        tarefa = get_object_or_404(Tarefa, id=pk)
        if tarefa.status == 'F':
            return Response({'message:' 'Tarefa Ja foi Finalizada'},status=status.HTTP_400_BAD_REQUEST)
        elif tarefa.usuario != usuario_logado:
            raise PermissionDenied("Não é possivel finalizar essa tarefa por favor finalizar uma tarefa valida")
        tarefa.status = 'F'
        tarefa.data_limite = now()
        tarefa.save()
        return Response({
            'message':'Tarefa Finalizada com Sucesso',
            'Data Finalização': tarefa.data_limite}, status=status.HTTP_200_OK)
        