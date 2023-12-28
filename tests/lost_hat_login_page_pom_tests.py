import unittest

import config_reader
from helpers.wrappers import screenshot_decorator
from helpers.base_test_class import BaseTestClass
from pages import front_page
from pages.login_page import LoginPage
from selenium.webdriver.common.by import By
from pages.front_page import FrontPage

import time


class LostHatLoginPagePomTests(BaseTestClass):

    @screenshot_decorator
    def test_login_text_header(self):
        expected_text = 'Log in to your account'

        login_page = LoginPage(self.conf_driver)
        login_page.visit()
        header_text = login_page.get_header()

        self.assertEqual(expected_text, header_text, f'Expected text differ from actual.')

    @screenshot_decorator
    def test_correct_login(self):
        config = config_reader.load()
        expected_text = config['correct_user_fullname']
        user_mail = config['correct_user']
        user_pass = config['correct_user_pass']

        login_page = LoginPage(self.conf_driver)
        login_page.visit()

        front_page = login_page.log_in(user_mail, user_pass)

        self.assertEqual(expected_text, front_page.get_username(),f'Expected text differ from actual.')

