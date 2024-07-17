from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from rest_framework.test import APIRequestFactory
from rest_framework import status
from ..models import AreaComercial, Loja
from ..services.areaComercialService import findById, create, findByLoja, update, delete, list_all
from  rest_framework.response import Response
from rest_framework.request import Request
from django.core.handlers.wsgi import WSGIRequest
import json
from rest_framework.parsers import JSONParser

class AreaComercialTestCase(TestCase):
    def setUp(self):
        # Criar objetos de teste, se necessário
        self.loja = Loja.objects.create(loj_codigo=1, loj_descricao='Loja Teste', loj_responsavel='João')
        self.area = AreaComercial.objects.create(aco_codigo=1, aco_descricao='Área Teste', aco_situacao=1, aco_rateio=50, loja_codigo=self.loja)

    def test_findById(self):
        # Teste para findById
        factory = APIRequestFactory()
        request = factory.get('/area_comercial/findById/')
        response = findById(id=self.area.aco_codigo)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create(self):
        # Teste para create
        factory = APIRequestFactory()
        data = {
            'aco_descricao': 'Nova Área',
            'aco_rateio': 60,
            'aco_situacao': 1,
            'id_loja': self.loja.loj_codigo
        }
        request = factory.post('/area_comercial/create/', data, format='json')
        request = Request(request, parsers=[JSONParser()])
        response = create(request)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_findByLoja(self):
        # Teste para findByLoja
        factory = APIRequestFactory()
        request = factory.get('/area_comercial/findByLoja/')
        response = findByLoja(id=self.loja.loj_codigo)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update(self):
        # Teste para update
        factory = APIRequestFactory()
        data = {
            'aco_descricao': 'Área Atualizada',
            'aco_rateio': 70,
            'aco_situacao': 0,  # Alterando a situação para teste
            'id_loja': self.loja.loj_codigo
        }
        # json_data = json.dumps(data)
        request = factory.put(f'/area_comercial/update/{self.area.aco_codigo}/', data, format='json')
        request = Request(request, parsers=[JSONParser()])
        response = update(request, id=self.area.aco_codigo)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete(self):
        # Teste para delete
        factory = APIRequestFactory()
        request = factory.delete(f'/area_comercial/delete/{self.area.aco_codigo}/')
        response = delete(self.area.aco_codigo)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_list_all(self):
        # Teste para list_all
        factory = APIRequestFactory()
        request = factory.get('/area_comercial/list_all/')
        response = list_all()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
