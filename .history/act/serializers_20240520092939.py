# serializers.py
from rest_framework import serializers
from .models import Note, Requirement,RequirementRelationship



class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = '__all__'

from rest_framework import serializers
from .models import Requirement, RequirementRelationship

class RequirementSerializer(serializers.ModelSerializer):
    parents = serializers.PrimaryKeyRelatedField(queryset=Requirement.objects.all(), many=True, required=False)

    class Meta:
        model = Requirement
        fields = ['id', 'name', 'status', 'description', 'priority', 'created_at', 'updated_at', 'start_time', 'end_time', 'parents']
        read_only_fields = ['created_at', 'updated_at']

    def create(self, validated_data):
        parents = validated_data.pop('parents', [])
        requirement = Requirement.objects.create(**validated_data)
        for parent in parents:
            RequirementRelationship.objects.create(from_requirement=parent, to_requirement=requirement)
        return requirement

    def update(self, instance, validated_data):
        parents = validated_data.pop('parents', None)
        if parents is not None:
            instance.parents.clear()
            for parent in parents:
                RequirementRelationship.objects.create(from_requirement=parent, to_requirement=instance)
        return super().update(instance, validated_data)

    

