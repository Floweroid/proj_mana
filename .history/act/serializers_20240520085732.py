# serializers.py
from rest_framework import serializers
from .models import Note, Requirement,RequirementRelationship



class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = '__all__'

class RequirementSerializer(serializers.ModelSerializer):
    parents = serializers.PrimaryKeyRelatedField(many=True, queryset=Requirement.objects.all(), required=False)

    class Meta:
        model = Requirement
        fields = '__all__'

    def create(self, validated_data):
        parents_data = validated_data.pop('parents', None)
        requirement = Requirement.objects.create(**validated_data)
        if parents_data:
            for parent in parents_data:
                RequirementRelationship.objects.create(from_requirement=parent, to_requirement=requirement)
        return requirement
