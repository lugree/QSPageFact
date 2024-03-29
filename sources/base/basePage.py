from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage():
    def __init__(self, driver: webdriver):
        self.driver = driver

    def find_element(self, locator):
        if self.is_element_visible(locator):
            element = self.driver.find_element(*locator)
            return element
        else:
            print("Element not found")
            exit(5)

    def is_element_visible(self, locator):
        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
            return True
        except:
            return False


    def get_title(self):
        return self.driver.title

    def send_keys(self, element, text):
        element.clear()
        element.send_keys(text)
        pass

    def click(self, webelement):
        webelement.click()

    def drag_and_drop(self):
        pass

    def press_and_hold(self):
        pass

    def get_text(self):
        pass

    def clear_text(self, webelement):
        webelement.clear()

    def double_click(self):
        pass