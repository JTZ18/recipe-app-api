"""
Serializers for the Recipe API view
"""
from rest_framework import serializers

from core.models import Recipe


class RecipeSerializer(serializers.ModelSerializer):
    """Serializer for the Recipe object"""

    class Meta:
        model = Recipe
        fields = (
            "id",
            "title",
            "time_minutes",
            "price",
            "link",
        )
        read_only_fields = ("id",)

    def create(self, validated_data):
        """Create a new recipe and return it"""
        return Recipe.objects.create(**validated_data)


class RecipeDetailSerializer(RecipeSerializer):
    """Serializer for the Recipe detail view"""

    class Meta(RecipeSerializer.Meta):
        fields = RecipeSerializer.Meta.fields + ("description",)
