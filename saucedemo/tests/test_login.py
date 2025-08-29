import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from tests.login_page import Login

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_login_success(driver):
    login_page = Login(driver)
    login_page.load()
    login_page.login(Login.VALID_USERNAME, Login.VALID_PASSWORD)
    assert "inventory" in driver.current_url

def test_login_failure(driver):
    login_page = Login(driver)
    login_page.load()
    login_page.login(Login.INVALID_USERNAME, Login.INVALID_PASSWORD)
    error_message = driver.find_element(By.CLASS_NAME, "error-message-container").text
    assert "Username and password do not match" in error_message

def test_inventory_page(driver):
    login_page = Login(driver)
    login_page.load()
    login_page.login(Login.VALID_USERNAME, Login.VALID_PASSWORD)
    inventory_items = driver.find_elements(By.CLASS_NAME, "inventory_item")
    assert len(inventory_items) > 0
