from rest_framework.viewsets import ModelViewSet
from .models import Project, ToDo
from .serializers import ToDoModelSerializer, ProjectModelSerializer



class ProjectModelViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectModelSerializer



class TodoModelViewSet(ModelViewSet):
    queryset = ToDo.objects.all()
    serializer_class = ToDoModelSerializer



