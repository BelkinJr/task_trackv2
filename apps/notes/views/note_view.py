from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.request import Request
from apps.notes.models.note import Note
from apps.user.models.user import User
from typing import Any
from apps.notes.serializers.note_create_serializer import NoteCreateSerializer
from apps.notes.decorators import login_required


class NoteView(generics.GenericAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteCreateSerializer

    @login_required
    def post(self, request: Request, *args: Any, user: User, **kwargs: Any) -> Response:
        request.data['payload'].update({'author': user.id})
        serializer = self.get_serializer(data=request.data)
        if not serializer.is_valid():
            return Response(data=serializer.errors)
        note_obj = serializer.create(serializer.validated_data)
        response_data = {'note created TEST'}
        return Response(data=response_data, status=status.HTTP_201_CREATED)