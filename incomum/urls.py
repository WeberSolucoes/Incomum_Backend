from django.urls import path
from .views import areaComercialViews, lojaViews, usuarioViews
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
]