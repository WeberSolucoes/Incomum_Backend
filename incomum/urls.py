from django import views
from django.urls import path

from .views import areaComercialViews, lojaViews, usuarioComercialViews, relatorioViews, relatorioViews
urlpatterns = [

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

    #UsuarioComercial
    path('usuario_comercial/find-byid/<int:id>/', usuarioComercialViews.find_by_id),
    path('usuario_comercial/create/', usuarioComercialViews.create),
    path('usuario_comercial/update/<int:id>/', usuarioComercialViews.update),
    path('usuario_comercial/delete/<int:id>/', usuarioComercialViews.delete),
    path('usuario_comercial/list-all/<int:id>/', usuarioComercialViews.list_all),

    #Relatorio
    path('relatorio/list-all-by-filter/', relatorioViews.list_all_byfilter),
    path('relatorio/loja-by-user/<int:id>/', relatorioViews.list_all_lojas_byfilter),
    path('relatorio/area-by-user/<int:id>/', relatorioViews.list_all_areas_byfilter),
    path('relatorio/vendedor-by-user/<int:id>/', relatorioViews.list_all_vendedores_byfilter),
    path('relatorio/agencia-by-user/<int:id>/', relatorioViews.list_all_agencias_byfilter),

]