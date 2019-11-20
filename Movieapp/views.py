from django.shortcuts import render

# Create your views here.
from.models import Actor,Movie
from .serializers import MovieSerializer,ActorSerializer
from rest_framework.viewsets import ModelViewSet

class MovieOperation(ModelViewSet):
    serializer_class = MovieSerializer
    queryset = Movie.objects.all()

class ActorOperation(ModelViewSet):
    serializer_class = ActorSerializer
    queryset = Actor.objects.all()