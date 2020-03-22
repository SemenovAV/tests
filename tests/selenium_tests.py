import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class TestsYandexAuth(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome()
        self.addCleanup(self.browser.quit)

    def test_auth(self):
        name = 'Testuser1234567891'
        password = 'testpass'
        self.browser.get('https://passport.yandex.ru/auth/')
        login = self.browser.find_element_by_name(name='login')
        login.send_keys(name)
        button = self.browser.find_element_by_css_selector(css_selector='.passp-sign-in-button ')
        button.click()
        password_input = WebDriverWait(self.browser, 5).until(
            EC.presence_of_element_located((By.ID, 'passp-field-passwd')))
        password_input.send_keys(password)
        button_next = self.browser.find_element_by_css_selector(css_selector='.passp-sign-in-button ')
        button_next.click()
        username = WebDriverWait(self.browser, 5).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'personal-info-login__text'))
        ).text
        self.assertEqual(name, username)
        self.browser.close()

    def test_auth_no(self):
        name = '__'
        self.browser.get('https://passport.yandex.ru/auth/')
        login = self.browser.find_element_by_name(name='login')
        login.send_keys(name)
        button = self.browser.find_element_by_css_selector(css_selector='.passp-sign-in-button ')
        button.click()
        err = WebDriverWait(self.browser, 5).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'passp-form-field__error'))
        ).text
        self.assertEqual('Такой логин не подойдет', err)
