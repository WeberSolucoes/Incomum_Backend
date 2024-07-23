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

    #Usuario
    # path('user/find-byid/<int:id>/', usuarioViews.findById),
    # path('user/create/', usuarioViews.create),
    # path('user/update/<int:id>/', usuarioViews.update),
    # path('user/delete/<int:id>/', usuarioViews.delete),
    # path('user/list-all/', usuarioViews.list_all),
    # path('user/updatePassword/', usuarioViews.update_password),
    # path('user/updatePassword-confirm/<uidb64>/<token>/', usuarioViews.update_password_confirm),
    
    #UsuarioGroups
    # path('user/group/listGroups/<int:id>/', usuarioViews.list_groups),
    # path('user/group/updateGroups/<int:id>/', usuarioViews.update_groups),
    # path('user/permission/listPermissions/<int:id>/', usuarioViews.list_permissions),
    # path('user/permission/updatePermissions/<int:id>/', usuarioViews.update_permissions),
]