from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .views.viewExemplo import *
urlpatterns = [
    path("model1/create/", post,name='Model1'),
    path('model1/update/<int:id>/', put, name='modelos-detail'),
    path("model1/findby-id/<int:id>/",get,name='get'),
    path("model1/list-all/",getAll,name='list'),
    path("model1/delete/<int:id>/",delete,name='delete'),

    path("userDetails/",userDetails),

    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]