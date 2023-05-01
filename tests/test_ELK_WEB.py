from time import sleep
from pages.rst_pages import Authorization
from pages.locators import ELKSearchLocator
from conftest import *
import os
from dotenv import load_dotenv

load_dotenv()

base_url = 'https://lk.rt.ru/'
email = os.getenv('valid_email')
password = os.getenv('valid_password')

def test_authorization_form(browser):
    elk_web_page = Authorization(browser, base_url, ELKSearchLocator)
    elk_web_page.go_to_site()
    sleep(5)
    elk_web_page.find_element(ELKSearchLocator.go_with_password_button_locator).click()
    """Проверяем наличие основных элементов на странице:
    логотипа в шапке странице"""
    assert elk_web_page.find_element(ELKSearchLocator.header_child_locator) == elk_web_page.find_element(ELKSearchLocator.logo_locator)
    """табов выбора типа аутентификации"""
    assert elk_web_page.find_element(ELKSearchLocator.phone_tab_locator).text == "Телефон"
    assert elk_web_page.find_element(ELKSearchLocator.email_tab_locator).text == "Почта"
    assert elk_web_page.find_element(ELKSearchLocator.login_tab_locator).text == "Логин"
    assert elk_web_page.find_element(ELKSearchLocator.personal_account_tab_locator).text == "Лицевой счёт"
    """проверяем, что по умолчанию выбран таб аутентификации по телефону"""
    assert "rt-tab--active" in elk_web_page.find_element(ELKSearchLocator.phone_tab_locator).get_attribute("class")
    """проверяем наличие формы ввода 'Мобильный телефон'"""
    assert elk_web_page.find_element(ELKSearchLocator.phone_field_locator).text == "Мобильный телефон"
    """проверяем наличие формы ввода 'Пароль'"""
    assert elk_web_page.find_element(ELKSearchLocator.password_name_field_locator).text == "Пароль"
    """проверяем наличие кнопки 'Войти'"""
    assert elk_web_page.find_element(ELKSearchLocator.login_button_locator).text == "Войти"
    """Проверяем наличие кнопки 'Войти по временному коду'"""
    assert elk_web_page.find_element(ELKSearchLocator.login_otp_button_locator).text == "Войти по временному коду"
    """проверяем наличие ссылки на условия пользовательского соглашения"""
    assert elk_web_page.find_element(ELKSearchLocator.user_agreement_link_locator).text == "пользовательского соглашения"
    """проверяем налчие ссылки на форму регистрации"""
    assert elk_web_page.find_element(ELKSearchLocator.registration_link_locator).text == "Зарегистрироваться"
    """проверяем наличие вспомогательной информации в левой части страницы"""
    assert elk_web_page.find_element(ELKSearchLocator.information_locator) == elk_web_page.find_element(
        ELKSearchLocator.information_text_locator)


def test_registration_form(browser):
    elk_web_page = Authorization(browser, base_url, ELKSearchLocator)
    elk_web_page.go_to_site()
    sleep(5)
    elk_web_page.find_element(ELKSearchLocator.go_with_password_button_locator).click()
    elk_web_page.find_element(ELKSearchLocator.registration_link_locator).click()
    """Проверяем наличие основных элементов на странице:
        логотипа в шапке странице"""
    assert elk_web_page.find_element(ELKSearchLocator.header_child_locator) == elk_web_page.find_element(
        ELKSearchLocator.logo_locator)
    """проверяем наличие необходимых полей"""
    assert elk_web_page.find_element(ELKSearchLocator.registration_name_field_locator).text == "Имя"
    assert elk_web_page.find_element(ELKSearchLocator.registration_lastname_field_locator).text == "Фамилия"
    assert elk_web_page.find_element(ELKSearchLocator.registration_region_field_locator).text == "Регион"
    assert elk_web_page.find_element(ELKSearchLocator.registration_email_or_phone_field_locator).text == "E-mail или мобильный телефон"
    assert elk_web_page.find_element(
        ELKSearchLocator.registration_password_field_locator).text == "Пароль"
    assert elk_web_page.find_element(
        ELKSearchLocator.registration_repeat_password_field_locator).text == "Подтверждение пароля"
    """Проверяем наличие кнопки 'Зарегистрироваться'"""
    assert elk_web_page.find_element(
        ELKSearchLocator.registration_button_locator).text == "Зарегистрироваться"
    """проверяем наличие ссылки на условия пользовательского соглашения"""
    assert elk_web_page.find_element(
        ELKSearchLocator.user_agreement_link_locator).text == "пользовательского соглашения"
    """проверяем наличие логотипа и продуктового слогана в левой части страницы"""
    assert elk_web_page.find_element(ELKSearchLocator.information_locator) == elk_web_page.find_element(
        ELKSearchLocator.information_text_locator)

