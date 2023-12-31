from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from apps.users.models import User

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'name', 'last_name', 'email')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = (
            'last_login', 'is_superuser', 'is_active', 'is_staff',
            'groups', 'user_permissions'
        )

    def create(self, validated_data):
        user = User(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

    def update(self, instance, validated_data):
        updated_user = super().update(instance, validated_data)
        updated_user.set_password(validated_data['password'])
        updated_user.save()
        return updated_user


class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User

    def to_representation(self, instance):
        return {
            'id': instance['id'],
            'username': instance['username'],
            'name': instance['name'],
            'last_name': instance['last_name'],
            'email': instance['email'],
        }


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    pass


class LogoutSerializer(serializers.Serializer):
    user = serializers.IntegerField(required=True)