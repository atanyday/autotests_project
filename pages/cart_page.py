import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import Keys, ActionChains

from base.base_class import Base

class Cart_page(Base):
    def __int__(self, driver):
        super.__init__(driver)

    # Locators
    cart_icon = "//a[@class='header__cart ']"

    # Getters
    def get_cart_icon(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.cart_icon)))

    # Actions
    def click_cart_icon(self):
        self.get_cart_icon().click()
        print("Click on cart icon")

    # Methods
    def enter_cart(self):
        self.click_cart_icon()
        self.get_current_url()
        time.sleep(2)

time.sleep(2)
