from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_empty_basket(self):
        assert self.is_not_element_present(
            *BasketPageLocators.PRODUCTS_IN_BASKET), "There are items in the basket"
    
    def should_be_empty_basket_text(self):
        assert self.is_element_present(
            *BasketPageLocators.EMPTY_BASKET_TEXT), "Text 'Your basket is empty' is not present"