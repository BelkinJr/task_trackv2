from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.request import Request
from apps.team.models import Team
from apps.user.models.user import User
from apps.team.serializers.team_create_serializer import TeamCreateSerializer
from apps.base.decorators import login_required
from typing import Any


class TeamView(generics.GenericAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamCreateSerializer

    @login_required
    def post(self, request: Request, *args: Any, user: User, **kwargs: Any) -> Response:
        request.data['payload'].update({'creator_id': user.id})
        serializer = self.get_serializer(data=request.data)
        if not serializer.is_valid():
            return Response(data=serializer.errors)
        team_obj = serializer.create(serializer.validated_data)
        response_data = {'team': TeamCreateSerializer(team_obj).data}
        return Response(data=response_data, status=status.HTTP_201_CREATED)
