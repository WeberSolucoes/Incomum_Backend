# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Agencia(models.Model):
    age_codigo = models.AutoField(primary_key=True)
    age_descricao = models.CharField(max_length=70, blank=True, null=True)
    age_endereco = models.CharField(max_length=60, blank=True, null=True)
    age_numero = models.CharField(max_length=20, blank=True, null=True)
    age_bairro = models.CharField(max_length=35, blank=True, null=True)
    age_cep = models.IntegerField(blank=True, null=True)
    cid_codigo = models.IntegerField(blank=True, null=True)
    age_fone = models.CharField(max_length=20, blank=True, null=True)
    age_celular = models.CharField(max_length=20, blank=True, null=True)
    age_observacao = models.CharField(max_length=180, blank=True, null=True)
    age_dataatualizacao = models.DateTimeField(blank=True, null=True)
    age_datacadastro = models.DateTimeField(blank=True, null=True)
    ban_codigo = models.IntegerField(blank=True, null=True)
    age_agencia = models.CharField(max_length=5, blank=True, null=True)
    age_contacorrente = models.CharField(max_length=15, blank=True, null=True)
    age_complementar = models.CharField(max_length=1, blank=True, null=True)
    age_codigocontabil = models.IntegerField(blank=True, null=True)
    age_cnpj = models.CharField(max_length=20, blank=True, null=True)
    age_situacao = models.CharField(max_length=1, blank=True, null=True)
    age_comissao = models.FloatField(blank=True, null=True)
    age_over = models.FloatField(blank=True, null=True)
    par_codigo = models.IntegerField(blank=True, null=True)
    age_imagem = models.TextField(blank=True, null=True)  # This field type is a guess.
    age_descricaosite = models.CharField(max_length=70, blank=True, null=True)
    age_verificar = models.CharField(max_length=1, blank=True, null=True)
    age_inscricaomunicipal = models.CharField(max_length=20, blank=True, null=True)
    age_markup = models.FloatField(blank=True, null=True)
    aco_codigo = models.IntegerField(blank=True, null=True)
    age_markupliberado = models.FloatField(blank=True, null=True)
    age_codigoprincipal = models.IntegerField(blank=True, null=True)
    age_codigoimportacao = models.IntegerField(blank=True, null=True)
    age_razaosocial = models.CharField(max_length=80, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'agencia'


class Agente(models.Model):
    agt_codigo = models.AutoField(primary_key=True)
    age_codigo = models.CharField(max_length=255)
    agt_descricao = models.CharField(max_length=255)
    agt_cpf = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'agente'


class Areacomercial(models.Model):
    aco_codigo = models.AutoField(primary_key=True)
    aco_descricao = models.CharField(max_length=50, blank=True, null=True)
    aco_datacadastro = models.DateTimeField(blank=True, null=True)
    aco_situacao = models.IntegerField(blank=True, null=True)
    aco_rateio = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'areacomercial'


class AutenticacaoweberUsuario(models.Model):
    id = models.BigAutoField(primary_key=True)
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()
    username = models.CharField(max_length=150)
    usr_cpf = models.CharField(max_length=20, blank=True, null=True)
    usr_datanascimento = models.DateTimeField(blank=True, null=True)
    email = models.CharField(unique=True, max_length=254)
    ven_endereco = models.CharField(max_length=60, blank=True, null=True)
    ven_numero = models.CharField(max_length=15, blank=True, null=True)
    ven_bairro = models.CharField(max_length=30, blank=True, null=True)
    ven_cep = models.IntegerField(blank=True, null=True)
    cid_codigo = models.IntegerField(blank=True, null=True)
    ven_fone = models.CharField(max_length=17, blank=True, null=True)
    ven_celular = models.CharField(max_length=17, blank=True, null=True)
    ven_observacao = models.CharField(max_length=170, blank=True, null=True)
    dep_codigo = models.ForeignKey('AuthGroup', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'autenticacaoWeber_usuario'


class AutenticacaoweberUsuarioGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    usuario = models.ForeignKey(AutenticacaoweberUsuario, models.DO_NOTHING)
    group = models.ForeignKey('AuthGroup', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'autenticacaoWeber_usuario_groups'
        unique_together = (('usuario', 'group'),)


class AutenticacaoweberUsuarioUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    usuario = models.ForeignKey(AutenticacaoweberUsuario, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'autenticacaoWeber_usuario_user_permissions'
        unique_together = (('usuario', 'permission'),)


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()
    aco_codigo = models.IntegerField(blank=True, null=True)
    ven_codigo = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Faturamentosimplificado(models.Model):
    fim_codigo = models.IntegerField(primary_key=True)
    tur_codigo = models.IntegerField()
    loj_codigo = models.IntegerField()
    ven_codigo = models.IntegerField()
    age_codigo = models.IntegerField()
    fim_data = models.DateField()
    aco_codigo = models.IntegerField()
    fim_tipo = models.CharField(max_length=10)
    tur_numerovenda = models.CharField(max_length=20)
    fim_valorliquido = models.FloatField()
    fim_markup = models.FloatField()
    fim_valorinc = models.FloatField()
    fim_valorincajustado = models.FloatField()
    loj_descricao = models.CharField(max_length=10)
    aco_descricao = models.CharField(max_length=20)
    ven_descricao = models.CharField(max_length=40)
    age_descricao = models.CharField(max_length=40)
    fat_valorvendabruta = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'faturamentosimplificado'


class IncomumPermissao(models.Model):
    id = models.BigAutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'incomum_permissao'


class Loja(models.Model):
    loj_codigo = models.AutoField(primary_key=True)
    loj_descricao = models.CharField(max_length=50, blank=True, null=True)
    loj_responsavel = models.CharField(max_length=30, blank=True, null=True)
    loj_email = models.CharField(max_length=200, blank=True, null=True)
    loj_endereco = models.CharField(max_length=80, blank=True, null=True)
    loj_bairro = models.CharField(max_length=45, blank=True, null=True)
    cep_codigo = models.IntegerField(blank=True, null=True)
    cid_codigo = models.IntegerField(blank=True, null=True)
    loj_fone = models.CharField(max_length=20, blank=True, null=True)
    loj_fax = models.CharField(max_length=20, blank=True, null=True)
    loj_emailloja = models.CharField(max_length=50, blank=True, null=True)
    loj_homepage = models.CharField(max_length=50, blank=True, null=True)
    loj_emailfinanceiro = models.CharField(max_length=60, blank=True, null=True)
    loj_textorelatorio = models.CharField(max_length=40, blank=True, null=True)
    loj_cnpj = models.CharField(max_length=20, blank=True, null=True)
    loj_serie = models.IntegerField(blank=True, null=True)
    loj_codigoempresa = models.IntegerField(blank=True, null=True)
    loj_emailbloqueio = models.CharField(max_length=60, blank=True, null=True)
    loj_situacao = models.IntegerField(blank=True, null=True)
    loj_codigofinanceiro = models.IntegerField(blank=True, null=True)
    aco_codigo = models.IntegerField(blank=True, null=True)
    loj_vendacorte = models.IntegerField(blank=True, null=True)
    loj_contrato = models.IntegerField(blank=True, null=True)
    loj_cortevendedor = models.IntegerField(blank=True, null=True)
    nem_codigo = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'loja'


class Lojacomercial(models.Model):
    loj_codigo = models.IntegerField(primary_key=True)  # The composite primary key (loj_codigo, aco_codigo) found, that is not supported. The first column is selected.
    aco_codigo = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'lojacomercial'
        unique_together = (('loj_codigo', 'aco_codigo'),)


class Turisticosituacao(models.Model):
    tur_codigo = models.IntegerField(primary_key=True)
    tsi_codigo = models.IntegerField()
    tsi_datacadastro = models.DateField()
    usr_codigo = models.IntegerField()
    stu_codigo = models.IntegerField()
    tsi_observacao = models.CharField(max_length=90, blank=True, null=True)
    tsi_markup = models.FloatField(blank=True, null=True)
    tsi_valorcambio = models.FloatField(blank=True, null=True)
    tsi_comissao = models.FloatField(blank=True, null=True)
    tsi_valortaxa = models.FloatField(blank=True, null=True)
    tsi_taxaemissao = models.FloatField(blank=True, null=True)
    tsi_incentivo = models.FloatField(blank=True, null=True)
    tsi_valortarifa = models.FloatField(blank=True, null=True)
    tsi_valorliquido = models.FloatField(blank=True, null=True)
    tsi_valorinc = models.FloatField()
    tsi_valorbase = models.FloatField(blank=True, null=True)
    tsi_valorprejuizo = models.FloatField(blank=True, null=True)
    tsi_markupajustado = models.FloatField(blank=True, null=True)
    tsi_vendareal = models.FloatField(blank=True, null=True)
    tsi_comissaoreal = models.FloatField(blank=True, null=True)
    tsi_incentivoreal = models.FloatField(blank=True, null=True)
    tsi_arredondamentoreal = models.FloatField(blank=True, null=True)
    tsi_diferencacambioreal = models.FloatField(blank=True, null=True)
    tsi_diferencaavista = models.FloatField(blank=True, null=True)
    tsi_incajustado = models.FloatField(blank=True, null=True)
    tsi_diferencataxareal = models.FloatField(blank=True, null=True)
    tsi_percentualcomissao = models.FloatField(blank=True, null=True)
    tsi_percentualincentivo = models.FloatField(blank=True, null=True)
    tsi_cambiotaxareal = models.FloatField(blank=True, null=True)
    tsi_multaincomum = models.FloatField(blank=True, null=True)
    tsi_netoreembolso = models.FloatField(blank=True, null=True)
    tsi_taxareembolso = models.FloatField(blank=True, null=True)
    tsi_vendareembolso = models.FloatField(blank=True, null=True)
    tsi_comissaoreembolso = models.FloatField(blank=True, null=True)
    tsi_incentivoreembolso = models.FloatField(blank=True, null=True)
    tsi_custoajustado = models.FloatField(blank=True, null=True)
    tsi_valoroperacional = models.FloatField(blank=True, null=True)
    tsi_valornota = models.FloatField(blank=True, null=True)
    tsi_valornotaajustado = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'turisticosituacao'
        unique_together = (('tur_codigo', 'tsi_codigo'),)


class Usuariocomercial(models.Model):
    usr_codigo = models.OneToOneField(AuthUser, models.DO_NOTHING, db_column='usr_codigo', primary_key=True)  # The composite primary key (usr_codigo, aco_codigo) found, that is not supported. The first column is selected.
    aco_codigo = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'usuariocomercial'
        unique_together = (('usr_codigo', 'aco_codigo'),)


class Vendedor(models.Model):
    ven_codigo = models.IntegerField(primary_key=True)
    ven_descricao = models.CharField(max_length=60, blank=True, null=True)
    ven_datacadastro = models.DateTimeField(blank=True, null=True)
    ven_dataatualizacao = models.DateTimeField(blank=True, null=True)
    ven_endereco = models.CharField(max_length=60, blank=True, null=True)
    ven_numero = models.CharField(max_length=15, blank=True, null=True)
    ven_bairro = models.CharField(max_length=30, blank=True, null=True)
    ven_cep = models.IntegerField(blank=True, null=True)
    cid_codigo = models.IntegerField(blank=True, null=True)
    ven_fone = models.CharField(max_length=17, blank=True, null=True)
    ven_celular = models.CharField(max_length=17, blank=True, null=True)
    ven_email = models.CharField(max_length=50, blank=True, null=True)
    ven_observacao = models.CharField(max_length=170, blank=True, null=True)
    ban_codigo = models.IntegerField(blank=True, null=True)
    ven_agencia = models.CharField(max_length=7, blank=True, null=True)
    ven_contacorrente = models.CharField(max_length=15, blank=True, null=True)
    ven_cpf = models.CharField(max_length=20, blank=True, null=True)
    ven_descricaoauxiliar = models.CharField(max_length=60, blank=True, null=True)
    ven_situacao = models.CharField(max_length=1, blank=True, null=True)
    ven_descricaoweb = models.CharField(max_length=60, blank=True, null=True)
    ven_codigoimportacao = models.IntegerField(blank=True, null=True)
    sve_codigo = models.IntegerField(blank=True, null=True)
    loj_codigo = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'vendedor'
