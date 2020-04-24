from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.request import Request
from apps.user.models import User
from apps.user.serializers.user_create_serializer import UserCreateSerializer
from apps.user.serializers.user_detail_serializer import UserDetailSerializer
from typing import Any


class UserCreateView(generics.GenericAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer

    def post(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        data = request.data
        serializer = self.get_serializer(data=data)
        if not serializer.is_valid():
            return Response(data=serializer.errors)
        user_obj = serializer.create(serializer.validated_data)
        response_data = {'user': UserDetailSerializer(user_obj).data}  # Можно заменить на UserCreateSerializer
        return Response(data=response_data, status=status.HTTP_201_CREATED)
