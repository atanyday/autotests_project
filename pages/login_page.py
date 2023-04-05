import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base

class Login_page(Base):
    url = ""
    def __int__(self, driver):
        super.__init__(driver)


    # Methods
    def autorization(self):
        self.driver.get(self.url)
        self.driver.set_window_position(0, 0)
        self.driver.set_window_size(1900, 1200)
        print("Browser opened")
        self.get_current_url()