from pages.rst_pages import Authorization
from pages.locators import KeySearchLocator

base_url = 'https://key.rt.ru/'


def test_authorization_form(browser):
    key_web_page = Authorization(browser, base_url, KeySearchLocator)
    key_web_page.go_to_site()
    key_web_page.find_element(KeySearchLocator.go_to_cabinet_link_locator).click()
    key_web_page.find_element(KeySearchLocator.go_with_password_button_locator).click()
    """Проверяем наличие основных элементов на странице:
           логотипа в шапке странице"""
    assert key_web_page.find_element(KeySearchLocator.header_child_locator) == key_web_page .find_element(
        KeySearchLocator.logo_locator)
    assert key_web_page.find_element(KeySearchLocator.logo_text_locator).text == "Ростелеком Ключ"
    """табов выбора типа аутентификации"""
    assert key_web_page.find_element(KeySearchLocator.phone_tab_locator).text == "Телефон"
    assert key_web_page.find_element(KeySearchLocator.email_tab_locator).text == "Почта"
    assert key_web_page.find_element(KeySearchLocator.login_tab_locator).text == "Логин"
    """проверяем, что по умолчанию выбрат таб аутентификации по телефону"""
    assert "rt-tab--active" in key_web_page.find_element(KeySearchLocator.phone_tab_locator).get_attribute("class")
    """проверяем наличие формы ввода 'Мобильный телефон'"""
    assert key_web_page.find_element(KeySearchLocator.phone_field_locator).text == "Мобильный телефон"
    """проверяем наличие формы ввода 'Пароль'"""
    assert key_web_page.find_element(KeySearchLocator.password_name_field_locator).text == "Пароль"
    """проверяем наличие кнопки 'Войти'"""
    assert key_web_page.find_element(KeySearchLocator.login_button_locator).text == "Войти"
    """Проверяем наличие кнопки 'Войти по временному коду'"""
    assert key_web_page.find_element(KeySearchLocator.login_otp_button_locator).text == "Войти по временному коду"
    """проверяем наличие ссылки на условия пользовательского соглашения"""
    assert key_web_page.find_element(KeySearchLocator.user_agreement_link_locator).text == "пользовательского соглашения"
    """проверяем налчие ссылки на форму регистрации"""
    assert key_web_page.find_element(KeySearchLocator.registration_link_locator).text == "Зарегистрироваться"
    """проверяем наличие вспомогательной информации в левой части страницы"""
    assert key_web_page.find_element(KeySearchLocator.information_locator) == key_web_page.find_element(
         KeySearchLocator.information_text_locator)


def test_authorization_with_otp_form(browser):
    key_web_page = Authorization(browser, base_url, KeySearchLocator)
    key_web_page.go_to_site()
    key_web_page.find_element(KeySearchLocator.go_to_cabinet_link_locator).click()
    """Проверяем наличие основных элементов на странице:
                   логотипа в шапке странице"""
    assert key_web_page.find_element(KeySearchLocator.header_child_locator) == key_web_page.find_element(
        KeySearchLocator.logo_locator)
    assert key_web_page.find_element(KeySearchLocator.logo_text_locator).text == "Ростелеком Ключ"
    """проверяем наличие формы ввода 'E-mail или мобильный телефон'"""
    assert key_web_page.find_element(KeySearchLocator.login_field_text_locator).text == "E-mail или мобильный телефон"
    """проверяем наличие кнопки 'Получить код'"""
    assert key_web_page.find_element(KeySearchLocator.otp_get_code_button_locator).text == "Получить код"
    """проверяем наличие кнопки 'Войти с паролем'"""
    assert key_web_page.find_element(KeySearchLocator.go_with_password_button_locator).text == "Войти с паролем"
    """проверяем наличие вспомогательной информации в левой части страницы"""
    assert key_web_page.find_element(KeySearchLocator.information_locator) == key_web_page.find_element(
        KeySearchLocator.information_text_locator)


