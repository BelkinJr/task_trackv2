from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.request import Request
from apps.invite.models.invite import Invite
from apps.user.models.user import User
from apps.base.decorators import login_required
from apps.invite.utils.create_invite_token import create_invite_token
from apps.invite.serializers.invite_serializer import InviteCreateSerializer
from typing import Any


class InviteView(generics.GenericAPIView):
    queryset = Invite.objects.all()
    serializer_class = InviteCreateSerializer

    @login_required
    def post(self, request: Request, *args: Any, user: User, **kwargs: Any) -> Response:
        team = request.data['payload'].get['team']
        if team not in user.teams.all():
            return Response({'Error': "Cannot generate invite if not in the team"}, status=403)
        serializer = self.get_serializer(data=request.data)
        if not serializer.is_valid():
            return Response(data=serializer.errors)
        invite = serializer.create(serializer.validated_data)
        invite_id = {'inv_id': str(invite.id)}
        invite_token = create_invite_token(invite_id)
        return Response(data=invite_token, status=200)
