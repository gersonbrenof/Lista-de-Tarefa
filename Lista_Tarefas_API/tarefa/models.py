from django.db import models
from django.contrib.auth.models import User

class Usuario(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    nome_usuario = models.CharField(max_length=100, blank=True, null=True)
    
    def save(self , *args, **kwargs):
        if not self.usuario.username:
            self.usuario.username = self.email
            self.usuario.save()
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.nome_usuario
    
    
class Tarefa(models.Model):
    STATUS_CHOICES = (
        ('P', 'Pendente'),
        ('F', 'Finalizada'),
        ('R', 'Replanejada'),
    )
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    Titulo_Tarefa = models.CharField(max_length=100, blank=False, null=False)
    descricao = models.TextField(blank= False, null=False)
    data_croacao = models.DateField(auto_now_add=True)
    data_limite = models.DateField(blank=True, null=True)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='P')
    
    def __str__(self):
        return self.Titulo_Tarefa