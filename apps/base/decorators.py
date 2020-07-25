from rest_framework.response import Response
from apps.base.constants import JWT_SECRET, JWT_ALGORITHM
from apps.user.models.user import User
from apps.team.models.team import Team
from rest_framework.request import Request
from apps.invite.models.invite_user_to_team import InviteUserToTeam
from typing import Any, TypeVar, Callable, cast
import functools
import jwt

TFunc = TypeVar('TFunc', bound=Callable)  # type: ignore


def login_required(func: TFunc) -> TFunc:
    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:

        request = args[1]
        assert isinstance(request, Request), f'{request} given'

        token = request.query_params.get('at')

        if not token:
            return Response({'Error': "Token not found"}, status=400)

        try:
            decoded_data = jwt.decode(token, JWT_SECRET, True, JWT_ALGORITHM)
            user = User.objects.get(id=decoded_data['id'])

            kwargs['user'] = user

        except User.DoesNotExist:
            return Response({'Error': "User not found"}, status=400)

        except jwt.DecodeError:
            return Response({"error_code": "INVALID_TOKEN"}, status=401)

        return func(*args, **kwargs)
    return cast(TFunc, wrapper)


def validate_invite(func: TFunc) -> TFunc:
    @login_required
    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:

        data = args[1].query_params
        invite_token = data['it']
        user = kwargs['user']

        try:
            decoded_data = jwt.decode(invite_token, JWT_SECRET, True, JWT_ALGORITHM)
            invite = InviteUserToTeam.objects.get(id=decoded_data['invite_id'])

        except jwt.DecodeError:
            return Response({"error_code": "INVALID_TOKEN"}, status=401)

        if user != invite.user:
            return Response({'Error': "WRONG_USER"}, status=403)

        if not invite.team.is_active:
            return Response({'Error': "Team doesn't exist"}, status=404)

        return func(*args, **kwargs)
    return cast(TFunc, wrapper)


def validate_team(func: TFunc) -> TFunc:
    @login_required
    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:

        request = args[1]
        assert isinstance(request, Request), f'{request} given'
        user_inviting = kwargs['user']
        team_id = kwargs['team_id']
        kwargs.pop('team_id', None)

        try:
            team = Team.objects.get(id=team_id)

            if not user_inviting.teams.filter(id=team.id).exists():
                return Response({'Error': "User is not in the team"}, status=403)

        except Team.DoesNotExist:
            return Response({'Error': "Team not found"}, status=400)

        kwargs['team_obj'] = team

        return func(*args, **kwargs)
    return cast(TFunc, wrapper)
