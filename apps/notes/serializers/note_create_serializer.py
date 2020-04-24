from rest_framework import serializers
from apps.notes.models.note import Note
from typing import Dict, Any


class NoteCreateSerializer(serializers.ModelSerializer):

    def create(self, validated_data: Dict[str, Any]) -> Note:
        note = super().create(validated_data)
        note.save()
        return note
