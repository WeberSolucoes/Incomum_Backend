from django.test import TestCase
from rest_framework.test import APIRequestFactory
from rest_framework import status
from rest_framework.request import Request
from rest_framework import status
from rest_framework.parsers import JSONParser

from ..models import Loja
from ..serializers.lojaSerializer import LojaSerializer
from ..services.lojaService import findById, create, update, delete, list_all

class LojaTests(TestCase):

    def setUp(self):
        self.factory = APIRequestFactory()
        self.loja = Loja.objects.create(
            loj_descricao="Loja Teste",
            loj_responsavel="Responsável Teste",
            loj_email="teste@loja.com"
        )

    def test_findById(self):
        request = self.factory.get(f'/loja/{self.loja.loj_codigo}/')
        response = findById(self.loja.loj_codigo)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['loj_descricao'], self.loja.loj_descricao)

    def test_create(self):
        data = {
            'loj_descricao': 'Nova Loja',
            'loj_responsavel': 'Novo Responsável',
            'loj_email': 'novo@loja.com'
        }
        request = self.factory.post('/loja/', data, format='json')
        request = Request(request, parsers=[JSONParser()])
        response = create(request)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Loja.objects.count(), 2)
        self.assertEqual(response.data['loj_descricao'], 'Nova Loja')

    def test_update(self):
        data = {
            'loj_descricao': 'Loja Atualizada',
            'loj_responsavel': 'Responsável Atualizado',
            'loj_email': 'atualizado@loja.com'
        }
        request = self.factory.put(f'/loja/{self.loja.loj_codigo}/', data, format='json')
        request = Request(request, parsers=[JSONParser()])
        response = update(request, self.loja.loj_codigo)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.loja.refresh_from_db()
        self.assertEqual(self.loja.loj_descricao, 'Loja Atualizada')

    def test_delete(self):
        request = self.factory.delete(f'/loja/{self.loja.loj_codigo}/')
        response = delete(self.loja.loj_codigo)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Loja.objects.count(), 0)

    def test_list_all(self):
        request = self.factory.get('/loja/')
        response = list_all()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['loj_descricao'], self.loja.loj_descricao)
