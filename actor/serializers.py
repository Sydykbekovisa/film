from rest_framework.serializers import ModelSerializer
from .models import Actors


class ActorsSerializersList(ModelSerializer):
    class Meta:
        model = Actors
        fields = '__all__'
