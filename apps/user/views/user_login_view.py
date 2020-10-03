from django.contrib.auth import authenticate
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.request import Request
from apps.user.serializers.user_login_serializer import UserLoginSerializer
from apps.user.utils.create_token import create_access_and_refresh_token
from apps.user.models.user import User
from typing import Any


class UserLoginView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserLoginSerializer

    def post(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        serializer = self.get_serializer(data=request.data)
        if not serializer.is_valid():
            return Response(data=serializer.errors)

        user = authenticate(username=serializer.validated_data['username'], password=serializer.validated_data['password'])
        if user is None:
            return Response({'Error': "Invalid username/password"}, status="400")

        tokens = create_access_and_refresh_token({'id': str(user.id)})

        return Response(data=tokens, status=200)
