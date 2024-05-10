from rest_framework import serializers
from recipe.models import Recipe,Review
from django.contrib.auth.models import User

class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = ['id','recipe_name', 'recipe_ingredients', 'instructions', 'cuisine', 'meal_type'] # created and updated is not added here


class UserSerializer(serializers.ModelSerializer):
    password=serializers.CharField(write_only=True)
    class Meta:
        model=User
        fields=['id','username','password']

    def create(self, validated_data):  # used to encrypt
        u = User.objects.create_user(username=validated_data['username'], password=validated_data['password'])
        u.save()
        return u


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id','recipe_name','user','rating','comment']