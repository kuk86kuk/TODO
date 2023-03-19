import json
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIRequestFactory, force_authenticate, APIClient, APISimpleTestCase, APITestCase
from django.contrib.auth.models import User
from .views import AuthorModelViewSet
from .models import Author, Book
from mixer.backend.django import mixer

class TestAuthorViewSet(TestCase):
    def test_get_list(self):
        factory = APIRequestFactory()
        request = factory.get('/api/authors/')
        view = AuthorModelViewSet.as_view({'get': 'list'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    

    def test_create_guest(self):
        factory = APIRequestFactory()
        request = factory.post('/api/authors/', {'name': 'Пушкин',
        'birthday_year': 1799}, format='json')
        view = AuthorModelViewSet.as_view({'post': 'create'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


    def test_edit_mixer(self):
        book = mixer.blend(Book)
        admin = User.objects.create_superuser('admin', 'admin@admin.com',
        'admin123456')
        self.client.login(username='admin', password='admin123456')
        response = self.client.put(f'/api/books/{book.id}/', {'name': 'Руслан и Людмила', 'author': book.author.id})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        book = Book.objects.get(id=book.id)
        self.assertEqual(book.name,'Руслан и Людмила')

    def test_get_detail(self):
        book = mixer.blend(Book, name='Алые паруса')
        response = self.client.get(f'/api/books/{book.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response_book = json.loads(response.content)
        self.assertEqual(response_book['name'], 'Алые паруса')


    def test_get_detail_author(self):
        book = mixer.blend(Book, author__name='Грин')
        response = self.client.get(f'/api/books/{book.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response_book = json.loads(response.content)
        self.assertEqual(response_book['author']['name'], 'Грин')
