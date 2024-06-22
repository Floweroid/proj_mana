# note/views.py

from rest_framework import generics
from .models import Note, NoteRelation
from .serializers import NoteSerializer, NoteRelationSerializer

class NoteListCreateView(generics.ListCreateAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer

class NoteDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer

class NoteRelationListCreateView(generics.ListCreateAPIView):
    queryset = NoteRelation.objects.all()
    serializer_class = NoteRelationSerializer

class NoteRelationDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = NoteRelation.objects.all()
    serializer_class = NoteRelationSerializer
