import pytest
import time
from .pages.product_page import ProductPage
 
@pytest.mark.need_review   
def test_guest_can_add_product_to_basket(browser):
   link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
   page = ProductPage(browser, link)
   page.open()
   page.should_not_be_success_message()
   page.add_to_basket()
   page.solve_quiz_and_get_code()
   page.should_be_message_about_product_added_to_basket()
   page.message_price_should_be_equal_to_basket_price()


@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                  pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",marks=pytest.mark.xfail),
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])

def test_guest_can_add_product_to_basket_parametrized(browser, link):
    link = f"{link}"
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    page.should_be_message_about_product_added_to_basket()
    page.message_price_should_be_equal_to_basket_price()
    
@pytest.mark.need_review
@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
   link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
   page = ProductPage(browser, link)
   page.open()
   page.add_to_basket()
   page.should_not_be_success_message()

@pytest.mark.need_review  
def test_guest_cant_see_success_message(browser):
   link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
   page = ProductPage(browser, link)
   page.open()
   page.should_not_be_success_message()
   
@pytest.mark.need_review
@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
   link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
   page = ProductPage(browser, link)
   page.open()
   page.add_to_basket()
   page.message_should_disappear()