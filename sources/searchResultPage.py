from sources.navigationBar import NavigationBar
from selenium import webdriver
from selenium.webdriver.common.by import By

class SearchResultPage():

    def __init__(self, driver):
        self.driver = driver
        self.firstItemLocator = (By.XPATH, "[//*[@class='a-size-medium a-color-base a-text-normal']][1]")
        self.addToCartLocator = (By.ID, "add-to-cart-button")

    def choose_first_item(self):
        chooseFirstElement = self.driver.find_element(*self.firstItemLocator)
        chooseFirstElement.click()

    def add_To_cart(self):
        addToCartButton = self.driver.find_element(*self.addToCartLocator)
        addToCartButton.click()





