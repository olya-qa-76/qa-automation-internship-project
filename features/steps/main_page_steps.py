from behave import given, when, then


@given('Open the main page')
def open_main_page(context):
    context.app.base_page.open_url()


@when('Log in to the page with email: "{valid_email}" and password: "{valid_password}"')
def login(context, valid_email, valid_password):
    context.app.sign_in_page.login(valid_email, valid_password)