from .base_page import BasePage
from .locators import LoginPageLocators

class LoginPage(BasePage):
    
    def register_new_user(self,email, password):
        email_input = self.browser.find_element(*LoginPageLocators.EMAIL_REG)
        email_input.send_keys(email)
        password_input = self.browser.find_element(*LoginPageLocators.PASSWORD_REG)
        password_input.send_keys(password)
        password_repeat = self.browser.find_element(*LoginPageLocators.PASSWORD_REG_REPEAT)
        password_repeat.send_keys(password)
        registr_button = self.browser.find_element(*LoginPageLocators.REGISTRATION_BUTTON)
        registr_button.click()
        
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_register_form()
        self.should_be_login_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "URL does not contain login substring"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"
        
    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_FORM), "Registration form is not presented"