from django.contrib.auth.models import User

from rest_framework import serializers

from .models import Url


class SignUpSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "password"]

    def validate_username(self, value):
        if User.objects.filter(username=value).exists():
            raise serializers.ValidationError("Username already exists")
        return value

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class CreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Url
        fields = [
            "url",
        ]
        read_only_fields = ["id", "short_code", "created_at", "updated_at"]

    def validate_url(self, value):
        if Url.objects.filter(url=value).exists():
            raise serializers.ValidationError("Url already exists")
        return value
