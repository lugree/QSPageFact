import unittest
from selenium import webdriver
from sources.loginPage import LoginPage
from sources.cartPage import CartPage
from sources.navigationBar import NavigationBar
import time

class TestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        #self.driver.delete_cookie(self)
        self.driver.maximize_window()
        self.driver.get("https://cutt.ly/r6vrJzd")
        self.logInPage = LoginPage(self.driver)

    def test_login_test(self):
        self.logInPage.fill_user_name_field("lgrigoryan48@yahoo.com")
        self.logInPage.prss_to_continue()

        self.logInPage.fill_password_field("lugree0813")
        self.logInPage.press_to_sign_in_button()

        #assert self.get_incorrect_password_error_massage == "Your password is incorrect"




    def tearDown(self) -> None:
        self.driver.close()
