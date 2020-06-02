import datetime
import uuid
from typing import Any, Dict
import jwt
from django.utils import timezone
from apps.base.constants import JWT_EXP_INVITE_SECONDS, JWT_SECRET, JWT_ALGORITHM


def create_invite_token(invite_id: Dict[str, str]) -> Dict[str, str]:

    expire_access_time = int(
        datetime.datetime.now(timezone.get_default_timezone()).timestamp()) + JWT_EXP_INVITE_SECONDS

    payload = dict(invite_id)

    payload.update(exp=str(expire_access_time))

    invite_token = jwt.encode(payload, JWT_SECRET, JWT_ALGORITHM, ).decode()

    return dict(invite_token=invite_token)
