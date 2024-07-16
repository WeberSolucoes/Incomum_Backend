from django.urls import path
from .views.areaComercialViews import *
urlpatterns = [
    path('areacomercial/find-byid/<int:id>/', find_by_id) ,
    path('areacomercial/create/', create),
    path('areacomercial/find-byloja/<int:id>/', find_by_loja),
    path('areacomercial/update/<int:id>/', update),
    path('areacomercial/delete/<int:id>/', delete),
    path('areacomercial/list-all/', list_all),
]