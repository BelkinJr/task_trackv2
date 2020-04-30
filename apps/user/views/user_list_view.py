from rest_framework import generics
from apps.user.models import User
from apps.user.serializers.user_detail_serializer import UserDetailSerializer


class UserListView(generics.GenericAPIView):
    queryset = User.objects.all()
    serializer_class = UserDetailSerializer
