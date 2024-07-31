from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from ..services import relatorioService

from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from ..serializers.relatorioSerializer import *
from ..models import *

@swagger_auto_schema(
    methods=['post'],
    request_body= RelatorioFiltersSerializer,
    responses={200: RelatorioSimplificadoResponse(many=True)},
    tags=['Relatorio'],
)
@api_view(['POST'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def listByFilters(request):
    return relatorioService.listByFilters(request)