from rest_framework import serializers
from apps.user.models.user import User


class UserLoginSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=255)
    password = serializers.CharField(max_length=255)

    class Meta:
        model = User
        fields = ('password', 'username', )
