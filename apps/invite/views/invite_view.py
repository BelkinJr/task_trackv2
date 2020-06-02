from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.request import Request
from apps.invite.models.invite import Invite
from apps.user.models.user import User
from apps.team.models.team import Team
from apps.base.decorators import validate_team
from apps.invite.utils.create_invite_token import create_invite_token
from apps.invite.serializers.invite_serializer import InviteCreateSerializer
from typing import Any


class InviteView(generics.GenericAPIView):
    queryset = Invite.objects.all()
    serializer_class = InviteCreateSerializer

    @validate_team
    def post(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        team = kwargs.get('team')

        serializer = self.get_serializer(team=team, data=request.data)

        if not serializer.is_valid():
            return Response(data=serializer.errors)

        invite = serializer.create(serializer.validated_data)

        invite_id = {'inv_id': str(invite.id)}  # TODO: to be fixed
        invite_token = create_invite_token(invite_id)

        return Response(data=invite_token, status=200)
