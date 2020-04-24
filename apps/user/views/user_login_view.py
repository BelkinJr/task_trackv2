from django.contrib.auth import authenticate
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.request import Request
from apps.user.serializers.user_login_serializer import UserLoginSerializer
from apps.user.utils.create_token import create_access_and_refresh_token
from typing import Any


class UserLoginView(generics.RetrieveAPIView):
    serializer_class = UserLoginSerializer

    def post(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        data = request.data
        serializer = self.get_serializer(data=data)
        if not serializer.is_valid():
            return Response(data=serializer.errors)
        username = request.data['username']
        password = request.data['password']
        user = authenticate(username=username, password=password)
        if user is None:
            return Response({'Error': "Invalid username/password"}, status="400")

        tokens = create_access_and_refresh_token(**data)

        return Response(data=tokens, status=200)
