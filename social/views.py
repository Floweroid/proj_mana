# act/views.py

from rest_framework import viewsets
from .models import Todo, Person, Media, SocialRelationship
from .serializers import TodoSerializer, PersonSerializer, MediaSerializer, SocialRelationshipSerializer

class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

class MediaViewSet(viewsets.ModelViewSet):
    queryset = Media.objects.all()
    serializer_class = MediaSerializer

class SocialRelationshipViewSet(viewsets.ModelViewSet):
    queryset = SocialRelationship.objects.all()
    serializer_class = SocialRelationshipSerializer
