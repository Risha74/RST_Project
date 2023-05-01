
from pages.base_page import BasePage


class Authorization(BasePage):
    def enter_email(self, search_locator, email):
        search_field_email = self.find_element(search_locator.email_field_locator)
        search_field_email.click()
        search_field_email.clear()
        search_field_email.send_keys(email)
        return search_field_email

    def enter_password(self, search_locator, password):
        search_field_pass = self.find_element(search_locator.password_field_locator)
        search_field_pass.click()
        search_field_pass.clear()
        search_field_pass.send_keys(password)
        return search_field_pass

    def clik_on_login_button(self, search_locator):
        return self.find_element(search_locator.login_button_locator).click()







