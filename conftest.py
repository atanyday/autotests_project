import pytest
from selenium import webdriver

@pytest.fixture()
def set_up():
    print("=== TEST START ===")
    yield
    # driver.close()
    print("=== TEST FINISH ===")

@pytest.fixture(scope="module")
def set_group():
    print("= ENTER SYSTEM =")
    yield
    # driver.close()
    print("= EXIT SYSTEM =")