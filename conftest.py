import pytest
from selenium import webdriver


@pytest.fixture(scope='session')
def browser():
    driver = webdriver.Chrome(executable_path="./chromedriver")
    yield driver
    driver.quit()

def generate_string(num):
   return "x" * num


def generate_numb_string(num):
   return "1" * num

def russian_chars():
   return 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'


def chinese_chars():
   return '的一是不了人我在有他这为之大来以个中上们'


def special_chars():
   return '|\\/!@#$%^&*()-_=+`~?"№;:[]{}'
