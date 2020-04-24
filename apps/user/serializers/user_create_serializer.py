from rest_framework import serializers
from apps.user.models.user import User
from typing import Dict, Any


class UserCreateSerializer(serializers.ModelSerializer):

    password2 = serializers.CharField(max_length=255, style={'input_type': 'password'}, write_only=True)

    def validate(self, attrs: Dict[str, Any]) -> Dict[str, Any]:
        password = attrs.get('password')
        password2 = attrs.get('password2')
        if not password == password2:
            raise serializers.ValidationError('Passwords do not match')
        return attrs

    def create(self, validated_data: Dict[str, Any]) -> User:
        validated_data.pop('password2')
        user = super().create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

    class Meta:
        model = User
        fields = ('id', 'password', 'first_name', 'last_name', 'username', 'password2', )
