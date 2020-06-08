from typing import Dict
import jwt
from apps.base.constants import JWT_SECRET, JWT_ALGORITHM


def create_invite_token(invite_id: Dict[str, str]) -> Dict[str, str]:

    payload = dict(invite_id)

    invite_token = jwt.encode(payload, JWT_SECRET, JWT_ALGORITHM, ).decode()

    return dict(invite_token=invite_token)
