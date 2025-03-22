from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from rest_framework.serializers import ModelSerializer
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from .models import Book, User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'password']
        extra_kwargs = {
            'password': {'write_only': True},
            'email': {'required': True, 'allow_blank': False}
        }

    def create(self, validated_data):
        """Hash password when creating a new user"""
        validated_data['password'] = make_password(validated_data['password'])
        return super().create(validated_data)

    def update(self, instance, validated_data):
        """Ensure password is hashed when updating"""
        if 'password' in validated_data:
            validated_data['password'] = make_password(validated_data['password'])
        return super().update(instance, validated_data)


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'published_date', 'isbn', 'available']
        read_only_fields = ['id']


class AdminSignupSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ["email", "password"]

    def create(self, validated_data):
        email = validated_data["email"]
        password = validated_data["password"]

        # Check if user exists
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError({"error": "Admin with this email already exists"})

        # Create superuser
        user = User.objects.create_superuser(username=email, email=email, password=password)
        return user