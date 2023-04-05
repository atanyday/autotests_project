import pytest
import time
from selenium import webdriver

from pages.login_page import Login_page
from pages.main_page import Main_page


def test_buy_product_1():
    driver = webdriver.Chrome(executable_path='/chromedriver')

    # Autorization
    login = Login_page(driver)
    login.autorization()
    # return to main page and change city to Moscow
    mp = Main_page(driver)
    mp.change_city_to_moscow()