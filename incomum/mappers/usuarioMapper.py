from ..models.usuario import *
from ..serializers.usuarioSerializer import *
def DtoToEntity(dto: UsuarioDTOSerializer)-> Usuario:
    entity: Usuario = Usuario()
    return DtoToEntityUpdate(dto, entity)
def DtoToEntityUpdate(dto: UsuarioDTOSerializer, entity: Usuario)-> Usuario:
    entity.username = dto.validated_data.get('username') if dto.validated_data.get('username') else entity.username
    entity.email = dto.validated_data.get('email') if dto.validated_data.get('email') else entity.email
    entity.first_name = dto.validated_data.get('first_name') if dto.validated_data.get('first_name') else entity.first_name
    entity.last_name = dto.validated_data.get('last_name') if dto.validated_data.get('last_name') else entity.last_name
    entity.ven_codigo = dto.validated_data.get('ven_cod') if dto.validated_data.get('ven_cod') else entity.ven_codigo
    entity.usr_cpf = dto.validated_data.get('cpf') if dto.validated_data.get('cpf') else entity.usr_cpf
    entity.usr_datanascimento = dto.validated_data.get('data_nasc') if dto.validated_data.get('data_nasc') else entity.usr_datanascimento
    entity.loj_codigo = dto.validated_data.get('loja_id') if dto.validated_data.get('loja_id') else entity.loj_codigo

    return entity

def EntityToDto(entity):
    data = {
        'id': entity.id,
        'username': entity.username,
        'email': entity.email,
        'first_name': entity.first_name,
        'last_name': entity.last_name,
        'ven_cod': entity.ven_codigo,
        'cpf': entity.usr_cpf,
        'data_nasc': entity.usr_datanascimento,
        'loja_id': entity.loj_codigo_id,
        'dep_principal': entity.dep_codigo_id
    }
    dto = UsuarioDTOSerializer(data=data)
    dto.is_valid(raise_exception=True)
    return dto

def EntitiesToDtos(entities):
    datas = []
    for entity in entities:
        data = {
        'id': entity.id,
        'username': entity.username,
        'email': entity.email,
        'first_name': entity.first_name,
        'last_name': entity.last_name,
        'ven_cod': entity.ven_codigo,
        'cpf': entity.usr_cpf,
        'data_nasc': entity.usr_datanascimento,
        'loja_id': entity.loj_codigo_id,
        'dep_principal': entity.dep_codigo_id
        }
        datas.append(data)
    dto = UsuarioDTOSerializer(data=datas, many=True)
    dto.is_valid(raise_exception=True)
    return dto