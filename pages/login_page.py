import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base

class Login_page(Base):
    def __int__(self, driver):
        super.__init__(driver)

    # Locators
    login_icon = "//a[@class='header__login']"
    mail_field = "//input[@name='USER_LOGIN']"
    password_field = "//input[@class='password']"
    login_button = "//button[@name='Login']"

    # Getters
    def get_login_icon(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.login_icon)))
    def get_mail_field(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.mail_field)))
    def get_password_field(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.password_field)))
    def get_login_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.login_button)))

    # Actions
    def click_login_icon(self):
        self.get_login_icon().click()
        print("Click login icon")
    def input_mail(self):
        mail = "qatest_mailbox@mail.ru"
        self.get_mail_field().send_keys(mail)
        print("Input mail")
    def input_password(self):
        password = "qRX2oxm7W4B2obD"
        self.get_password_field().send_keys(password)
        print("Input password")
    def click_login_button(self):
        self.get_login_button().click()
        print("Click login button")

    # Methods
    def autorization(self):
        self.click_login_icon()
        self.input_mail()
        self.input_password()
        self.click_login_button()
        print("Autorization success")