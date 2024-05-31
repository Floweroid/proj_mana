# serializers.py
from rest_framework import serializers
from .models import Note, Requirement



class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = '__all__'
        
class RequirementSerializer(serializers.ModelSerializer):
    start_time = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S', required=False)
    end_time = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S', required=False)
    class Meta:
        model = Requirement
        fields = ['status','name','description','priority','start_time','end_time']