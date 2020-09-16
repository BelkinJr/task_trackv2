import pytest
from urllib.parse import urlencode, quote_plus
from django.urls import reverse
from apps.base.constants import API_URL


@pytest.mark.db
class TestInvite:
    def test_generate_invite(client, team, user_token):
        at_token = user_token
        params = {"at": at_token}
        result = urlencode(params, quote_via=quote_plus)
        url = reverse(f'{API_URL}/teams/<uuid:team_id>/generate_invite/?{result}', kwargs={"team": team.id})
        response = client.get(url, {"user": "11814d18-4e8d-45b6-b9c9-f08577d731eb"})
        assert response.status_code == 200
