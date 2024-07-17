from django.contrib.auth.models import AbstractUser, BaseUserManager, Group
from django.db import models
from .loja import Loja

class CustomUserManager(BaseUserManager):
    """
    Gerenciador personalizado para o modelo Usuario.
    """
    def create_user(self, login, password=None, **extra_fields):
        """
        Cria e salva um usuário com o username e senha fornecidos.
        """
        if not login:
            raise ValueError(('O campo username é obrigatório.'))
        
        user = self.model(login=login, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, usr_login, password=None, **extra_fields):
        """
        Cria e salva um superusuário com o username e senha fornecidos.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(usr_login, password, **extra_fields)

class Usuario(AbstractUser):
    dep_codigo = models.ForeignKey(Group, on_delete=models.SET_NULL, null=True, blank=True)
    loj_codigo = models.ForeignKey(Loja, on_delete=models.SET_NULL, null=True, blank=True)
    ven_codigo = models.IntegerField(null=True, blank=True)
    usr_cpf = models.CharField(max_length=20, null=True, blank=True)
    usr_datanascimento = models.DateTimeField(null=True, blank=True)
    
    # objects = CustomUserManager()
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.username