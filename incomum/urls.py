from django import views
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .views import areaComercialViews, lojaViews, usuarioComercialViews, relatorioViews, relatorioViews,agenciaViews,vendedorViews,userViews
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

    #Agencia
    path('agencia/find-byid/<int:id>/', agenciaViews.find_by_id),
    path('agencia/create/', agenciaViews.create),
    path('agencia/update/<int:id>/', agenciaViews.update),
    path('agencia/delete/<int:id>/', agenciaViews.delete),
    path('agencia/list-all/', agenciaViews.list_all),

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
    path('relatorio/list-all-areas/', relatorioViews.list_all_areas),
    path('relatorio/list-all-area/', relatorioViews.list_all_area),

    #Vendedor
    path('vendedor/find-byid/<int:id>/', vendedorViews.find_by_id),
    path('vendedor/create/', vendedorViews.create),
    path('vendedor/update/<int:id>/', vendedorViews.update),
    path('vendedor/delete/<int:id>/', vendedorViews.delete),
    path('vendedor/list-all/', vendedorViews.list_all),

    #Usuario
    path('usuario/login/', userViews.login),
]
