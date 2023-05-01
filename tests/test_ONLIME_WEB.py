from pages.rst_pages import Authorization
from pages.locators import OnlimeSearchLocator
from time import sleep

base_url = 'https://my.rt.ru/'


def test_authorization_form(browser):
    onlime_web_page = Authorization(browser, base_url, OnlimeSearchLocator)
    onlime_web_page.go_to_site()
    sleep(5)
    onlime_web_page.find_element(OnlimeSearchLocator.go_with_password_button_locator).click()
    """Проверяем наличие основных элементов на странице:
       логотипа в шапке странице"""
    assert onlime_web_page.find_element(OnlimeSearchLocator.header_child_locator) == onlime_web_page.find_element(
        OnlimeSearchLocator.logo_locator)
    """табов выбора типа аутентификации"""
    assert onlime_web_page.find_element(OnlimeSearchLocator.phone_tab_locator).text == "Телефон"
    assert onlime_web_page.find_element(OnlimeSearchLocator.email_tab_locator).text == "Почта"
    assert onlime_web_page.find_element(OnlimeSearchLocator.login_tab_locator).text == "Логин"
    """проверяем, что по умолчанию выбрат таб аутентификации по телефону"""
    assert "rt-tab--active" in onlime_web_page.find_element(OnlimeSearchLocator.phone_tab_locator).get_attribute("class")
    """проверяем наличие формы ввода 'Мобильный телефон'"""
    assert onlime_web_page.find_element(OnlimeSearchLocator.phone_field_locator).text == "Мобильный телефон"
    """проверяем наличие формы ввода 'Пароль'"""
    assert onlime_web_page.find_element(OnlimeSearchLocator.password_name_field_locator).text == "Пароль"
    """проверяем наличие кнопки 'Войти'"""
    assert onlime_web_page.find_element(OnlimeSearchLocator.login_button_locator).text == "Войти"
    """Проверяем наличие кнопки 'Войти по временному коду'"""
    assert onlime_web_page.find_element(OnlimeSearchLocator.login_otp_button_locator).text == "Войти по временному коду"
    """проверяем наличие ссылки на условия пользовательского соглашения"""
    assert onlime_web_page.find_element(OnlimeSearchLocator.user_agreement_link_locator).text == "пользовательского соглашения"
    """проверяем наличие вспомогательной информации в левой части страницы"""
    assert onlime_web_page.find_element(OnlimeSearchLocator.information_locator) == onlime_web_page.find_element(
        OnlimeSearchLocator.information_text_locator)


def test_authorization_with_otp_form(browser):
    onlime_web_page = Authorization(browser, base_url, OnlimeSearchLocator)
    onlime_web_page.go_to_site()
    sleep(5)
    """Проверяем наличие основных элементов на странице:
       логотипа в шапке странице"""
    assert onlime_web_page.find_element(OnlimeSearchLocator.header_child_locator) == onlime_web_page.find_element(
        OnlimeSearchLocator.logo_locator)
    """проверяем наличие формы ввода 'E-mail или мобильный телефон'"""
    assert onlime_web_page.find_element(OnlimeSearchLocator.login_field_text_locator).text == "E-mail или мобильный телефон"
    """проверяем наличие кнопки 'Получить код'"""
    assert onlime_web_page.find_element(OnlimeSearchLocator.otp_get_code_button_locator).text == "Получить код"
    """проверяем наличие кнопки 'Войти с паролем'"""
    assert onlime_web_page.find_element(OnlimeSearchLocator.go_with_password_button_locator).text == "Войти с паролем"
    """проверяем наличие вспомогательной информации в левой части страницы"""
    assert onlime_web_page.find_element(OnlimeSearchLocator.information_locator) == onlime_web_page.find_element(
        OnlimeSearchLocator.information_text_locator)


def test_forgot_password_form(browser):
    onlime_web_page = Authorization(browser, base_url, OnlimeSearchLocator)
    onlime_web_page.go_to_site()
    sleep(5)
    onlime_web_page.find_element(OnlimeSearchLocator.go_with_password_button_locator).click()
    onlime_web_page.find_element(OnlimeSearchLocator.forgot_password_link_locator).click()
    """Проверяем наличие основных элементов на странице:
                логотипа в шапке странице"""
    assert onlime_web_page.find_element(OnlimeSearchLocator.header_child_locator) == onlime_web_page.find_element(
        OnlimeSearchLocator.logo_locator)
    """табов выбора типа ввода контактных данных"""
    assert onlime_web_page.find_element(OnlimeSearchLocator.phone_tab_locator).text == "Телефон"
    assert onlime_web_page.find_element(OnlimeSearchLocator.email_tab_locator).text == "Почта"
    assert onlime_web_page.find_element(OnlimeSearchLocator.login_tab_locator).text == "Логин"
    assert onlime_web_page.find_element(OnlimeSearchLocator.personal_account_tab_locator).text == "Лицевой счёт"
    """проверяем, что по умолчанию выбран таб 'Телефон'"""
    assert "rt-tab--active" in onlime_web_page.find_element(OnlimeSearchLocator.phone_tab_locator).get_attribute("class")
    """проверяем наличие необходимых полей"""
    assert onlime_web_page.find_element(OnlimeSearchLocator.phone_field_locator).text == "Мобильный телефон"
    assert onlime_web_page.find_element(OnlimeSearchLocator.captcha_field_locator).text == "Символы"
    """Проверяем наличие кнопки 'Продолжить'"""
    assert onlime_web_page.find_element(OnlimeSearchLocator.reset_button_locator).text == "Продолжить"
    """Проверяем наличие кнопки 'Вернуться назад'"""
    assert onlime_web_page.find_element(OnlimeSearchLocator.come_back_button_locator).text == "Вернуться назад"
