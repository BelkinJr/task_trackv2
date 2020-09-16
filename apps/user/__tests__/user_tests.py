# import pytest
# from apps.user.models.user import User
# from django.urls import reverse
#
# @pytest.mark.django_db
#
#
# # @pytest.mark.django_db
# # def test_user_create():
# #     User.objects.create(username="test",
# #                         last_name="Testovich",
# #                         first_name="Test",
# #                         password="1234")
# #     assert User.objects.count() == 1
#
# @pytest.fixture
# def test_password():
#     return 'strong-test-pass'
#
# @pytest.fixture
# def create_user(db, django_user_model, test_password):
#     def make_user(**kwargs):
#         kwargs['password'] = test_password
#         return User.objects.create(**kwargs)
#     return make_user


