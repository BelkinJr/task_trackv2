from rest_framework import serializers
from apps.user.models.user import User


class UserLoginSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('password', 'username', )
