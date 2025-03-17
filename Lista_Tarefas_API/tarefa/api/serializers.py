from rest_framework import serializers
from django.contrib.auth.models import User
from tarefa.models import Usuario

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
            