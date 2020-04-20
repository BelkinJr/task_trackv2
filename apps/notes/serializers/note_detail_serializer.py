from rest_framework import serializers

from apps.notes.models.note import Note
from apps.user.serializers import UserSerializer


class NoteDetailSerializer(serializers.ModelSerializer):

    author = UserSerializer()
    
    class Meta:
        model = Note
        fields = ('body', 'author', )
