import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base

class Main_page(Base):
    def __int__(self, driver):
        super.__init__(driver)

    # Locators
    logo = "//*[@class='header__logo']"
    choose_city = "//span[@class='header__city-selection-text header__city-selection-text--green']"
    choose_city_moscow = "//a[@data-id='129']"

    # Getters
    def get_logo(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.logo)))
    def get_choose_city(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.choose_city)))
    def get_choose_city_moscow(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.choose_city_moscow)))

    # Actions
    def click_logo(self):
        self.get_logo().click()
        print("Click on Logo")
    def click_choose_city(self):
        self.get_choose_city().click()
        print("City list opened")
    def click_choose_city_moscow(self):
        self.get_choose_city_moscow().click()
        print("Choose Moscow")

    # Methods
    def change_city_to_moscow(self):
        self.click_logo()
        self.click_choose_city()
        self.click_choose_city_moscow()
        # time.sleep(2)
        city_text = self.driver.find_element(By.XPATH, "//*[@class='header__city-selection-wrp']").click()
        value_city_text = city_text.text
        print(value_city_text)