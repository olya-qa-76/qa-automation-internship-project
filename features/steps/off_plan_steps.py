from behave import given, when, then


@then('Click on "Off-plan" at the left side menu')
def click_off_plan(context):
    context.app.main_page.click_off_plan()


@then('Verify the right page opens')
def verify_off_plan_opens(context):
    context.app.off_plan_page.verify_off_plan_opens()


@when('Filter by sale status of “Announced”')
def filter_by_announced(context):
    context.app.off_plan_page.filter_by_announced()


@then('Verify each product contains the Announced')
def verify_sale_status(context):
    context.app.off_plan_page.verify_announced()