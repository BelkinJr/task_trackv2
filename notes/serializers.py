from rest_framework import serializers
from notes.models import Note
from user.serializers import UserSerializer

class NoteSerializer(serializers.ModelSerializer):

    author = UserSerializer()
    
    class Meta:
        model = Note
        fields = ('body','author')