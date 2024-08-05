from django.urls import path
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

from .views import usuarioViews, tokenView, permissionsView, groupView

urlpatterns = [
    #Login
    path('token/login/', tokenView.login_user, name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/user-id/', tokenView.user_id, name='user_id'),
    
    #user
    path('user/find-byid/<int:id>/', usuarioViews.findById),
    path('user/create/', usuarioViews.create),
    path('user/update/<int:id>/', usuarioViews.update),
    path('user/delete/<int:id>/', usuarioViews.delete),
    path('user/list-all/', usuarioViews.list_all),
    path('user/updatePassword/', usuarioViews.update_password),
    path('user/updatePassword-confirm/<uidb64>/<token>/', usuarioViews.update_password_confirm),

    #Permissioes
    path('permissions/', permissionsView.permission_list, name='permission_list'),
    path('permissions/<int:pk>/', permissionsView.permission_detail, name='permission_detail'),
    path('permissions/list-by-groups/', permissionsView.permission_list_by_groups, name='permission_list_by_groups'),
    path('permissions/listPermissions-by-user/<int:id>/', permissionsView.list_permissions),
    path('permissions/updatePermissions-by-user/<int:id>/', permissionsView.update_permissions),

    #Groups
    path('groups/', groupView.group_list, name='group_list'),
    path('groups/<int:pk>/', groupView.group_detail, name='group_detail'),
    path('groups/create/', groupView.group_create, name='group_create'),
    path('groups/<int:pk>/update/', groupView.group_update, name='group_update'),
    path('groups/<int:pk>/delete/', groupView.group_delete, name='group_delete'),
    path('groups/listGroups-by-user/<int:id>/', groupView.list_groups),
    path('groups/updateGroups-by-user/<int:id>/', groupView.update_groups),

]