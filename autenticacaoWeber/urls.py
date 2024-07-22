from django.urls import path
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)
from .views.tokenView import *
from .views.permissionsView import *
from .views.groupView import *
urlpatterns = [
    #Login
    path('token/login/', login_user, name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/user-id/', user_id, name='user_id'),
    # path('token/register/', register_user, name='register_user'),

    #Permissioes
    path('permissions/', permission_list, name='permission_list'),
    path('permissions/<int:pk>/', permission_detail, name='permission_detail'),
    path('permissions/list-by-groups/', permission_list_by_groups, name='permission_list_by_groups'),
    # path('permissions/create/', permission_create, name='permission_create'),
    # path('permissions/<int:pk>/update/', permission_update, name='permission_update'),
    # path('permissions/<int:pk>/delete/', permission_delete, name='permission_delete'),

    #Groups
    path('groups/', group_list, name='group_list'),
    path('groups/<int:pk>/', group_detail, name='group_detail'),
    path('groups/create/', group_create, name='group_create'),
    path('groups/<int:pk>/update/', group_update, name='group_update'),
    path('groups/<int:pk>/delete/', group_delete, name='group_delete'),

]