import pytest
from urllib.parse import urlencode

from django.test import Client
from django.urls import reverse


@pytest.mark.django_db
class TestInvite:
    def test_generate_invite(self, client: Client, user, user_token, team):
        url = f"{reverse('generate_invite', kwargs={'team_id': team.id})}?{urlencode({'at': user_token})}"
        response = client.post(path=url, data={"payload": {"user": "11814d18-4e8d-45b6-b9c9-f08577d731eb"}})
        assert response.status_code == 200