def test_forgot_password_form(browser):
    elk_web_page = Authorization(browser, base_url, ELKSearchLocator)
    elk_web_page.go_to_site()
    sleep(5)
    elk_web_page.find_element(ELKSearchLocator.go_with_password_button_locator).click()
    elk_web_page.find_element(ELKSearchLocator.forgot_password_link_locator).click()
    """Проверяем наличие основных элементов на странице:
            логотипа в шапке странице"""
    assert elk_web_page.find_element(ELKSearchLocator.header_child_locator) == elk_web_page.find_element(
        ELKSearchLocator.logo_locator)
    """табов выбора типа ввода контактных данных"""
    assert elk_web_page.find_element(ELKSearchLocator.phone_tab_locator).text == "Телефон"
    assert elk_web_page.find_element(ELKSearchLocator.email_tab_locator).text == "Почта"
    assert elk_web_page.find_element(ELKSearchLocator.login_tab_locator).text == "Логин"
    assert elk_web_page.find_element(ELKSearchLocator.personal_account_tab_locator).text == "Лицевой счёт"
    """проверяем, что по умолчанию выбран таб 'Телефон'"""
    assert "rt-tab--active" in elk_web_page.find_element(ELKSearchLocator.phone_tab_locator).get_attribute("class")
    """проверяем наличие необходимых полей"""
    assert elk_web_page.find_element(ELKSearchLocator.phone_field_locator).text == "Мобильный телефон"
    assert elk_web_page.find_element(ELKSearchLocator.captcha_field_locator).text == "Символы"
    """Проверяем наличие кнопки 'Продолжить'"""
    assert elk_web_page.find_element(ELKSearchLocator.reset_button_locator).text == "Продолжить"
    """Проверяем наличие кнопки 'Вернуться назад'"""
    assert elk_web_page.find_element(ELKSearchLocator.come_back_button_locator).text == "Вернуться назад"



def test_authorization_with_valid_email_and_password(browser):
    elk_web_page = Authorization(browser, base_url, ELKSearchLocator)
    elk_web_page.go_to_site()
    sleep(5)
    elk_web_page.find_element(ELKSearchLocator.go_with_password_button_locator).click()
    elk_web_page.find_element(ELKSearchLocator.email_tab_locator).click()
    elk_web_page.enter_email(ELKSearchLocator, email)
    elk_web_page.enter_password(ELKSearchLocator, password)
    elk_web_page.clik_on_login_button(ELKSearchLocator)
    sleep(5)
    "проверяем переход на соответствующую страницу"
    assert browser.current_url == 'https://start.rt.ru/?tab=main'

@pytest.mark.parametrize("password",
                        [
                            generate_string(255)
                            , generate_string(1001)
                            , russian_chars()
                            , russian_chars().upper()
                            , chinese_chars()
                            , special_chars()
                            , 123
                        ],
                        ids =
                        [
                            '255 symbols'
                            , 'more that 1000 symbols'
                            , 'russian'
                            , 'RUSSIAN'
                            , 'chinese'
                            , 'specials'
                            , 'digit'
                        ])
def test_authorization_with_invalid_password(browser, password):
    elk_web_page = Authorization(browser, base_url, ELKSearchLocator)
    elk_web_page.go_to_site()
    sleep(5)
    elk_web_page.find_element(ELKSearchLocator.go_with_password_button_locator).click()
    elk_web_page.find_element(ELKSearchLocator.email_tab_locator).click()
    elk_web_page.enter_email(ELKSearchLocator, email)
    elk_web_page.enter_password(ELKSearchLocator, password)
    "В случает пароля, длинной свыше 1000 символов проверяем, что в поле вводятся первые 256 символов"
    if password == generate_string(1001):
        assert len(elk_web_page.find_element(ELKSearchLocator.password_text_field_locator).text) <= 256 and \
           elk_web_page.find_element(ELKSearchLocator.password_text_field_locator).text == generate_string(1001)[:257]
    elk_web_page.clik_on_login_button(ELKSearchLocator)
    """проверяем, что высвечивается подсказка о неверном вводе логина или пароля"""
    assert elk_web_page.find_element(ELKSearchLocator.error_message_locator).text == 'Неверный логин или пароль'
    """проверяем, что ссылка 'Забыл пароль подсвечивается оранжевый цветом'"""
    assert elk_web_page.find_element(ELKSearchLocator.forgot_password_link_locator).text == elk_web_page.find_element(
        ELKSearchLocator.forgot_password_orange_link_locator).text


