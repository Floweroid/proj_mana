# note/views.py

from rest_framework import viewsets
from .models import Note, NoteRelation
from .serializers import NoteSerializer, NoteRelationSerializer

class NoteViewSet(viewsets.ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer

class NoteRelationViewSet(viewsets.ModelViewSet):
    queryset = NoteRelation.objects.all()
    serializer_class = NoteRelationSerializer
