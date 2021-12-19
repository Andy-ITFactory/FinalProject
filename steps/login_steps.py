from behave import *

# given!, when!, and, but, then! - sintaxa gherkin
# given - seteaza situatia initiala
# when - pasii din test
# then - verificarea din test

@given('login: user is on the login page')
def step_impl(context):
    context.login_page.navigate_to_jules()

# username password parameters are set in login.feature
@when('login: user enters valid username "{username}" and valid password "{password}"')
def step_impl(context, username, password):
    context.login_page.login(username, password)

@when('login: user clicks on forgot pass button')
def step_impl(context):
    context.login_page.click_forgot_pass_btn()

@then('login: verify that invalid credentials error is displayed')
def step_impl(context):
    context.login_page.verify_error_displayed()


