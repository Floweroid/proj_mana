# serializers.py
from rest_framework import serializers
from .models import Note, Requirement



class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ['status','name','description','priority','start_time','end_time']
        
class RequirementSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S', required=False)
    updated_at = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S', required=False)
    class Meta:
        model = Requirement
        fields = '__all__'