# from rest_framework import generics, status
# from rest_framework.response import Response
# from rest_framework.request import Request
# from apps.user.serializers.user_detail_serializer import UserDetailSerializer
# from apps.user.models.user import User
# from typing import Any
#
#
# class GetUserByUsernameView(generics.GenericAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserDetailSerializer
#
#     def get(self, request: Request, *args: Any, **kwargs: Any) -> Response:
#         username = request.data['payload'].get['username']
#         qs = User.objects.filter(username=username)
#         response_data = UserDetailSerializer(qs, many=True).data
#         return Response(data=response_data, status=status.HTTP_200_OK)
