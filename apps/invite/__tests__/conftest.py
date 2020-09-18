from typing import Any, Dict
from apps.user.models.user import User
from apps.team.models.team import Team
import pytest
from apps.user.utils.create_token import create_access_and_refresh_token

from django.core.management import call_command


@pytest.fixture(scope="session")
def django_db(django_db_setup: Any) -> None:
    call_command('loaddata', './test_invite.json')

#
# @pytest.fixture(scope="session")
# def user() -> User:
#     return User.objects.get(pk="cfc035db-abe8-4e87-97ed-f05dfa5a1d95")
#
#
# @pytest.fixture(scope="session")
# def team() -> Team:
#     return Team.objects.get(pk="9509f1da-214f-4e25-b310-914c8920521a")
#
#
# @pytest.fixture(scope="session")
# def user_token(user: User) -> str:
#     user_id = {'id': str(user.id)}
#     return create_access_and_refresh_token(user_id)['access_token']
