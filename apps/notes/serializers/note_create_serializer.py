from rest_framework import serializers
from apps.notes.models.note import Note
from apps.user.serializers.user_detail_serializer import UserDetailSerializer


class NoteCreateSerializer(serializers.ModelSerializer):

    author = UserDetailSerializer()

    class Meta:
        model = Note
        fields = ('author', 'body')
