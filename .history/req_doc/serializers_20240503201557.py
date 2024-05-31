# serializers.py
from rest_framework import serializers
from .models import Project, Definition, Requirement

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'

class DefinitionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Definition
        fields = '__all__'
class RequirementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Requirement
        fields = '__all__'