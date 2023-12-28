from selenium.webdriver.common.by import By

from pages import front_page


class LoginPage:

    def __init__(self, driver):
        self.url = 'https://autodemo.testoneo.com/en/login'

        self.driver = driver

        self.header_xpath = '//*[@id="main"]/header/h1'
        self.email_xpath = '//*[@id="login-form"]/section/div[1]/div[1]/input'
        self.password_xpath = '//*[@id="login-form"]/section/div[2]/div[1]/div/input'
        self.login_button_xpath = '//*[@id="submit-login"]'

    def visit(self):
        self.driver.get(self.url)
        return self


    def get_header(self):
        element = self.driver.find_element(By.XPATH, self.header_xpath)
        return element.text

    def enter_email(self, user_email):
        #finding login box and sending value
        email_element = self.driver.find_element(By.XPATH, self.email_xpath)
        email_element.clear()
        email_element.send_keys(user_email)
        return self

    def enter_password(self, user_pass):
        #finding password box and sending value
        password_element = self.driver.find_element(By.XPATH, self.password_xpath)
        password_element.clear()
        password_element.send_keys(user_pass)
        return self

    def click_login_button(self):
        #finding and clicking login button "Sign In"
        button_element = self.driver.find_element(By.XPATH, self.login_button_xpath)
        button_element.click()
        return self

    def log_in(self, user_email, user_pass):
        self.enter_email(user_email)
        self.enter_password(user_pass)
        self.click_login_button()
        return front_page.FrontPage(self.driver)