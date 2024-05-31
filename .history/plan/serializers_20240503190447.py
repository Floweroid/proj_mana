from rest_framework import serializers
from .models import Definition, Requirement

class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Definition
        fields = '__all__'
        

class StuffSerializer(serializers.ModelSerializer):
    class Meta:
        model = Requirement
        fields = '__all__'  # Specify the fields you want to include in the serializer