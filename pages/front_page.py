from selenium.webdriver.common.by import By


class FrontPage:

    def __init__(self, driver):

        self.driver = driver

        self.url = 'https://autodemo.testoneo.com/en/'
        self.user_name_header = '//a[@class="account"]/*[@class="hidden-sm-down"]'

    def visit(self):
        self.driver.get(self.url)
        return self

    def get_username(self):
        user_name_element = self.driver.find_element(By.XPATH, self.user_name_header)
        return user_name_element.text