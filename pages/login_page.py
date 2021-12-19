from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from browser import Browser

#design pattern = page object model (POM)
#fiecare pagina din website are o clasa dedicata cu elemenetele din pagina


class LoginPage(Browser):
    # definim locator pt elemente
    USER = '//input[@placeholder="Enter your email"]'
    PASS = '//*[@placeholder="Enter your password"]'
    LOGIN = '//button[@data-test-id="login-button"]'
    INVALID_LOGIN_ERROR = '//span[text()="Invalid email/password combination"]'
    FORGOT_PASS_BTN = '//*[text()="Forgot password?"]'

    # small steps (cei mai mici pasi posibili, in jurul unui singur element)
    def navigate_to_jules(self):
        self.driver.get('https://jules.app/sign-in')

    def get_page_title(self):
        return self.driver.title

    def set_username(self, username):
        sleep(1)
        user_name_field = self.driver.find_element(By.XPATH, self.USER)
        user_name_field.send_keys(username)

    def set_password(self, password):
        # explicit wait example
        # selenium will wait for element to be loaded before taking next action
        # mai profi decat sleep
        password_field = WebDriverWait(self.driver, 5000).until(EC.presence_of_element_located((By.XPATH, self.PASS)))
        password_field.send_keys(password)

    def click_login(self):
        self.driver.find_element(By.XPATH, self.LOGIN).click()

    def click_forgot_pass_btn(self):
        self.driver.find_element(By.XPATH, self.FORGOT_PASS_BTN).click()

    def verify_error_displayed(self):
        assert self.driver.find_element(By.XPATH, self.INVALID_LOGIN_ERROR).is_displayed() is True

    # step definition (agregare de pasi mici, care au logica sa fie sub o singura umbrela)
    def login(self, username, password):
        self.set_username(username)
        self.set_password(password)
        self.click_login()