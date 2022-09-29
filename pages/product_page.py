from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def add_to_basket(self):
        add_to_basket_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        add_to_basket_button.click()
        
    def should_be_message_about_product_added_to_basket(self):
        product_title = self.browser.find_element(*ProductPageLocators.PRODUCT_TITLE).text
        product_add_to_basket_title = self.browser.find_element(*ProductPageLocators.PRODUCT_ADD_MESSAGE).text
        assert product_title == product_add_to_basket_title, f"Product is not added to basket"
        
    def message_price_should_be_equal_to_basket_price(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        basket_price = self.browser.find_element(*ProductPageLocators.BASKET_ADD_PRICE).text
        assert product_price == basket_price, "Basket cost does not match the product price"