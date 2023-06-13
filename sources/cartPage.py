from selenium import webdriver
from selenium.webdriver.common.by import By
from sources.base.basePage import BasePage

class CartPage(BasePage):

    def __init__(self, driver: webdriver.Chrome):
        BasePage.__init__(self.driver)
        self.driver = driver
        self.deletefirstElementFromCartLocator = (By.XPATH, "//*[@class='a-color-link'][1]")
        self.goToCartLocator = (By.ID, "sw-gtc")

    def go_to_cart(self):
        goToCartButton = self.driver.find_element(*self.goToCartLocator)
        goToCartButton.click()


    def delete_first_button_element_from_cart(self):
        #deleteFirstElement = self.driver.find_element(*self.deletefirstElementFromCartLocator)
        deleteFirstElement = self.find_element(self.deletefirstElementFromCartLocator)
        self.click(deleteFirstElement)
        #deleteFirstElement.click()





