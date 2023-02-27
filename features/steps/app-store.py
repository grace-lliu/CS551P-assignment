from behave import given, when, then
import sqlite3

@given(u'the app store database is available')
def app_store_db_available(context):
    """
    Ensure that the app store database is available
    """
    conn = sqlite3.connect('app_store.db')
    context.cursor = conn.cursor()

@when(u'I navigate to the app details page with id {id}')
def navigate_to_app_details(context, id):
    """
    Navigate to the app details page for the specified id
    """
    context.browser.get(f'http://localhost:5000/detail/{id}')

@then(u'I should see the app details for id {id}')
def verify_app_details(context, id):
    """
    Verify that the app details for the specified id are displayed
    """
    expected_url = f'http://localhost:5000/detail/{id}'
    expected_name = context.cursor.execute(f"SELECT track_name, artist_name FROM app_store WHERE app_id = {id}").fetchone()
    expected_name = f"{expected_name[0]} {expected_name[1]}"

    assert context.browser.current_url == expected_url
    assert expected_name in context.browser.page_source

    context.cursor.close()
