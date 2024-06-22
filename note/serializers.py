# note/serializers.py

from rest_framework import serializers
from .models import Note, NoteRelation

class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ['id', 'title', 'content', 'description', 'created_at', 'updated_at']

class NoteRelationSerializer(serializers.ModelSerializer):
    class Meta:
        model = NoteRelation
        fields = ['id', 'from_note', 'to_note']
