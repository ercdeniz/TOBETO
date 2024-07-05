from pages import page_search
from utils import Driver, ConfigReader as cr


class TestSearch:
    def setup_method(self):
        self.driver = Driver.get_driver()
        self.driver.get(cr.read_config("url_search"))
        self.page = page_search.PageSearch(self.driver)

    def teardown_method(self):
        self.driver.quit()

    def test_search_page(self):
        self.page.home()
        self.page.from_where.clear()
        self.page.from_where.send_keys("Ankara YHT Gar")
        self.page.choose_place_func()
        self.driver.execute_script("arguments[0].click();", self.page.choose_from_where)
        self.page.age.click()
        self.page.choose_age_func()
        self.driver.execute_script("arguments[0].click();", self.page.choose_age)
        self.driver.execute_script("arguments[0].click();", self.page.button_search)
        file_name = "search.png"
        if cr.read_config("headless") == "1":
            file_name = "search_headless.png"
        Driver.screenshot(self.driver, "../screenshots/search", file_name, 2)
