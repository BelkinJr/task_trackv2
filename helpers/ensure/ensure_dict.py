from typing import Any, Dict


def ensure_dict(some: Any) -> Dict[Any, Any]:
    assert isinstance(some, Dict), f'{some} is given'
    return some
