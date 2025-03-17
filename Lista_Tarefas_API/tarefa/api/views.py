from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import UsuarioSerializer
from rest_framework.permissions import  AllowAny

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