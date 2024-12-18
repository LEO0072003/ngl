from pyexpat import model
from django.contrib.auth.models import User
from .models import UserAppDownload
from rest_framework import serializers

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=8)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def create(self, validated_data):
        # Create the user with validated data
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user


class UserAppDownloadSerializer(serializers.ModelSerializer):
    point = serializers.SerializerMethodField()
    app = serializers.SerializerMethodField()

    class Meta:
        model = UserAppDownload
        fields = ["id","point","app", "screenshot"]
        extra_kwargs = {
            'user': {'required': False}
        }

    def get_app(self, obj):
        return obj.app.app_name

    def get_point(self, obj):
        return obj.app.points



class UserAppDownloadCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAppDownload
        fields = "__all__"
        extra_kwargs = {
            'user': {'required': False}
        }
