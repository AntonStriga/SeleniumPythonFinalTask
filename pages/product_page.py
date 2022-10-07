from .base_page import BasePage
from .locators import ProductsPageLocators


class ProductPage(BasePage):
    def add_product_to_basket(self):
        self.click_on_element(*ProductsPageLocators.ADD_TO_BASKET_BUTTON)

    def get_product_name(self):
        return self.get_element_text(*ProductsPageLocators.MAIN_PRODUCT_NAME)

    def get_product_price(self):
        return self.get_element_text(*ProductsPageLocators.MAIN_PRODUCT_PRICE)

    def should_be_added_product_name(self, name):
        assert name == self.get_element_text(*ProductsPageLocators.ALERT_SUCCESS), "Added product name is wrong"

    def should_be_added_product_price(self, price):
        assert price == self.get_element_text(*ProductsPageLocators.BASKET_TOTAL_SUM), "Added product price is wrong"