def test_authorization_with_invalid_email_of_12_numbers(browser):
    elk_web_page = Authorization(browser, base_url, ELKSearchLocator)
    elk_web_page.go_to_site()
    sleep(5)
    elk_web_page.find_element(ELKSearchLocator.go_with_password_button_locator).click()
    elk_web_page.find_element(ELKSearchLocator.email_tab_locator).click()
    elk_web_page.enter_email(ELKSearchLocator, generate_numb_string(12))
    elk_web_page.enter_password(ELKSearchLocator, password)
    sleep(5)
    """проверяем, что таб аутентификации перешел на 'Лицевой счет'"""
    assert "rt-tab--active" in elk_web_page.find_element(ELKSearchLocator.personal_account_tab_locator).get_attribute("class")
    elk_web_page.clik_on_login_button(ELKSearchLocator)
    """проверяем, что высвечивается подсказка о неверном вводе логина или пароля"""
    assert elk_web_page.find_element(ELKSearchLocator.error_message_locator).text == 'Неверный логин или пароль'

def test_authorization_with_empty_field_email(browser):
    elk_web_page = Authorization(browser, base_url, ELKSearchLocator)
    elk_web_page.go_to_site()
    sleep(5)
    elk_web_page.find_element(ELKSearchLocator.go_with_password_button_locator).click()
    elk_web_page.find_element(ELKSearchLocator.email_tab_locator).click()
    elk_web_page.enter_email(ELKSearchLocator, '')
    elk_web_page.enter_password(ELKSearchLocator, password)
    elk_web_page.clik_on_login_button(ELKSearchLocator)
    """проверяем, что высвечивается подсказка о незаполненном поле 'Почта'"""
    assert elk_web_page.find_element(ELKSearchLocator.error_email_pass_message_locator).text == 'Введите адрес, указанный при регистрации'

def test_authorization_with_empty_field_password(browser):
    elk_web_page = Authorization(browser, base_url, ELKSearchLocator)
    elk_web_page.go_to_site()
    sleep(5)
    elk_web_page.find_element(ELKSearchLocator.go_with_password_button_locator).click()
    elk_web_page.find_element(ELKSearchLocator.email_tab_locator).click()
    elk_web_page.enter_email(ELKSearchLocator, email)
    elk_web_page.enter_password(ELKSearchLocator, '')
    elk_web_page.clik_on_login_button(ELKSearchLocator)
    """проверяем, что высвечивается подсказка о незаполненном поле 'Пароль'"""
    assert elk_web_page.find_element(ELKSearchLocator.error_email_pass_message_locator).text == 'Введите пароль, указанный при регистрации'
    """проверяем, что ссылка 'Забыл пароль подсвечивается оранжевый цветом'"""
    assert elk_web_page.find_element(ELKSearchLocator.forgot_password_link_locator).text == elk_web_page.find_element(
        ELKSearchLocator.forgot_password_orange_link_locator).text

def test_authorization_with_long_email(browser):
    elk_web_page = Authorization(browser, base_url, ELKSearchLocator)
    elk_web_page.go_to_site()
    sleep(5)
    elk_web_page.find_element(ELKSearchLocator.go_with_password_button_locator).click()
    elk_web_page.find_element(ELKSearchLocator.email_tab_locator).click()
    elk_web_page.enter_email(ELKSearchLocator, generate_string(1001))
    elk_web_page.enter_password(ELKSearchLocator, password)
    """проверяем, что таб аутентификации перешел на 'Логин'"""
    assert "rt-tab--active" in elk_web_page.find_element(ELKSearchLocator.login_tab_locator).get_attribute("class")
    """Проверяем, что в поле вводятся первые 256 символов """
    assert len(elk_web_page.find_element(ELKSearchLocator.login_text_field_locator).get_attribute("value")) <= 256 and \
           elk_web_page.find_element(ELKSearchLocator.login_text_field_locator).get_attribute("value") == generate_string(1001)[:257]
    elk_web_page.clik_on_login_button(ELKSearchLocator)
    """Проверяем наличие ошибки о неверно введем логине или пароле"""
    assert elk_web_page.find_element(ELKSearchLocator.error_message_locator).text == 'Неверный логин или пароль'
