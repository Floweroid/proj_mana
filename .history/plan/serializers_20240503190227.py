from rest_framework import serializers
from .models import Recipe, Stuff

class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = '__all__'
        
# Serializer for the Stuff model
class StuffSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stuff
        fields = ('id', 'name', 'emoji')  # Specify the fields you want to include in the serializer