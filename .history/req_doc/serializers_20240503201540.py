# serializers.py
from rest_framework import serializers
from .models import Project, Definition, Requirement

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['id', 'name', 'description']

class DefinitionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Definition
        fields = ['id', 'project', 'name', 'alias', 'description']

class RequirementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Requirement
        fields = ['id', 'project', 'status', 'description', 'definitions', 'priority']
