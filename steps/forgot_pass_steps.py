from behave import *


@when('forgot_pass: user enters email address in email input "{email}"')
def step_impl(context, email):
    context.forgot_pass_page.set_email(email)

@then('forgot_pass: verify that send email button is enabled')
def step_impl(context):
    context.forgot_pass_page.verify_btn_enabled()