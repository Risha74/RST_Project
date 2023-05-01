from pages.rst_pages import Authorization
from pages.locators import StartSearchLocator
from time import sleep

base_url = 'https://start.rt.ru/'


def test_authorization_form(browser):
    start_web_page = Authorization(browser, base_url, StartSearchLocator)
    start_web_page.go_to_site()
    sleep(5)
    start_web_page.find_element(StartSearchLocator.go_with_password_button_locator).click()
    """Проверяем наличие основных элементов на странице:
        логотипа в шапке странице"""
    assert start_web_page.find_element(StartSearchLocator.header_child_locator) == start_web_page.find_element(
        StartSearchLocator.logo_locator)
    """табов выбора типа аутентификации"""
    assert start_web_page.find_element(StartSearchLocator.phone_tab_locator).text == "Телефон"
    assert start_web_page.find_element(StartSearchLocator.email_tab_locator).text == "Почта"
    assert start_web_page.find_element(StartSearchLocator.login_tab_locator).text == "Логин"
    assert start_web_page.find_element(StartSearchLocator.personal_account_tab_locator).text == "Лицевой счёт"
    """проверяем, что по умолчанию выбрат таб аутентификации по телефону"""
    assert "rt-tab--active" in start_web_page.find_element(StartSearchLocator.phone_tab_locator).get_attribute("class")
    """проверяем наличие формы ввода 'Мобильный телефон'"""
    assert start_web_page.find_element(StartSearchLocator.phone_field_locator).text == "Мобильный телефон"
    """проверяем наличие формы ввода 'Пароль'"""
    assert start_web_page.find_element(StartSearchLocator.password_name_field_locator).text == "Пароль"
    """проверяем наличие кнопки 'Войти'"""
    assert start_web_page.find_element(StartSearchLocator.login_button_locator).text == "Войти"
    """Проверяем наличие кнопки 'Войти по временному коду'"""
    assert start_web_page.find_element(StartSearchLocator.login_otp_button_locator).text == "Войти по временному коду"
    """проверяем наличие ссылки на условия пользовательского соглашения"""
    assert start_web_page.find_element(StartSearchLocator.user_agreement_link_locator).text == "пользовательского соглашения"
    """проверяем налчие ссылки на форму регистрации"""
    assert start_web_page.find_element(StartSearchLocator.registration_link_locator).text == "Зарегистрироваться"
    """проверяем наличие вспомогательной информации в левой части страницы"""
    assert start_web_page.find_element(StartSearchLocator.information_locator) == start_web_page.find_element(
        StartSearchLocator.information_text_locator)


def test_authorization_with_otp_form(browser):
    start_web_page = Authorization(browser, base_url, StartSearchLocator)
    start_web_page.go_to_site()
    sleep(5)
    """Проверяем наличие основных элементов на странице:
           логотипа в шапке странице"""
    assert start_web_page.find_element(StartSearchLocator.header_child_locator) == start_web_page.find_element(
        StartSearchLocator.logo_locator)
    """проверяем наличие формы ввода 'E-mail или мобильный телефон'"""
    assert start_web_page.find_element(StartSearchLocator.login_field_text_locator).text == "E-mail или мобильный телефон"
    """проверяем наличие кнопки 'Получить код'"""
    assert start_web_page.find_element(StartSearchLocator.otp_get_code_button_locator).text == "Получить код"
    """проверяем наличие кнопки 'Войти с паролем'"""
    assert start_web_page.find_element(StartSearchLocator.go_with_password_button_locator).text == "Войти с паролем"
    """проверяем наличие вспомогательной информации в левой части страницы"""
    assert start_web_page.find_element(StartSearchLocator.information_locator) == start_web_page.find_element(
        StartSearchLocator.information_text_locator)


def test_registration_form(browser):
    start_web_page = Authorization(browser, base_url, StartSearchLocator)
    start_web_page.go_to_site()
    sleep(5)
    start_web_page.find_element(StartSearchLocator.go_with_password_button_locator).click()
    start_web_page.find_element(StartSearchLocator.registration_link_locator).click()
    """Проверяем наличие основных элементов на странице:
            логотипа в шапке странице"""
    assert start_web_page.find_element(StartSearchLocator.header_child_locator) == start_web_page.find_element(
        StartSearchLocator.logo_locator)
    """проверяем наличие необходимых полей"""
    assert start_web_page.find_element(StartSearchLocator.registration_name_field_locator).text == "Имя"
    assert start_web_page.find_element(StartSearchLocator.registration_lastname_field_locator).text == "Фамилия"
    assert start_web_page.find_element(StartSearchLocator.registration_region_field_locator).text == "Регион"
    assert start_web_page.find_element(StartSearchLocator.registration_email_or_phone_field_locator).text == "E-mail или мобильный телефон"
    assert start_web_page.find_element(
        StartSearchLocator.registration_password_field_locator).text == "Пароль"
    assert start_web_page.find_element(
        StartSearchLocator.registration_repeat_password_field_locator).text == "Подтверждение пароля"
    """Проверяем наличие кнопки 'Зарегистрироваться'"""
    assert start_web_page.find_element(
        StartSearchLocator.registration_button_locator).text == "Зарегистрироваться"
    """проверяем наличие ссылки на условия пользовательского соглашения"""
    assert start_web_page.find_element(
        StartSearchLocator.user_agreement_link_locator).text == "пользовательского соглашения"
    """проверяем наличие логотипа и продуктового слогана в левой части страницы"""
    assert start_web_page.find_element(StartSearchLocator.information_locator) == start_web_page.find_element(
        StartSearchLocator.information_text_locator)


def test_forgot_password_form(browser):
    start_web_page = Authorization(browser, base_url, StartSearchLocator)
    start_web_page.go_to_site()
    sleep(5)
    start_web_page.find_element(StartSearchLocator.go_with_password_button_locator).click()
    start_web_page.find_element(StartSearchLocator.forgot_password_link_locator).click()
    """Проверяем наличие основных элементов на странице:
               логотипа в шапке странице"""
    assert start_web_page.find_element(StartSearchLocator.header_child_locator) == start_web_page.find_element(
        StartSearchLocator.logo_locator)
    """табов выбора типа ввода контактных данных"""
    assert start_web_page.find_element(StartSearchLocator.phone_tab_locator).text == "Телефон"
    assert start_web_page.find_element(StartSearchLocator.email_tab_locator).text == "Почта"
    assert start_web_page.find_element(StartSearchLocator.login_tab_locator).text == "Логин"
    assert start_web_page.find_element(StartSearchLocator.personal_account_tab_locator).text == "Лицевой счёт"
    """проверяем, что по умолчанию выбран таб 'Телефон'"""
    assert "rt-tab--active" in start_web_page.find_element(StartSearchLocator.phone_tab_locator).get_attribute("class")
    """проверяем наличие необходимых полей"""
    assert start_web_page.find_element(StartSearchLocator.phone_field_locator).text == "Мобильный телефон"
    assert start_web_page.find_element(StartSearchLocator.captcha_field_locator).text == "Символы"
    """Проверяем наличие кнопки 'Продолжить'"""
    assert start_web_page.find_element(StartSearchLocator.reset_button_locator).text == "Продолжить"
    """Проверяем наличие кнопки 'Вернуться назад'"""
    assert start_web_page.find_element(StartSearchLocator.come_back_button_locator).text == "Вернуться назад"
