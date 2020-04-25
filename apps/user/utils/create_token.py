import datetime
from typing import Any, Dict

import jwt
from django.utils import timezone

from apps.base.constants import JWT_SECRET, JWT_ALGORITHM, JWT_EXP_ACCESS_SECONDS, JWT_EXP_REFRESH_SECONDS


def create_access_and_refresh_token(kwargs: Any) -> Dict[str, str]:
    expire_access_time = int(
        datetime.datetime.now(timezone.get_default_timezone()).timestamp()) + JWT_EXP_ACCESS_SECONDS

    expire_refresh_time = int(
        datetime.datetime.now(timezone.get_default_timezone()).timestamp()) + JWT_EXP_REFRESH_SECONDS

    payload = kwargs

    payload.update(exp=str(expire_access_time))
    access_token = jwt.encode(payload, JWT_SECRET, JWT_ALGORITHM,).decode()

    payload.update(exp=str(expire_refresh_time))
    refresh_token = jwt.encode(payload, JWT_SECRET, JWT_ALGORITHM,).decode()

    return dict(access_token=access_token, refresh_token=refresh_token)
