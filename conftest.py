from typing import Any

import pytest
from django.test import TestCase


def _db_helper(request: Any, django_db_blocker: Any) -> None:
    django_db_blocker.unblock()
    test_case = TestCase(methodName="__init__")
    test_case._pre_setup()
    request.addfinalizer(django_db_blocker.restore)
    request.addfinalizer(test_case._post_teardown)


@pytest.fixture(scope='class')
def db_class(request: Any, django_db_blocker: Any) -> None:
    _db_helper(request, django_db_blocker)


@pytest.fixture(scope='module')
def db_module(request: Any, django_db_blocker: Any) -> None:
    _db_helper(request, django_db_blocker)


@pytest.fixture(scope='session')
def db_session(request: Any, django_db_blocker: Any) -> None:
    _db_helper(request, django_db_blocker)
