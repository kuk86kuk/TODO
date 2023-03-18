from rest_framework.viewsets import ModelViewSet
from .models import Project, ToDo
from .serializers import ToDoModelSerializer, ProjectModelSerializer
from rest_framework.permissions import IsAuthenticated




from rest_framework.pagination import LimitOffsetPagination

class ArticleLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 2


class ProjectModelViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Project.objects.all()
    serializer_class = ProjectModelSerializer
    pagination_class = ArticleLimitOffsetPagination



class TodoModelViewSet(ModelViewSet):
    queryset = ToDo.objects.all()
    serializer_class = ToDoModelSerializer
    pagination_class = ArticleLimitOffsetPagination



