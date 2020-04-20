from rest_framework import serializers

from apps.notes.models.note import Note
from apps.user.serializers.user_create_serializer import UserCreateSerializer


class NoteDetailSerializer(serializers.ModelSerializer):

    author = UserCreateSerializer()  # создай и юзай здесь UserDetailSerializer
    
    class Meta:
        model = Note
        fields = ('body', 'author', )
