from pages.rst_pages import Authorization
from pages.locators import SmartHomeSearchLocator
from time import sleep

base_url = 'https://lk.smarthome.rt.ru/'


def test_authorization_form(browser):
    smart_home_web_page = Authorization(browser, base_url, SmartHomeSearchLocator)
    smart_home_web_page.go_to_site()
    sleep(5)
    smart_home_web_page.find_element(SmartHomeSearchLocator.go_with_password_button_locator).click()
    """Проверяем наличие основных элементов на странице:
        логотипа в шапке странице"""
    assert smart_home_web_page.find_element(SmartHomeSearchLocator.header_child_locator) == smart_home_web_page.find_element(
        SmartHomeSearchLocator.logo_locator)
    assert smart_home_web_page.find_element(SmartHomeSearchLocator.logo_text_locator).text == "Умный Дом\nРостелеком"
    """табов выбора типа аутентификации"""
    assert smart_home_web_page.find_element(SmartHomeSearchLocator.phone_tab_locator).text == "Телефон"
    assert smart_home_web_page.find_element(SmartHomeSearchLocator.email_tab_locator).text == "Почта"
    assert smart_home_web_page.find_element(SmartHomeSearchLocator.login_tab_locator).text == "Логин"
    """проверяем, что по умолчанию выбрат таб аутентификации по телефону"""
    assert "rt-tab--active" in smart_home_web_page.find_element(SmartHomeSearchLocator.phone_tab_locator).get_attribute("class")
    """проверяем наличие формы ввода 'Мобильный телефон'"""
    assert smart_home_web_page.find_element(SmartHomeSearchLocator.phone_field_locator).text == "Мобильный телефон"
    """проверяем наличие формы ввода 'Пароль'"""
    assert smart_home_web_page.find_element(SmartHomeSearchLocator.password_name_field_locator).text == "Пароль"
    """проверяем наличие кнопки 'Войти'"""
    assert smart_home_web_page.find_element(SmartHomeSearchLocator.login_button_locator).text == "Войти"
    """Проверяем наличие кнопки 'Войти по временному коду'"""
    assert smart_home_web_page.find_element(SmartHomeSearchLocator.login_otp_button_locator).text == "Войти по временному коду"
    """проверяем наличие ссылки на условия пользовательского соглашения"""
    assert smart_home_web_page.find_element(SmartHomeSearchLocator.user_agreement_link_locator).text == "пользовательского соглашения"
    """проверяем налчие ссылки на форму регистрации"""
    assert smart_home_web_page.find_element(SmartHomeSearchLocator.registration_link_locator).text == "Зарегистрироваться"
    """проверяем наличие вспомогательной информации в левой части страницы"""
    assert smart_home_web_page.find_element(SmartHomeSearchLocator.information_locator) == smart_home_web_page.find_element(
         SmartHomeSearchLocator.information_text_locator)


def test_authorization_with_otp_form(browser):
    smart_home_web_page = Authorization(browser, base_url, SmartHomeSearchLocator)
    smart_home_web_page.go_to_site()
    sleep(5)
    """Проверяем наличие основных элементов на странице:
               логотипа в шапке странице"""
    assert smart_home_web_page.find_element(SmartHomeSearchLocator.header_child_locator) == smart_home_web_page.find_element(
        SmartHomeSearchLocator.logo_locator)
    assert smart_home_web_page.find_element(SmartHomeSearchLocator.logo_text_locator).text == "Умный Дом\nРостелеком"
    """проверяем наличие формы ввода 'Мобильный телефон'"""
    assert smart_home_web_page.find_element(SmartHomeSearchLocator.login_field_text_locator).text == "Мобильный телефон"
    """проверяем наличие кнопки 'Получить код'"""
    assert smart_home_web_page.find_element(SmartHomeSearchLocator.otp_get_code_button_locator).text == "Получить код"
    """проверяем наличие кнопки 'Войти с паролем'"""
    assert smart_home_web_page.find_element(SmartHomeSearchLocator.go_with_password_button_locator).text == "Войти с паролем"
    """проверяем наличие вспомогательной информации в левой части страницы"""
    assert smart_home_web_page.find_element(SmartHomeSearchLocator.information_locator) == smart_home_web_page.find_element(
        SmartHomeSearchLocator.information_text_locator)


