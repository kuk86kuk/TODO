from rest_framework.serializers import HyperlinkedModelSerializer
from .models import User

class UsesModelSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = '__all__'