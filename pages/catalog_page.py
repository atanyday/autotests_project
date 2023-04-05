import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import Keys, ActionChains

from base.base_class import Base

class Catalog_page(Base):
    def __int__(self, driver):
        super.__init__(driver)

    # Locators
    filter_feed = "//div[@class='sidebar-categories-short-list']/div[1]/a"
    filter_price = "//*[@data-property_id='488']"
    filter_price_max = "//*[@class='max-price']"
    filter_brand = "//*[@data-prop_code='brend']"
    filter_brand_hills = "//label[@data-role='label_OPTIMUS_SMART_FILTER_435_408697150']"
    filter_btn = "//input[@id='set_filter']"

    # Getters
    def get_filter_feed(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.filter_feed)))
    def get_filter_price(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.filter_price)))
    def get_filter_price_max(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.filter_price_max)))
    def get_filter_brand(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.filter_brand)))
    def get_filter_brand_hills(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.filter_brand_hills)))
    def get_filter_btn(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.filter_btn)))

    # Actions
    def click_filter_feed(self):
        self.get_filter_feed().click()
        print("Filter: choose 'Сухой корм'")
    def click_filter_price(self):
        self.get_filter_price().click()
        print("Filter: price")
    def click_filter_price_max(self, max_price):
        self.get_filter_price_max().click()
        self.get_filter_price_max().send_keys(max_price)
        print("Filter: set max price")
    def click_filter_brand(self):
        self.get_filter_brand().click()
        print("Filter: brand")
    def click_filter_brand_hills(self):
        action = ActionChains(self.driver)
        action.move_to_element(self.get_filter_brand_hills()).perform()
        self.get_filter_brand_hills().click()
        print("Filter: scroll and choose brand 'Chammy'")
    def click_filter_btn(self):
        action = ActionChains(self.driver)
        action.move_to_element(self.get_filter_btn()).perform()
        self.get_filter_btn().click()
        print("Filter: confirmation button clicked")


    # Methods
    def buy_dog_product(self):
        self.click_filter_feed()
        self.click_filter_price()
        self.click_filter_price_max(5000)
        self.click_filter_brand()
        self.click_filter_brand_hills()
        self.driver.execute_script("window.scrollTo(0, 1000)")
        self.click_filter_btn()

