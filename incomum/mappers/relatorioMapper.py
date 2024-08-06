from typing import List
from incomum.models.relatorio import FaturamentoSimplificado
from incomum.serializers.relatorioSerializer import RelatorioSimplificadoResponse


def entitiesToDtos(entities:List[FaturamentoSimplificado]) -> List[RelatorioSimplificadoResponse]:
    datas: List[RelatorioSimplificadoResponse] = []
    for entity in entities:
        data = {
            'id': entity.fim_codigo,
            'tipo': entity.fim_tipo,
            'numeroVenda': entity.tur_numerovenda,
            # 'numeroPacote': entity.numeroPacote,
            'dataVenda': entity.fim_data.strftime('%d/%m/%Y'),
            'valorLiquidoVenda': entity.fim_valorliquido,
            'markUp': entity.fim_markup,
            'valorInc': entity.fim_valorinc,
            'valorIncAjustado': entity.fim_valorincajustado,
            'areaComercial': entity.aco_codigo.aco_descricao,
            'agencia': entity.age_codigo.age_descricao
        }
        datas.append(data)
    dto = RelatorioSimplificadoResponse(data=datas, many=True)
    dto.is_valid(raise_exception=True)
    return dto