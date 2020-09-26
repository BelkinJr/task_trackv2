from rest_framework import generics
from rest_framework.response import Response
from rest_framework.request import Request
from apps.invite.models.invite_user_to_team import InviteUserToTeam
from apps.base.decorators import validate_team
from apps.invite.utils.create_invite_token import create_invite_token
from apps.invite.serializers.invite_serializer import InviteCreateSerializer
from typing import Any
from apps_config.url_constants import ENV_TO_DOMAIN_MAP
from apps_config.env_constants import CURRENT_ENV

from apps.team.models.team import Team


class InviteView(generics.GenericAPIView):
    queryset = InviteUserToTeam.objects.all()
    serializer_class = InviteCreateSerializer

    @validate_team
    def post(self, request: Request, *args: Any, team_obj: Team, **kwargs: Any) -> Response:
        print(request)
        serializer = self.get_serializer(team=team_obj, data=request.data)

        if not serializer.is_valid():
            return Response(data=serializer.errors)

        invite = serializer.create(serializer.validated_data)

        invite_id = {'inv_id': str(invite.id)}  # TODO: to be fixed
        invite_token = create_invite_token(invite_id)
        host = ENV_TO_DOMAIN_MAP[CURRENT_ENV]
        data = f'https://{host}/{invite_token}'

        return Response(data=data, status=200)
