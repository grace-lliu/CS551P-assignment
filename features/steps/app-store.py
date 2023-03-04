from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

@given('the app store page is available')
def step_impl(context):
    context.browser = webdriver.Chrome()
    context.browser.get('https://colorexotic-italianspeed-5000.codio-box.uk')

@when('I navigate to the app details page with id "{app_id}"')
def step_impl(context, app_id):
    context.browser.get(f'https://colorexotic-italianspeed-5000.codio-box.uk/detail/{app_id}')

@then('the URL should include the app ID')
def step_impl(context):
    assert 'detail/281656475' in context.browser.current_url


