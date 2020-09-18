import pytest
from urllib.parse import urlencode, quote_plus
from django.urls import reverse
from apps.base.constants import API_URL
from ...team.models import Team
from ...user.models import User
from ...user.utils.create_token import create_access_and_refresh_token


@pytest.mark.django_db
class TestInvite:
    def test_generate_invite(client, django_db_setup):
        user = User.objects.get(pk="cfc035db-abe8-4e87-97ed-f05dfa5a1d95")
        user_id = {'id': str(user.id)}
        at_token = create_access_and_refresh_token(user_id)['access_token']
        # at_token = user_token
        params = {"at": at_token}
        team = Team.objects.get(pk="9509f1da-214f-4e25-b310-914c8920521a")
        result = urlencode(params, quote_via=quote_plus)
        url = reverse(f'{API_URL}/teams/<uuid:team_id>/generate_invite/?{result}', kwargs={"team": team.id})
        response = client.get(url, {"user": "11814d18-4e8d-45b6-b9c9-f08577d731eb"})
        assert response.status_code == 200
