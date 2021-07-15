import uuid

import pytest
from rest_framework.test import APIClient
from pytest_factoryboy import register

from home.tests.factories import (
    FreePlanFactory,
    StandardPlanFactory,
    ProPlanFactory,
    WebAppFactory,
    MobileAppFactory)


register(FreePlanFactory)
register(StandardPlanFactory)
register(ProPlanFactory)
register(WebAppFactory)
register(MobileAppFactory)


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def test_password():
    return 'test-pass'


@pytest.fixture
def create_user(django_user_model, test_password):
    def make_user(**kwargs):
        kwargs['password'] = test_password
        if 'username' not in kwargs:
            kwargs['username'] = str(uuid.uuid4())
        return django_user_model.objects.create_user(**kwargs)
    return make_user

@pytest.fixture
def auto_login_user(client, create_user, test_password):
    def make_auto_login(user=None):
        if user is None:
            user = create_user()
        client.login(username=user.username, password=test_password)
        return client, user
    return make_auto_login


@pytest.fixture
def authenticated_client(create_user, api_client):
    user = create_user()
    api_client.force_authenticate(user=user)
    yield api_client
    api_client.force_authenticate(user=None)


@pytest.fixture()
def free_plan(free_plan_factory):
    return free_plan_factory()


@pytest.fixture()
def standard_plan(standard_plan_factory):
    return standard_plan_factory()


@pytest.fixture()
def pro_plan(pro_plan_factory):
    return pro_plan_factory()


@pytest.fixture()
def web_app(web_app_factory):
    return web_app_factory()


@pytest.fixture()
def mobile_app(mobile_app_factory):
    return mobile_app_factory()