def test_registration_form(browser):
    key_web_page = Authorization(browser, base_url, KeySearchLocator)
    key_web_page.go_to_site()
    key_web_page.find_element(KeySearchLocator.go_to_cabinet_link_locator).click()
    key_web_page.find_element(KeySearchLocator.go_with_password_button_locator).click()
    key_web_page.find_element(KeySearchLocator.registration_link_locator).click()
    """Проверяем наличие основных элементов на странице:
                       логотипа в шапке странице"""
    assert key_web_page.find_element(KeySearchLocator.header_child_locator) == key_web_page.find_element(
        KeySearchLocator.logo_locator)
    assert key_web_page.find_element(KeySearchLocator.logo_text_locator).text == "Ростелеком Ключ"
    """проверяем наличие необходимых полей"""
    assert key_web_page.find_element(KeySearchLocator.registration_name_field_locator).text == "Имя"
    assert key_web_page.find_element(KeySearchLocator.registration_lastname_field_locator).text == "Фамилия"
    assert key_web_page.find_element(KeySearchLocator.registration_region_field_locator).text == "Регион"
    assert key_web_page.find_element(
        KeySearchLocator.registration_email_or_phone_field_locator).text == "E-mail или мобильный телефон"
    assert key_web_page.find_element(
        KeySearchLocator.registration_password_field_locator).text == "Пароль"
    assert key_web_page.find_element(
        KeySearchLocator.registration_repeat_password_field_locator).text == "Подтверждение пароля"
    """Проверяем наличие кнопки 'Зарегистрироваться'"""
    assert key_web_page.find_element(
        KeySearchLocator.registration_button_locator).text == "Зарегистрироваться"
    """проверяем наличие ссылки на условия пользовательского соглашения"""
    assert key_web_page.find_element(
        KeySearchLocator.user_agreement_link_locator).text == "пользовательского соглашения"
    """проверяем наличие логотипа и продуктового слогана в левой части страницы"""
    assert key_web_page.find_element(KeySearchLocator.information_locator) == key_web_page.find_element(
        KeySearchLocator.information_text_locator)


def test_forgot_password_form(browser):
    key_web_page = Authorization(browser, base_url, KeySearchLocator)
    key_web_page.go_to_site()
    key_web_page.find_element(KeySearchLocator.go_to_cabinet_link_locator).click()
    key_web_page.find_element(KeySearchLocator.go_with_password_button_locator).click()
    key_web_page.find_element(KeySearchLocator.forgot_password_link_locator).click()
    """Проверяем наличие основных элементов на странице:
                логотипа в шапке странице"""
    assert key_web_page.find_element(KeySearchLocator.header_child_locator) == key_web_page.find_element(
        KeySearchLocator.logo_locator)
    assert key_web_page.find_element(KeySearchLocator.logo_text_locator).text == "Ростелеком Ключ"
    """табов выбора типа ввода контактных данных"""
    assert key_web_page.find_element(KeySearchLocator.phone_tab_locator).text == "Телефон"
    assert key_web_page.find_element(KeySearchLocator.email_tab_locator).text == "Почта"
    assert key_web_page.find_element(KeySearchLocator.login_tab_locator).text == "Логин"
    """проверяем, что по умолчанию выбран таб 'Телефон'"""
    assert "rt-tab--active" in key_web_page.find_element(KeySearchLocator.phone_tab_locator).get_attribute("class")
    """проверяем наличие необходимых полей"""
    assert key_web_page.find_element(KeySearchLocator.phone_field_locator).text == "Мобильный телефон"
    assert key_web_page.find_element(KeySearchLocator.captcha_field_locator).text == "Символы"
    """Проверяем наличие кнопки 'Продолжить'"""
    assert key_web_page.find_element(KeySearchLocator.reset_button_locator).text == "Продолжить"
    """Проверяем наличие кнопки 'Вернуться назад'"""
    assert key_web_page.find_element(KeySearchLocator.come_back_button_locator).text == "Вернуться назад"
