from rest_framework import serializers
from apps.user.models.user import User


class UserDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', )
