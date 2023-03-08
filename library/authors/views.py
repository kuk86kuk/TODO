from rest_framework.viewsets import ModelViewSet
from .models import Author
from .serializers import AuthorModelSerializer
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.views import APIView
from rest_framework.response import Response


class ArticleLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 20


class AuthorModelViewSet(ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorModelSerializer
    pagination_class = ArticleLimitOffsetPagination
