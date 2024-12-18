from rest_framework import serializers
from app.models import App, Category, SubCategory


class ImageUploadSerializer(serializers.Serializer):
    image = serializers.ImageField()


class AppSerializer(serializers.ModelSerializer):
    """Serializer for app model"""
    pic = serializers.ImageField(required=True)
    class Meta:
        model = App
        fields = "__all__"
