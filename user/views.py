from rest_framework  import status, generics, serializers
from rest_framework.response import Response
from .models import User
from .serializers import UserSerializer

class UserCreateAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def post (self, request, *args, **kwargs):
        data = request.data
        serializer = UserSerializer(data=data)
        if not serializer.is_valid():
            return Response(data=serializer.errors)
        user_obj = serializer.create(serializer.validated_data)
        response_data = {'user': UserSerializer(user_obj).data}
        return Response(data=response_data, status=status.HTTP_201_CREATED)


class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer