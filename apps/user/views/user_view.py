from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.request import Request
from apps.user.models import User
from apps.user.serializers.user_create_serializer import UserCreateSerializer
from apps.user.serializers.user_detail_serializer import UserDetailSerializer
from typing import Any


class UserView(generics.GenericAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer

    def post(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        data = request.data
        serializer = self.get_serializer(data=data)
        if not serializer.is_valid():
            return Response(data=serializer.errors)
        user_obj = serializer.create(serializer.validated_data)
        response_data = {'user': UserDetailSerializer(user_obj).data}
        return Response(data=response_data, status=status.HTTP_201_CREATED)

    def get(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        users_qs = self.get_queryset()
        response_data = UserDetailSerializer(users_qs, many=True).data
        return Response(data=response_data, status=status.HTTP_200_OK)
