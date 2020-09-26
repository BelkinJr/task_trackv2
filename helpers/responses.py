from rest_framework import status
from rest_framework.response import Response
from typing import Any, Optional, Dict


def create_response_data(result: Any,
                         status_code: status,
                         items_total_count: Optional[int] = None,
                         items_count: Optional[int] = None,) -> Dict[str, Any]:

    data = {'result': result,
            'status_code': status_code,
            'items_total_count': items_total_count,
            'items_count': items_count}
    return data


class CreatedStdResponse(Response):
    def __init__(
        self,
        data: Any,
        items_total_count: Optional[int] = None,
        items_count: Optional[int] = None,
    ) -> None:
        super().__init__(
            status=status.HTTP_201_CREATED,
            data=create_response_data(
                result=data,
                status_code=status.HTTP_201_CREATED,
                items_total_count=items_total_count,
                items_count=items_count
            )
        )
