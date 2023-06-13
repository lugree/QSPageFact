from selenium.webdriver.common.by import By

class NavigationBar():
    def __init__(self, driver):
        self.driver = driver
        self.fillSearchFieldLocator = (By.ID, "twotabsearchtextbox")
        self.searchButtonElementLocator = (By.ID, "nav-search-submit-button")
        self.cartButtonLocator = (By.ID, "nav-cart-count")

    def fill_search_field(self, searchElement):
        fillsearchFieldElement = self.driver.find_element(*self.fillSearchFieldLocator)
        fillsearchFieldElement.clear()
        fillsearchFieldElement.send_keys(searchElement)

    def click_to_search_button(self):
        clickSearchButton = self.driver.find_element(*self.searchButtonElementLocator)
        clickSearchButton.click()

    def click_to_home_page_button(self):
        pass