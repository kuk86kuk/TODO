from rest_framework.viewsets import ModelViewSet
from .models import User
from .serializers import UsesModelSerializer

class UserModelViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UsesModelSerializer
    