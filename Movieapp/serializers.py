from rest_framework.serializers import ModelSerializer
from .models import *

class MovieSerializer(ModelSerializer):
    class Meta:
        model=Movie
        fields = '__all__'


class ActorSerializer(ModelSerializer):
    # Movi_Act=ModelSerializer(many=True)
    class Meta:
        model=Actor
        fields = '__all__'
