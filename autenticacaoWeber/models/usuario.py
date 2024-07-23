from django.contrib.auth.models import AbstractUser, BaseUserManager, Group
from django.db import models
from incomum.models.loja import Loja

class CustomUserManager(BaseUserManager):
    """
    Gerenciador personalizado para o modelo Usuario.
    """
    def create_user(self, email, password=None, **extra_fields):
        """
        Cria e salva um usuário com o email e senha fornecidos.
        """
        if not email:
            raise ValueError(('O campo email é obrigatório.'))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        """
        Cria e salva um superusuário com o email e senha fornecidos.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(email, password, **extra_fields)

class Usuario(AbstractUser):
    username = models.CharField(max_length=150, blank=True, default="")
    dep_codigo = models.ForeignKey(Group, on_delete=models.SET_NULL, null=True, blank=True)
    loj_codigo = models.ForeignKey(Loja, on_delete=models.SET_NULL, null=True, blank=True)
    ven_codigo = models.IntegerField(null=True, blank=True)
    usr_cpf = models.CharField(max_length=20, null=True, blank=True)
    usr_datanascimento = models.DateTimeField(null=True, blank=True)
    email = models.EmailField(('email address'), unique=True)
    
    objects = CustomUserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email