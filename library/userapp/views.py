from rest_framework.viewsets import ModelViewSet
from .models import User
from .serializers import UserModelSerializer, UserSerializerWithFullName
from rest_framework.permissions import IsAdminUser
from rest_framework.pagination import LimitOffsetPagination

class ArticleLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 2

class UserModelViewSet(ModelViewSet):
    permission_classes = [IsAdminUser]
    queryset = User.objects.all()
    serializer_class = UserModelSerializer
    pagination_class = ArticleLimitOffsetPagination


class UserListAPIView(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserModelSerializer
    def get_serializer_class(self):
        if self.request.version == '0.2':
            return UserSerializerWithFullName
        return UserModelSerializer
