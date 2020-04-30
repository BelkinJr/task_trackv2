from typing import Any, Dict


class GenericSerializerMixin:

    @staticmethod
    def transform_input(data: Dict[str, Any]) -> Dict[str, Any]:
        data = data.get('payload')
        return data

    @staticmethod
    def lowercase(string: str) -> str:
        return string.lower()
