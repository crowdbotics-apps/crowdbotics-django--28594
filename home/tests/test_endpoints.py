import json
import pytest
# import factory
from django.urls import reverse
from rest_framework import status

from home.api.v1.serializers import AppSerializer

pytestmark = pytest.mark.django_db


class TestPlanAPITestCase:
    def test_plan_list(self, client, free_plan, standard_plan, pro_plan):
        url = reverse('plan-list')
        response = client.get(url)
        assert response.status_code == status.HTTP_200_OK
        assert len(response.json()) == 3

    def test_free_plan_detail(self, client, free_plan):
        url = reverse('plan-detail', args=[free_plan.id])
        response = client.get(url)
        assert response.status_code == status.HTTP_200_OK
        plan = response.json()
        assert plan['id'] == free_plan.id
        assert plan['name'] == free_plan.name
        assert plan['description'] == free_plan.description
        assert float(plan['price']) == free_plan.price

    def test_standard_plan_detail(self, client, standard_plan):
        url = reverse('plan-detail', args=[standard_plan.id])
        response = client.get(url)
        assert response.status_code == status.HTTP_200_OK
        plan = response.json()
        assert plan['id'] == standard_plan.id
        assert plan['name'] == standard_plan.name
        assert plan['description'] == standard_plan.description
        assert float(plan['price']) == standard_plan.price

    def test_pro_plan_detail(self, client, pro_plan):
        url = reverse('plan-detail', args=[pro_plan.id])
        response = client.get(url)
        assert response.status_code == status.HTTP_200_OK
        plan = response.json()
        assert plan['id'] == pro_plan.id
        assert plan['name'] == pro_plan.name
        assert plan['description'] == pro_plan.description
        assert float(plan['price']) == pro_plan.price


class TestAppAPITestCase:

    #  Unauthenticated Action
    def test_unauthenticated_app_list(self, client):
        url = reverse('app-list')
        response = client.get(url)
        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_unauthenticated_app_creation(self, client, web_app):
        url = reverse('app-list')
        data = AppSerializer(web_app).data
        data.pop('user')
        screenshot = data.pop('screenshot')
        response = client.post(url, data=data)
        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_unauthenticated_app_detail(self, client, web_app):
        url = reverse('app-detail', args=[web_app.id])
        response = client.get(url)
        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    #  Authenticated Action
    def test_app_list(self, auto_login_user, web_app):
        client, user = auto_login_user()
        url = reverse('app-list')
        response = client.get(url)
        assert response.status_code == status.HTTP_200_OK

    def test_creating_web_app(self, auto_login_user, web_app):
        client, user = auto_login_user()
        url = reverse('app-list')
        data = AppSerializer(web_app).data
        # TODO: test screenshot
        screenshot = data.pop('screenshot')
        response = client.post(url, data=data)
        assert response.status_code == status.HTTP_201_CREATED
        app = response.json()
        assert app['name'] == web_app.name
        assert app['description'] == web_app.description
        assert app['type'] == web_app.type
        assert app['framework'] == web_app.framework
        assert app['domain_name'] == web_app.domain_name
        assert app['user'] == user.id

    def test_web_app_detail(self, auto_login_user, web_app):
        client, user = auto_login_user()
        url = reverse('app-detail', args=[web_app.id])
        response = client.get(url)
        assert response.status_code == status.HTTP_200_OK
        res = response.json()
        assert res['id'] == web_app.id
        assert res['name'] == web_app.name
        assert res['description'] == web_app.description
        assert res['type'] == web_app.type
        assert res['framework'] == web_app.framework
        assert res['domain_name'] == web_app.domain_name