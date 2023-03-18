from rest_framework.viewsets import ModelViewSet
from .models import User
from .serializers import UserModelSerializer
from rest_framework.permissions import IsAdminUser



from rest_framework.pagination import LimitOffsetPagination

class ArticleLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 2

class UserModelViewSet(ModelViewSet):
    permission_classes = [IsAdminUser]
    queryset = User.objects.all()
    serializer_class = UserModelSerializer
    pagination_class = ArticleLimitOffsetPagination