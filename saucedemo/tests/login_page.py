from selenium.webdriver.common.by import By

class Login:
    URL = "https://www.saucedemo.com/"
    VALID_USERNAME = "standard_user"
    VALID_PASSWORD = "secret_sauce"
    INVALID_USERNAME = "invalid_user"
    INVALID_PASSWORD = "invalid_password"

    def __init__(self, driver):
        self.driver = driver

    def load(self):
        self.driver.get(self.URL)

    def login(self, username, password):
        self.driver.find_element(By.ID, "user-name").send_keys(username)
        self.driver.find_element(By.ID, "password").send_keys(password)
        self.driver.find_element(By.ID, "login-button").click()
