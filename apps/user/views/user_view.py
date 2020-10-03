from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.request import Request

from apps.base.decorators.login_required import login_required
from apps.user.models import User
from apps.user.serializers.user_create_serializer import UserCreateSerializer
from apps.user.serializers.user_detail_serializer import UserDetailSerializer
from typing import Any

from helpers.responses import CreatedStdResponse


class UserView(generics.GenericAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer

    @login_required
    def get(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        response_data = UserDetailSerializer(self.get_queryset(), many=True).data
        return Response(data=response_data, status=status.HTTP_200_OK)

    def post(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        serializer = self.get_serializer(data=request.data)
        if not serializer.is_valid():
            return Response(data=serializer.errors)

        user_obj = serializer.create(serializer.validated_data)
        return CreatedStdResponse(data={'id': user_obj.id})
