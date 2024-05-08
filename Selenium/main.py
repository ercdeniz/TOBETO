from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait as Wait


def replace_and_convert(element):
    price = float(element.replace("$", ""))
    return price


class TestSauce:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://www.saucedemo.com/")

    def empty_login(self):
        login_button = self.driver.find_element(By.XPATH, "//input[@type='submit']")
        login_button.click()
        error_message = self.driver.find_element(By.XPATH, "//h3[@data-test=\"error\"]")
        assert error_message.text == "Epic sadface: Username is required"

    def empty_password_login(self):
        user_name = self.driver.find_element(By.XPATH, "//input[@id=\"user-name\"]")
        user_name.send_keys("standard_user")
        login_button = self.driver.find_element(By.XPATH, "//input[@type='submit']")
        login_button.click()
        error_message = self.driver.find_element(By.XPATH, "//h3[@data-test=\"error\"]")
        assert error_message.text == "Epic sadface: Password is required"

    def locked_user_login(self):
        user_name = self.driver.find_element(By.XPATH, "//input[@id=\"user-name\"]")
        user_name.send_keys("locked_out_user")
        password = self.driver.find_element(By.XPATH, "//input[@id=\"password\"]")
        password.send_keys("secret_sauce")
        login_button = self.driver.find_element(By.XPATH, "//input[@type='submit']")
        login_button.click()
        error_message = self.driver.find_element(By.XPATH, "//h3[@data-test=\"error\"]")
        assert error_message.text == "Epic sadface: Sorry, this user has been locked out."

    def product_count(self):
        user_name = self.driver.find_element(By.XPATH, "//input[@id=\"user-name\"]")
        user_name.send_keys("standard_user")
        password = self.driver.find_element(By.XPATH, "//input[@id=\"password\"]")
        password.send_keys("secret_sauce")
        login_button = self.driver.find_element(By.XPATH, "//input[@type='submit']")
        login_button.click()
        assert self.driver.current_url == "https://www.saucedemo.com/inventory.html"
        products = self.driver.find_elements(By.XPATH, "//div[@class=\"inventory_item_description\"]")
        assert len(products) == 6

    def add_product_to_cart(self):
        user_name = self.driver.find_element(By.XPATH, "//input[@id=\"user-name\"]")
        user_name.send_keys("standard_user")
        password = self.driver.find_element(By.XPATH, "//input[@id=\"password\"]")
        password.send_keys("secret_sauce")
        login_button = self.driver.find_element(By.XPATH, "//input[@type='submit']")
        login_button.click()
        Wait(self.driver, 5).until(ec.visibility_of_element_located((By.XPATH, "//div[@class=\"inventory_item_description\"]")))
        products = self.driver.find_elements(By.XPATH, "//div[@class=\"inventory_item_description\"]")
        count = 0
        for product in products:
            price = replace_and_convert(product.find_element(By.CLASS_NAME, "inventory_item_price").text)
            if price < 20.00:
                add_to_cart = product.find_element(By.XPATH, "//button[contains(@data-test, 'add-to-cart')]")
                add_to_cart.click()
                count += 1
        cart_count = self.driver.find_element(By.XPATH, "//span[@class=\"shopping_cart_badge\"]")
        cart_count_value = int(cart_count.text)
        assert count == cart_count_value

    def visual_user_login(self):
        user_name = self.driver.find_element(By.XPATH, "//input[@id=\"user-name\"]")
        user_name.send_keys("visual_user")
        password = self.driver.find_element(By.XPATH, "//input[@id=\"password\"]")
        password.send_keys("secret_sauce")
        login_button = self.driver.find_element(By.XPATH, "//input[@type='submit']")
        login_button.click()
        Wait(self.driver, 5).until(ec.element_to_be_clickable((By.XPATH, "//img[@alt=\"Sauce Labs Backpack\"]")))
        bag = self.driver.find_element(By.XPATH, "//img[@alt=\"Sauce Labs Backpack\"]")
        home_page_img = bag.get_attribute("src")
        bag.click()
        Wait(self.driver, 5).until(ec.url_contains("inventory-item"))
        bag = self.driver.find_element(By.XPATH, "//img[@alt=\"Sauce Labs Backpack\"]")
        product_img = bag.get_attribute("src")
        assert home_page_img != product_img


test_class = TestSauce()
# test_class.empty_login()
# test_class.empty_password_login()
# test_class.locked_user_login()
# test_class.product_count()
test_class.add_product_to_cart()
# test_class.visual_user_login()

