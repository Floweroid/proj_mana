# serializers.py
from rest_framework import serializers
from .models import Note, Todo, TodoRelationship



class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = '__all__'
        
class TodoSerializer(serializers.ModelSerializer):
    parents = serializers.PrimaryKeyRelatedField(queryset=Todo.objects.all(), many=True, required=False)

    class Meta:
        model = Todo
        fields = ['id', 'name', 'status', 'description', 'priority', 'created_at', 'updated_at', 'start_time', 'end_time', 'parents']
        read_only_fields = ['created_at', 'updated_at']

    def create(self, validated_data):
        parents = validated_data.pop('parents', [])
        Todo = Todo.objects.create(**validated_data)
        for parent in parents:
            TodoRelationship.objects.create(from_Todo=parent, to_Todo=Todo)
        return Todo

    def update(self, instance, validated_data):
        parents = validated_data.pop('parents', None)
        if parents is not None:
            instance.parents.clear()
            for parent in parents:
                TodoRelationship.objects.create(from_Todo=parent, to_Todo=instance)
        return super().update(instance, validated_data)
