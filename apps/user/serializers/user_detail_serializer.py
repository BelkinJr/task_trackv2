from rest_framework import serializers
from apps.user.models.user import User


class UserDetailSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=255)
    first_name = serializers.CharField(max_length=255)
    last_name = serializers.CharField(max_length=255)
    id = serializers.UUIDField(read_only=True)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'id')
