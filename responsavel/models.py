from django.db import models
from django.contrib.auth.models import AbstractUser

class Usuario(AbstractUser):

    class Meta:
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'
        app_label = "responsavel"

class Responsavel(Usuario):

    class Meta:
        verbose_name = 'Responsável'
        verbose_name_plural = 'Responsáveis'
        app_label = "responsavel"

    cpf = models.CharField(max_length=20)
    endereco = models.CharField(max_length=200)
    celular = models.CharField(max_length=12)

    def save(self, *args, **kwargs):
        self.is_staff = True
        if not self.username or self.username == "":
        	self.username = self.email.split("@")[0]
        super(Responsavel, self).save()


