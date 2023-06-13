from selenium.webdriver.common.by import By


class ProductDetails():
    def __init__(self, driver):
        self.driver = driver
        self.addToCartButton = (By.ID, "add-to-cart-button")

    def click_to_cart_button(self):
        clickToCartButton = self.driver.find_element(*self.addToCartButton)
        clickToCartButton.click()
