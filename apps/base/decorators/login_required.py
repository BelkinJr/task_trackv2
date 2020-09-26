from rest_framework.response import Response
from apps.base.constants import JWT_SECRET, JWT_ALGORITHM
from apps.user.models.user import User
from rest_framework.request import Request
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
