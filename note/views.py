# note/views.py

from rest_framework import viewsets
from .models import Note, NotePointer
from .serializers import NoteSerializer, NoteRelationSerializer

class NoteViewSet(viewsets.ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer

class NoteRelationViewSet(viewsets.ModelViewSet):
    queryset = NotePointer.objects.all()
    serializer_class = NoteRelationSerializer
