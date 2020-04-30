from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.request import Request
from apps.notes.models.note import Note
from apps.user.models.user import User
from typing import Any
from apps.notes.serializers.note_create_serializer import NoteCreateSerializer
from apps.notes.decorators import login_required


class NoteCreateView(generics.GenericAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteCreateSerializer

    @login_required
    def post(self, request: Request, *args: Any, user, **kwargs: Any) -> Response:
        # data = request.data['payload']
        request.data['payload'].update({'author': user.__dict__})
        print(request.data['payload'])
        serializer = self.get_serializer(data=request.data)
        if not serializer.is_valid():
            return Response(data=serializer.errors)
        note_obj = serializer.create(serializer.validated_data)
        response_data = {'note created TEST'}
        # response_data = {'note': NoteCreateView(note_obj).data}
        return Response(data=response_data, status=status.HTTP_201_CREATED)
