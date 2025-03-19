from rest_framework import serializers
from django.contrib.auth.models import User
from tarefa.models import Usuario, Tarefa
from django.contrib.auth import authenticate
from rest_framework.exceptions import AuthenticationFailed
from rest_framework_simplejwt.tokens import RefreshToken
class UsuarioSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(write_only=True)
    class Meta:
        model = Usuario
        fields = ('id', 'nome_usuario','email',  'password')
        extra_kwargs = {'password': {'write_only': True}} 
        
    def create(self, validated_data):
        email = validated_data.pop('email')
        password = validated_data.pop('password')
            
            # cria o usuario no modelo do user
        user = User.objects.create_user(username=email, email=email, password=password)
            
        #cria o perfil do usuario no modelo do usuario que no caso vai cria o nome do usuario
            
        usuario = Usuario.objects.create(usuario=user, **validated_data)
            
        return usuario
class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(required=True)
    access = serializers.CharField(read_only=True)
    refresh = serializers.CharField(read_only=True)
    def validate(self, data):
        email = data.get('email')
        password = data.get('password')
        try:
           user = User.objects.get(email=email)
        except User.DoesNotExist:
           raise AuthenticationFailed('Credenciais inválidas')
       
        if not user.check_password(password):
            raise AuthenticationFailed('Credenciais inválidas')
        
        user = authenticate(username=user.username, password=password)
       
        if user is None or not user.is_active:
           raise AuthenticationFailed('Erro Crendencial invlaidados')
        # Gera tokens de acesso
        refresh = RefreshToken.for_user(user)
        return {
            'access': str(refresh.access_token),
            'refresh': str(refresh)
        }
        
class TarefaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tarefa
        fields = ['id', 'Titulo_Tarefa','descricao', 'data_limite','status', 'data_croacao' ]
        read_only_fields = ['usuario'] 
        