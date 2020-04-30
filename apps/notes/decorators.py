import jwt
from rest_framework.response import Response
from apps.base.constants import JWT_SECRET, JWT_ALGORITHM
from apps.user.models.user import User


def login_required(func):

    def wrapper(self, request, *args, **kwargs):

        data = request.data['payload']
        token = data['at']
        try:
            decoded_data = jwt.decode(token, JWT_SECRET, JWT_ALGORITHM)
            user = User.objects.get(id=decoded_data['id'])

            kwargs['user'] = user

        except User.DoesNotExist:
            return Response({'Error': "User not found"}, status=400)

        except jwt.DecodeError:
            return Response({"error_code": "INVALID_TOKEN"}, status=401)

        return func(self, request, *args, **kwargs)
    return wrapper
