from selenium.webdriver.common.by import By
from sources.base.basePage import BasePage

class LoginPage(BasePage):

    def __init__(self, driver):
        BasePage.__init__(self, driver)
        self.driver = driver
        self.userNameFieldLocator = (By.ID, "ap_email")
        self.continueButtonLocator = (By.ID, "continue")
        self.passwordFieldLocator = (By.ID, "ap_password")
        self.signInButtonLocator = (By.ID, "signInSubmit")
        self.incorrectPasswordMassageLocator = (By.CLASS_NAME, "a-list-item")


    def fill_user_name_field(self, username):
        #userNameFieldElement = self.driver.find_element(*self.userNameFieldLocator)
        userNameFieldElement = self.find_element(self.userNameFieldLocator)
        self.send_keys(userNameFieldElement, username)
        # userNameFieldElement.clear()
        # userNameFieldElement.send_keys(username)

    def prss_to_continue(self):
        #continueButtonElement = self.driver.find_element(*self.continueButtonLocator )
        continueButtonElement = self.find_element(self.continueButtonLocator)
        self.click(continueButtonElement)
        #continueButtonElement.click()

    def fill_password_field(self, password):
        #passwordFieldElement = self.driver.find_element(*self.passwordFieldLocator)
        passwordFieldElement = self.find_element(self.passwordFieldLocator)
        self.send_keys(passwordFieldElement, password)
        # passwordButton.clear()
        # passwordButton.send_keys(password)

    def press_to_sign_in_button(self):
        #signInButtonElement = self.driver.find_element(*self.signInButtonLocator)
        signInButtonElement = self.find_element(self.signInButtonLocator)
        self.click(signInButtonElement)
        #signInButtonElement.click()

    def check_keep_me_signiedin_button(self):
        pass

    def get_incorrect_password_error_massage(self):
        incorrectPasswordMassageElement = self.driver.find_element(*self.incorrectPasswordMassageLocator)
        massage = incorrectPasswordMassageElement.text
        return massage


