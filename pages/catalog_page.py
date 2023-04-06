import time
from selenium.common import NoSuchWindowException, NoSuchElementException
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
    filter_btn = "//input[@id='set_filter']"
    sort_btn_popular = "//a[@class='sort_btn  asc SHOWS']"
    product_characteristics = "//*[@class='tabs1 main_tabs1 tabs-head']/li[4]"
    # Dog section
    filter_brand_hills = "//label[@data-role='label_OPTIMUS_SMART_FILTER_435_408697150']"
    product_1 = "//*[@id='right_block_ajax']/div[2]/div[2]/div[1]/div/div[4]/div/div[1]/a/span"
    product_1_add = "//a[@data-id='76033']"
    # Cat section
    filter_brand_sheba = "//label[@data-role='label_OPTIMUS_SMART_FILTER_435_2778784718']"
    product_2_add = "//a[@data-id='62882']"

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
    def get_filter_brand_sheba(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.filter_brand_sheba)))
    def get_filter_btn(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.filter_btn)))
    def get_sort_btn_popular(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.sort_btn_popular)))
    def get_product_1(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.product_1)))
    def get_product_characteristics(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.product_characteristics)))
    def get_product_1_add(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.product_1_add)))
    def get_product_2_add(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.product_2_add)))

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
        print("Filter: scroll and choose brand HILL'S")
    def click_filter_brand_sheba(self):
        action = ActionChains(self.driver)
        action.move_to_element(self.get_filter_brand_sheba()).perform()
        self.get_filter_brand_sheba().click()
        print("Filter: scroll and choose brand Sheba")
    def click_filter_btn(self):
        action = ActionChains(self.driver)
        action.move_to_element(self.get_filter_btn()).perform()
        self.get_filter_btn().click()
        print("Filter: confirmation button clicked")
    def click_sort_btn_popular(self):
        self.get_sort_btn_popular().click()
        print("Sort: by popular")
    def click_product_1(self):
        self.get_product_1().click()
        print("Choose product_1")
    def click_product_characteristics(self):
        self.get_product_characteristics().click()
        print("Go to characteristics info of the product")
    def click_product_1_add(self):
        self.get_product_1_add().click()
        print("Add product_1 to cart")
    def click_product_2_add(self):
        self.get_product_2_add().click()
        print("Add product_2 to cart")

    # Methods
    def buy_dog_product(self):
        # self.click_filter_feed()
        # self.click_filter_price()
        # self.click_filter_price_max(5000)
        self.click_filter_brand()
        self.click_filter_brand_hills()
        self.click_filter_btn()
        self.click_sort_btn_popular()
        # self.click_product_1()
        # self.driver.execute_script("window.scrollTo(0, 500)")
        # self.click_product_characteristics()
        # self.driver.back()
        self.click_product_1_add()
    def buy_cat_product(self):
        self.click_filter_brand()
        self.click_filter_brand_sheba()
        self.click_filter_btn()
        self.click_product_2_add()
