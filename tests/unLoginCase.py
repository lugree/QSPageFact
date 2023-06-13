import unittest
from selenium import webdriver
from sources.cartPage import CartPage
from sources.navigationBar import NavigationBar
from sources.searchResultPage import SearchResultPage

from sources.searchResultPage import SearchResultPage
from sources.product_detail_page import ProductDetails

class TestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://cutt.ly/r6vrJzd")

    def test_unlogin(self):
        self.navigationObject = NavigationBar(webdriver.Chrome())
        self.navigationObject.fill_search_field("basketball ball")

        self.searchResultObject = SearchResultPage()
        self.searchResultObject.choose_first_item()
        self.searchResultObject.add_To_cart()



        self.cartPage = CartPage(self.driver)
        self.cartPage.go_to_cart()
        self.cartPage.delete_first_button_element_from_cart()

    def tearDown(self) -> None:
        self.driver.close()
