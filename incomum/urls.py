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
    path('Usuario_Comercial/find-byid/<int:id>/', usuarioComercialViews.find_by_id),
    path('Usuario_Comercial/create/', usuarioComercialViews.create),
    path('Usuario_Comercial/update/<int:id>/', usuarioComercialViews.update),
    path('Usuario_Comercial/delete/<int:id>/', usuarioComercialViews.delete),
    path('Usuario_Comercial/list-all/<int:id>/', usuarioComercialViews.list_all),

    path('relatorio/find-byid/<int:id>/', relatorioViews.find_by_id),
    path('relatorio/create/', relatorioViews.create),
    path('relatorio/update/<int:id>/', relatorioViews.update),
    path('relatorio/delete/<int:id>/', relatorioViews.delete),
    path('relatorio/list-all/', relatorioViews.list_all),
    path('relatorio/unidade/', relatorioViews.filtraunidade),
    path('relatorio/vendedor/', relatorioViews.filtravendedor)

]