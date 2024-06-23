# act/serializers.py

from rest_framework import serializers
from .models import Todo, Person, Media, SocialRelationship

class TodoSerializer(serializers.ModelSerializer):
    duration = serializers.SerializerMethodField()

    class Meta:
        model = Todo
        fields = ['id', 'title', 'description', 'content', 'created_at', 'updated_at', 'start_time', 'end_time', 'due', 'duration']

    def get_duration(self, obj):
        duration = obj.duration()
        if duration:
            return str(duration)
        return "N/A"

class MediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Media
        fields = ['id', 'media', 'account']

class PersonSerializer(serializers.ModelSerializer):
    medias = MediaSerializer(many=True, read_only=True)
    age = serializers.SerializerMethodField()

    class Meta:
        model = Person
        fields = ['id', 'title', 'description', 'content', 'created_at', 'updated_at', 'fName', 'mid', 'lName', 'birthdate', 'age', 'medias']

    def get_age(self, obj):
        return obj.age()

class SocialRelationshipSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialRelationship
        fields = ['id', 'relation', 'from_person', 'to_person']
