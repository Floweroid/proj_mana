# note/serializers.py

from rest_framework import serializers
from .models import Note, NotePointer

class NoteSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    updated_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    class Meta:
        model = Note
        fields = ['id', 'title', 'content', 'description', 'related', 'created_at', 'updated_at']

class NoteRelationSerializer(serializers.ModelSerializer):
    class Meta:
        model = NotePointer
        fields = ['id', 'from_note', 'to_note']
