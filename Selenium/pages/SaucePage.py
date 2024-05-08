from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait as Wait


class SaucePage:
    user_name = None
    password = None
    login_button = None
    products = None
    cart_badge = None
    product_bag = None
    timeout = 10

    def __init__(self, driver):
        self.driver = driver
        self.wait = Wait(self.driver, self.timeout)
        self.assign_elements()

    def assign_elements(self):
        self.user_name = self.wait.until(ec.presence_of_element_located((By.ID, "user-name")))
        self.password = self.wait.until(ec.presence_of_element_located((By.ID, "password")))
        self.login_button = self.wait.until(ec.presence_of_element_located((By.XPATH, "//input[@type='submit']")))
        return self

    def home_page(self):
        self.products = self.wait.until(
            ec.presence_of_all_elements_located((By.XPATH, "//div[@class=\"inventory_item_description\"]")))
        self.product_bag = self.wait.until(
            ec.presence_of_element_located((By.XPATH, "//img[@alt=\"Sauce Labs Backpack\"]")))

    def product_added_on_home_page(self):
        self.cart_badge = self.wait.until(
            ec.presence_of_element_located((By.XPATH, "//span[@class=\"shopping_cart_badge\"]")))
        return self

    def product_page(self):
        self.product_bag = self.wait.until(
            ec.presence_of_element_located((By.XPATH, "//img[@alt=\"Sauce Labs Backpack\"]")))
        return self
