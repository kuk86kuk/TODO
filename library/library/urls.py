from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from userapp.views import UserModelViewSet
from authors.views import AuthorModelViewSet
from todoapp.views import TodoModelViewSet, ProjectModelViewSet
from rest_framework.authtoken import views



router = DefaultRouter()
router.register('User', UserModelViewSet)
router.register('authors', AuthorModelViewSet)
router.register('Project', ProjectModelViewSet)
router.register('Todo', TodoModelViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include(router.urls)), 
    path('api-token-auth/', views.obtain_auth_token)
    ]
