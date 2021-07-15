import random

from django.conf import settings

import factory
from factory.django import DjangoModelFactory


from home.models import (
    App,
    Plan,
    Subscription)

from users.factories import UserFactory


MIN_PRICE = 10
MAX_PRICE = 100


class FreePlanFactory(DjangoModelFactory):
    class Meta:
        model = Plan

    id = 1
    name = 'Free'
    description = 'Free plan'
    price = 0.0


class StandardPlanFactory(DjangoModelFactory):
    class Meta:
        model = Plan

    id = 2
    name = 'Standard'
    description = 'Standard plan'
    price = 10.0


class ProPlanFactory(DjangoModelFactory):
    class Meta:
        model = Plan

    id = 3
    name = 'Pro'
    description = 'Pro plan'
    price = 25.00


class WebAppFactory(DjangoModelFactory):
    class Meta:
        model = App

    name = factory.Faker('name')
    description = factory.Faker('text')
    type = 'Web'
    framework = 'Django'
    domain_name = factory.Faker('url')
    user = factory.SubFactory(UserFactory)


class MobileAppFactory(DjangoModelFactory):
    class Meta:
        model = App

    name = factory.Faker('name')
    description = factory.Faker('text')
    type = 'Mobile'
    framework = 'React Native'
    domain_name = factory.Faker('url')
    user = factory.SubFactory(UserFactory)