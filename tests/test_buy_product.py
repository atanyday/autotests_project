import pytest
import time
from selenium import webdriver
from selenium.webdriver import Keys, ActionChains

from pages.login_page import Login_page
from pages.main_page import Main_page
from pages.catalog_page import Catalog_page
from pages.cart_page import Cart_page

def test_buy_product_1(set_up):
    driver = webdriver.Chrome(executable_path='/chromedriver')
    url = "https://www.dinozavrik.ru/"
    driver.get(url)
    driver.set_window_position(0, 0)
    driver.set_window_size(1900, 1200)
    print("Browser opened")

    # Autorization
    login = Login_page(driver)
    login.autorization()

    # Change city to Moscow on the main page
    mp = Main_page(driver)
    mp.change_city_to_moscow()

    # Choose product for dogs and add to cart
    cp = Catalog_page(driver)
    mp.click_block_dog_products()
    cp.buy_dog_product()

    # Go back to main page
    driver.get(url)

    # Choose product for cats and add to cart
    mp.click_block_cat_products()
    cp.buy_cat_product()

    # Go to cart
    cart_p = Cart_page(driver)
    cart_p.enter_cart()
    # # очистить корзину
    # cart_p.empty_cart()
