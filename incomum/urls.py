from django import views
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from django.conf import settings
from django.conf.urls.static import static

from .views import areaComercialViews, lojaViews, usuarioComercialViews, relatorioViews, relatorioViews,agenciaViews,vendedorViews,userViews,agenteViews,aeroportoViews,paisViews,cidadeViews,moedaViews,cepViews,departamentoViews,companhiaViews,assinaturaViews,classeViews,tipoAcomodacaoViews,tipoPadraoViews,tipoRegimeViews,situacaoTuristicoViews,servicoTuristicoViews,bandeiraViews,formaPagamentoViews,parceiroViews,parceiroContatoViews,bancoViews,despesasViews,centroCustoViews,subgrupoViews,despesasGeralViews 
urlpatterns = [

    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    #AreaComercial
    path('areacomercial/find-byid/<int:id>/', areaComercialViews.find_by_id) ,
    path('areacomercial/create/', areaComercialViews.create),
    path('areacomercial/find-byloja/<int:id>/', areaComercialViews.find_by_loja),
    path('areacomercial/update/<int:id>/', areaComercialViews.update),
    path('areacomercial/delete/<int:id>/', areaComercialViews.delete),
    path('areacomercial/list-all/', areaComercialViews.list_all),

    #Loja
    path('loja/find-byid/<int:id>/', lojaViews.find_by_id),
    path('loja/create/', lojaViews.create),
    path('loja/update/<int:id>/', lojaViews.update),
    path('loja/delete/<int:id>/', lojaViews.delete),
    path('loja/list-all/', lojaViews.list_all),
    #path('loja/find-vinculadas/<int:aco_codigo>/', lojaViews.find_vinculadas),


    #LojaComercial
    #path('lojaComercial/find-byid/<int:id>',lojaComercialViews.find_by_id),
    #path('lojaComercial/create/', lojaComercialViews.create),
    #path('lojaComercial/update/<int:id>/', lojaComercialViews.update),
    #path('lojaComercial/delete/<int:id>/', lojaComercialViews.delete),
    #path('lojaComercial/list-all/', lojaComercialViews.list_all),

    #Agencia
    path('agencia/find-byid/<int:id>/', agenciaViews.find_by_id),
    path('agencia/create/', agenciaViews.create),
    path('agencia/update/<int:id>/', agenciaViews.update),
    path('agencia/delete/<int:id>/', agenciaViews.delete),
    path('agencia/list-all/', agenciaViews.list_all),
    path('agencia/upload/<int:id>/', agenciaViews.update_logo),
    path('agencia/<int:id>/imagem/', agenciaViews.get_agencia_imagem),

    #UsuarioComercial
    path('usuario_comercial/find-byid/<int:id>/', usuarioComercialViews.find_by_id),
    path('usuario_comercial/create/', usuarioComercialViews.create),
    path('usuario_comercial/update/<int:id>/', usuarioComercialViews.update),
    path('usuario_comercial/delete/<int:id>/', usuarioComercialViews.delete),
    path('usuario_comercial/list-all/<int:id>/', usuarioComercialViews.list_all),

    #Relatorio
    path('relatorio/list-all-by-filter/', relatorioViews.list_all_byfilter),
    path('relatorio/total-by-filter/', relatorioViews.total_byfilter),
    path('relatorio/loja-by-user/', relatorioViews.list_all_lojas_byfilter),
    path('relatorio/area-by-user/', relatorioViews.list_all_areas_byfilter),
    path('relatorio/vendedor-by-user/', relatorioViews.list_all_vendedores_byfilter),
    path('relatorio/agencia-by-user/', relatorioViews.list_all_agencias_byfilter),
    path('relatorio/download-relatorio/', relatorioViews.create_excel_byfilter),
    path('relatorio/list-all-area/', relatorioViews.list_all_areas),  # Quando não há unidade selecionada
    path('relatorio/list-all-areas/<int:unidade_id>/', relatorioViews.list_all_areas),
    path('relatorio/obter-dados-unidade/', relatorioViews.obter_dados_unidade),
    path('relatorio/obter-dados-agencia/', relatorioViews.obter_dados_agencia),
    #Vendedor
    path('vendedor/find-byid/<int:id>/', vendedorViews.find_by_id),
    path('vendedor/create/', vendedorViews.create),
    path('vendedor/update/<int:id>/', vendedorViews.update),
    path('vendedor/delete/<int:id>/', vendedorViews.delete),
    path('vendedor/list-all/', vendedorViews.list_all),

    #Usuario
    path('usuario/login/', userViews.login),
    path('usuario/permission/', userViews.user_permissions_view),

    #Agente
    path('agente/create/', agenteViews.create),
    path('agente/find-byid/<int:id>/', agenteViews.find_by_id),
    path('agente/update/<int:id>/',agenteViews.update),
    path('agente/delete/<int:id>/', agenteViews.delete),
    path('agente/list-all/', agenteViews.list_all),
    path('agente/<int:age_codigo>/', agenteViews.get_agentes_por_agencia),

    #Aeroporto
    path('aeroporto/create/', aeroportoViews.create),
    path('aeroporto/find-byid/<int:id>/', aeroportoViews.find_by_id),
    path('aeroporto/update/<int:id>/',aeroportoViews.update),
    path('aeroporto/delete/<int:id>/', aeroportoViews.delete),
    path('aeroporto/list-all/', aeroportoViews.list_all),

    #Pais
    path('pais/find-byid/<int:id>/', paisViews.find_by_id),
    path('pais/create/', paisViews.create),
    path('pais/update/<int:id>/', paisViews.update),
    path('pais/delete/<int:id>/', paisViews.delete),
    path('pais/list-all/', paisViews.list_all),

    #Cidade
    path('cidade/find-byid/<int:id>/', cidadeViews.find_by_id),
    path('cidade/create/', cidadeViews.create),
    path('cidade/update/<int:id>/', cidadeViews.update),
    path('cidade/delete/<int:id>/', cidadeViews.delete),
    path('cidade/list-all/', cidadeViews.list_all),

    #Moeda
    path('moeda/find-byid/<int:id>/', moedaViews.find_by_id),
    path('moeda/create/', moedaViews.create),
    path('moeda/update/<int:id>/', moedaViews.update),
    path('moeda/delete/<int:id>/', moedaViews.delete),
    path('moeda/list-all/', moedaViews.list_all),

    #Cep
    path('cep/find-byid/<int:id>/', cepViews.find_by_id),
    path('cep/create/', cepViews.create),
    path('cep/update/<int:id>/', cepViews.update),
    path('cep/delete/<int:id>/', cepViews.delete),
    path('cep/list-all/', cepViews.list_all),

    #Departamento
    path('departamento/find-byid/<int:id>/', departamentoViews.find_by_id),
    path('departamento/create/', departamentoViews.create),
    path('departamento/update/<int:id>/', departamentoViews.update),
    path('departamento/delete/<int:id>/', departamentoViews.delete),
    path('departamento/list-all/', departamentoViews.list_all),

    #Companhia
    path('companhia/find-byid/<int:id>/', companhiaViews.find_by_id),
    path('companhia/create/', companhiaViews.create),
    path('companhia/update/<int:id>/', companhiaViews.update),
    path('companhia/delete/<int:id>/', companhiaViews.delete),
    path('companhia/list-all/', companhiaViews.list_all),

    #Assinatura
    path('assinatura/find-byid/<int:id>/', assinaturaViews.find_by_id),
    path('assinatura/create/', assinaturaViews.create),
    path('assinatura/update/<int:id>/', assinaturaViews.update),
    path('assinatura/delete/<int:id>/', assinaturaViews.delete),
    path('assinatura/list-all/', assinaturaViews.list_all),

    #Classe
    path('classe/find-byid/<int:id>/', classeViews.find_by_id),
    path('classe/create/', classeViews.create),
    path('classe/update/<int:id>/', classeViews.update),
    path('classe/delete/<int:id>/', classeViews.delete),
    path('classe/list-all/', classeViews.list_all),

    #Acomodação
    path('acomodacao/find-byid/<int:id>/', tipoAcomodacaoViews.find_by_id),
    path('acomodacao/create/', tipoAcomodacaoViews.create),
    path('acomodacao/update/<int:id>/', tipoAcomodacaoViews.update),
    path('acomodacao/delete/<int:id>/', tipoAcomodacaoViews.delete),
    path('acomodacao/list-all/', tipoAcomodacaoViews.list_all),

    #Padrão
    path('padrao/find-byid/<int:id>/', tipoPadraoViews.find_by_id),
    path('padrao/create/', tipoPadraoViews.create),
    path('padrao/update/<int:id>/', tipoPadraoViews.update),
    path('padrao/delete/<int:id>/', tipoPadraoViews.delete),
    path('padrao/list-all/', tipoPadraoViews.list_all),

    #Regime
    path('regime/find-byid/<int:id>/', tipoRegimeViews.find_by_id),
    path('regime/create/', tipoRegimeViews.create),
    path('regime/update/<int:id>/', tipoRegimeViews.update),
    path('regime/delete/<int:id>/', tipoRegimeViews.delete),
    path('regime/list-all/', tipoRegimeViews.list_all),

    #Situação Turistico
    path('situacaoturistico/find-byid/<int:id>/', situacaoTuristicoViews.find_by_id),
    path('situacaoturistico/create/', situacaoTuristicoViews.create),
    path('situacaoturistico/update/<int:id>/', situacaoTuristicoViews.update),
    path('situacaoturistico/delete/<int:id>/', situacaoTuristicoViews.delete),
    path('situacaoturistico/list-all/', situacaoTuristicoViews.list_all),

    #Serviço Turistico
    path('servicoturistico/find-byid/<int:id>/', servicoTuristicoViews.find_by_id),
    path('servicoturistico/create/', servicoTuristicoViews.create),
    path('servicoturistico/update/<int:id>/', servicoTuristicoViews.update),
    path('servicoturistico/delete/<int:id>/', servicoTuristicoViews.delete),
    path('servicoturistico/list-all/', servicoTuristicoViews.list_all),

    #Bandeira
    path('bandeira/find-byid/<int:id>/', bandeiraViews.find_by_id),
    path('bandeira/create/', bandeiraViews.create),
    path('bandeira/update/<int:id>/', bandeiraViews.update),
    path('bandeira/delete/<int:id>/', bandeiraViews.delete),
    path('bandeira/list-all/', bandeiraViews.list_all),

    #Forma De Pagamento
    path('formapagamento/find-byid/<int:id>/', formaPagamentoViews.find_by_id),
    path('formapagamento/create/', formaPagamentoViews.create),
    path('formapagamento/update/<int:id>/', formaPagamentoViews.update),
    path('formapagamento/delete/<int:id>/', formaPagamentoViews.delete),
    path('formapagamento/list-all/', formaPagamentoViews.list_all),

    #Parceiro
    path('parceiro/find-byid/<int:id>/', parceiroViews.find_by_id),
    path('parceiro/create/', parceiroViews.create),
    path('parceiro/update/<int:id>/', parceiroViews.update),
    path('parceiro/delete/<int:id>/', parceiroViews.delete),
    path('parceiro/list-all/', parceiroViews.list_all),

    #Parceiro
    path('parceirocontato/find-byid/<int:id>/', parceiroContatoViews.find_by_id),
    path('parceirocontato/create/', parceiroContatoViews.create),
    path('parceirocontato/update/<int:id>/', parceiroContatoViews.update),
    path('parceirocontato/delete/<int:id>/', parceiroContatoViews.delete),
    path('parceirocontato/list-all/', parceiroContatoViews.list_all),

    #Banco
    path('banco/find-byid/<int:id>/', bancoViews.find_by_id),
    path('banco/create/', bancoViews.create),
    path('banco/update/<int:id>/', bancoViews.update),
    path('banco/delete/<int:id>/', bancoViews.delete),
    path('banco/list-all/', bancoViews.list_all),


    #Despesas
    path('despesas/find-byid/<int:id>/', despesasViews.find_by_id),
    path('despesas/create/', despesasViews.create),
    path('despesas/update/<int:id>/', despesasViews.update),
    path('despesas/delete/<int:id>/', despesasViews.delete),
    path('despesas/list-all/', despesasViews.list_all),

    #Centro De Custo
    path('centrocusto/find-byid/<int:id>/', centroCustoViews.find_by_id),
    path('centrocusto/create/', centroCustoViews.create),
    path('centrocusto/update/<int:id>/', centroCustoViews.update),
    path('centrocusto/delete/<int:id>/', centroCustoViews.delete),
    path('centrocusto/list-all/', centroCustoViews.list_all),

    #Subgrupo
    path('subgrupo/find-byid/<int:id>/', subgrupoViews.find_by_id),
    path('subgrupo/create/', subgrupoViews.create),
    path('subgrupo/update/<int:id>/', subgrupoViews.update),
    path('subgrupo/delete/<int:id>/', subgrupoViews.delete),
    path('subgrupo/list-all/', subgrupoViews.list_all),

    #Despesas Geral
    path('despesasgeral/find-byid/<int:id>/', despesasGeralViews.find_by_id),
    path('despesasgeral/create/', despesasGeralViews.create),
    path('despesasgeral/update/<int:id>/', despesasGeralViews.update),
    path('despesasgeral/delete/<int:id>/', despesasGeralViews.delete),
    path('despesasgeral/list-all/', despesasGeralViews.list_all),




    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
