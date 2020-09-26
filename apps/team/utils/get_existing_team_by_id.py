from typing import Union
from uuid import UUID

from rest_framework.response import Response

from apps.team.models.team import Team


def get_existing_team_by_id(team_id: Union[str, UUID]) -> Union[Team, Response]:
    assert isinstance(team_id, str) or isinstance(team_id, UUID), f'{team_id} given'

    try:
        return Team.objects.get(id=team_id)
    except Team.DoesNotExist:
        return Response({"error_code": "Team does not exist"}, status=400)
