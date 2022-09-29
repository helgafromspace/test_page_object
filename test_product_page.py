import pytest
import time
from .pages.product_page import ProductPage

def test_guest_can_add_product_to_basket(browser):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    page.should_be_message_about_product_added_to_basket()
    page.message_price_should_be_equal_to_basket_price()
  