def test_registration_form(browser):
    smart_home_web_page = Authorization(browser, base_url, SmartHomeSearchLocator)
    smart_home_web_page.go_to_site()
    sleep(5)
    smart_home_web_page.find_element(SmartHomeSearchLocator.go_with_password_button_locator).click()
    smart_home_web_page.find_element(SmartHomeSearchLocator.registration_link_locator).click()
    """Проверяем наличие основных элементов на странице:
                логотипа в шапке странице"""
    assert smart_home_web_page.find_element(SmartHomeSearchLocator.header_child_locator) == smart_home_web_page.find_element(
        SmartHomeSearchLocator.logo_locator)
    assert smart_home_web_page.find_element(SmartHomeSearchLocator.logo_text_locator).text == "Умный Дом\nРостелеком"
    """проверяем наличие необходимых полей"""
    assert smart_home_web_page.find_element(SmartHomeSearchLocator.registration_name_field_locator).text == "Имя"
    assert smart_home_web_page.find_element(SmartHomeSearchLocator.registration_lastname_field_locator).text == "Фамилия"
    assert smart_home_web_page.find_element(SmartHomeSearchLocator.registration_region_field_locator).text == "Регион"
    assert smart_home_web_page.find_element(SmartHomeSearchLocator.registration_phone_field_locator).text == "Мобильный телефон"
    assert smart_home_web_page.find_element(
        SmartHomeSearchLocator.registration_password_field_locator).text == "Пароль"
    assert smart_home_web_page.find_element(
        SmartHomeSearchLocator.registration_repeat_password_field_locator).text == "Подтверждение пароля"
    """Проверяем наличие кнопки 'Зарегистрироваться'"""
    assert smart_home_web_page.find_element(
        SmartHomeSearchLocator.registration_button_locator).text == "Зарегистрироваться"
    """проверяем наличие ссылки на условия пользовательского соглашения"""
    assert smart_home_web_page.find_element(
        SmartHomeSearchLocator.user_agreement_link_locator).text == "пользовательского соглашения"
    """проверяем наличие логотипа и продуктового слогана в левой части страницы"""
    assert smart_home_web_page.find_element(SmartHomeSearchLocator.information_locator) == smart_home_web_page.find_element(
        SmartHomeSearchLocator.information_text_locator)


def test_forgot_password_form(browser):
    smart_home_web_page = Authorization(browser, base_url, SmartHomeSearchLocator)
    smart_home_web_page.go_to_site()
    sleep(5)
    smart_home_web_page.find_element(SmartHomeSearchLocator.go_with_password_button_locator).click()
    smart_home_web_page.find_element(SmartHomeSearchLocator.forgot_password_link_locator).click()
    """Проверяем наличие основных элементов на странице:
                логотипа в шапке странице"""
    assert smart_home_web_page.find_element(SmartHomeSearchLocator.header_child_locator) == smart_home_web_page.find_element(
        SmartHomeSearchLocator.logo_locator)
    assert smart_home_web_page.find_element(SmartHomeSearchLocator.logo_text_locator).text == "Умный Дом\nРостелеком"
    """табов выбора типа ввода контактных данных"""
    assert smart_home_web_page.find_element(SmartHomeSearchLocator.phone_tab_locator).text == "Телефон"
    assert smart_home_web_page.find_element(SmartHomeSearchLocator.email_tab_locator).text == "Почта"
    assert smart_home_web_page.find_element(SmartHomeSearchLocator.login_tab_locator).text == "Логин"
    """проверяем, что по умолчанию выбран таб 'Телефон'"""
    assert "rt-tab--active" in smart_home_web_page.find_element(SmartHomeSearchLocator.phone_tab_locator).get_attribute("class")
    """проверяем наличие необходимых полей"""
    assert smart_home_web_page.find_element(SmartHomeSearchLocator.phone_field_locator).text == "Мобильный телефон"
    assert smart_home_web_page.find_element(SmartHomeSearchLocator.captcha_field_locator).text == "Символы"
    """Проверяем наличие кнопки 'Продолжить'"""
    assert smart_home_web_page.find_element(SmartHomeSearchLocator.reset_button_locator).text == "Продолжить"
    """Проверяем наличие кнопки 'Вернуться назад'"""
    assert smart_home_web_page.find_element(SmartHomeSearchLocator.come_back_button_locator).text == "Вернуться назад"
