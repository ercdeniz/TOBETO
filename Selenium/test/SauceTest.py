import pytest
from selenium.webdriver.common.by import By

from pages import SaucePage as sp
from utils import ConfigReader as cr
from utils import Constants as c
from utils import Driver


def replace_and_convert(element):
    price = float(element.replace("$", ""))
    return price


class TestSauceDemo:
    def setup_method(self):
        self.driver = Driver.get_driver(True)
        self.driver.get(cr.read_config("urlSauce"))
        self.page = sp.SaucePage(self.driver)

    def teardown_method(self):
        self.driver.quit()

    @pytest.mark.skip()
    def test_demo(self):
        self.driver.get(cr.read_config("urlGoogle"))
        assert self.driver.title == "Google"

    def test_empty_login(self):
        self.page.login_button.click()
        error_message = self.driver.find_element(By.XPATH, "//h3[@data-test=\"error\"]")
        assert error_message.text == c.error_user_name

    def test_empty_password_login(self):
        self.page.user_name.send_keys("standard_user")
        self.page.login_button.click()
        error_message = self.driver.find_element(By.XPATH, "//h3[@data-test=\"error\"]")
        assert error_message.text == c.error_password

    def test_locked_user_login(self):
        self.page.user_name.send_keys("locked_out_user")
        self.page.password.send_keys("secret_sauce")
        self.page.login_button.click()
        error_message = self.driver.find_element(By.XPATH, "//h3[@data-test=\"error\"]")
        assert error_message.text == c.error_locked_user

    def test_product_count(self):
        self.page.user_name.send_keys("standard_user")
        self.page.password.send_keys("secret_sauce")
        self.page.login_button.click()
        assert self.driver.current_url == c.url_inventory
        self.page.home_page()
        assert len(self.page.products) == 6

    def test_add_product_to_cart(self):
        self.page.user_name.send_keys("standard_user")
        self.page.password.send_keys("secret_sauce")
        self.page.login_button.click()
        self.page.home_page()
        count = 0
        for product in self.page.products:
            price = replace_and_convert(product.find_element(By.CLASS_NAME, "inventory_item_price").text)
            if price < 20.00:
                add_to_cart = product.find_element(By.XPATH, "//button[contains(@data-test, 'add-to-cart')]")
                add_to_cart.click()
                count += 1
        self.page.product_added_on_home_page()
        num_of_orders = int(self.page.cart_badge.text)
        assert count == num_of_orders

    def test_visual_user_login(self):
        self.page.user_name.send_keys("visual_user")
        self.page.password.send_keys("secret_sauce")
        self.page.login_button.click()
        self.page.home_page()
        home_page_img = self.page.product_bag.get_attribute("src")
        self.page.product_bag.click()
        self.page.product_page()
        product_img = self.page.product_bag.get_attribute("src")
        assert home_page_img != product_img
