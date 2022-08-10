# ----------------------------------------------------------------------------
# STEPS:
# ----------------------------------------------------------------------------
import requests
from requests.auth import HTTPBasicAuth

from behave   import given, when, then
from hamcrest import assert_that, equal_to, raises, calling

@given('a user with id = "{id}"')
def step_impl(context, id):
    context.auth = HTTPBasicAuth('super', 'super123')
    context.id = id

@when('the user is retrieved')
def step_impl(context):
    context.response = requests.get(f'http://localhost:8000/users/{context.id}/', auth=context.auth)

@then('the user name is "{name}"')
def step_impl(context, name):
    assert_that(context.response.ok, equal_to(True))
    assert_that(context.response.json()['username'], equal_to(name))