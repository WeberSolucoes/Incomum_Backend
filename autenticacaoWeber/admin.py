from django.contrib import admin

from autenticacaoWeber.models.usuario import Usuario
from django.contrib.auth.admin import UserAdmin

# Register your models here.
class UsuarioAdmin(UserAdmin):
    model = Usuario
    list_display = ('email','first_name','last_name','is_staff','is_active')
admin.site.register(Usuario, UsuarioAdmin)