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
    price_product_1 = "//*[@id='basket_items']/li[1]/div[5]/span"
    price_product_2 = "//*[@id='basket_items']/li[2]/div[5]/span"
    cart_total_price = "//span[@class='selected-products__final-price']"

    # Getters
    def get_cart_icon(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.cart_icon)))
    def get_price_product_1(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.price_product_1)))
    def get_price_product_2(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.price_product_2)))
    def get_cart_total_price(self):
        # have to use time.sleep() because of delay in calculating price on the page which cause errors
        time.sleep(4)
        return self.driver.find_element(By.XPATH, self.cart_total_price)
        # return WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, self.cart_total_price)))

    # Actions
    def click_cart_icon(self):
        self.get_cart_icon().click()
        print("Click on cart icon")
    def show_price_product_1(self):
        self.price_product_1_text = self.get_price_product_1().text
        print("Product 1 price: " + self.price_product_1_text)
    def show_price_product_2(self):
        self.price_product_2_text = self.get_price_product_2().text
        print("Product 2 price: " + self.price_product_2_text)
    def show_cart_total_price(self):
        self.cart_total_price_text = self.get_cart_total_price().text
        print("Cart total price: " + self.cart_total_price_text)
    def number_price_product_1(self):
        # delete space and letters from price
        self.product_1_price_no_space = self.price_product_1_text.replace(" ", "")
        self.product_1_price_number = self.product_1_price_no_space[:-2]
        print("Product 1 price number: " + self.product_1_price_number)
    def number_price_product_2(self):
        # delete space and letters from price
        self.product_2_price_no_space = self.price_product_2_text.replace(" ", "")
        self.product_2_price_number = self.product_2_price_no_space[:-2]
        print("Product 2 price number: " + self.product_2_price_number)
    def count_total_price(self):
        self.total_price = int(self.product_1_price_number) + int(self.product_2_price_number)
        self.total_price_value = self.total_price
        print("Total price of products: " + str(self.total_price_value))
    def number_cart_total_price(self):
        # delete space and letters from total price in cart for further comparison with our prices
        self.cart_total_price_no_space = self.cart_total_price_text.replace(" ", "")
        self.cart_total_price_number = self.cart_total_price_no_space[:-2]
        print("Cart total price number: " + self.cart_total_price_number)
    def compare_prices_in_cart(self):
        assert int(self.cart_total_price_number) == int(self.total_price_value)
        print("Total price is correct")

    # Methods
    def enter_cart(self):
        self.click_cart_icon()
        self.get_current_url()
        self.show_price_product_1()
        self.show_price_product_2()
        self.show_cart_total_price()
        self.number_price_product_1()
        self.number_price_product_2()
        self.count_total_price()
        self.number_cart_total_price()
        self.compare_prices_in_cart()
        time.sleep(2)

time.sleep(2)
