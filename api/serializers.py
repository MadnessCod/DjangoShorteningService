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
            "id",
            "url",
            "short_code",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["id", "short_code", "created_at", "updated_at"]

    def create(self, validated_data):
        url = validated_data.get("url")
        existing = Url.objects.filter(url=url).first()
        if existing:
            return existing
        return Url.objects.create(**validated_data)
