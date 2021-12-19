from selenium.webdriver.common.by import By
from time import sleep
from browser import Browser


class ForgotPassPage(Browser):
    # definim locator pt elemente
    FORGOT_EMAIL_INPUT = '//*[@placeholder="Enter your email"]'
    SEND_EMAIL_BTN = '//*[text()="Send email"]/parent::button'

    # small steps (cei mai mici pasi posibili, in jurul unui singur element)
    def navigate_to_forgot_pass_page(self):
        self.driver.get('https://jules.app/forgot-password')

    def set_email(self, email):
        sleep(1)
        email_input = self.driver.find_element(By.XPATH, self.FORGOT_EMAIL_INPUT)
        email_input.send_keys(email)

    def verify_btn_enabled(self):
        assert self.driver.find_element(By.XPATH, self.SEND_EMAIL_BTN).is_enabled() is True



