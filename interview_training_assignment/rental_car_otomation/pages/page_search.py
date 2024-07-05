from selenium.webdriver.common.by import By

from utils import Driver


class PageSearch:
    from_where = None
    choose_from_where = None
    age = None
    choose_age = None
    button_search = None

    def __init__(self, driver):
        self.driver = driver

    def home(self):
        self.from_where = Driver.wait(self.driver, By.XPATH, "//input[@id='searchDomesticWrap-input']")
        self.age = Driver.wait(self.driver, By.XPATH, "//input[@placeholder='Yaş seçiniz']")
        self.button_search = Driver.wait(self.driver, By.XPATH,
                                         "//button[@class='btn btn-brand btn-full btnApplyFilter']")

    def choose_place_func(self):
        self.choose_from_where = Driver.wait(self.driver, By.XPATH, "//a[span[text()='Ankara YHT Gar']]")

    def choose_age_func(self):
        self.choose_age = Driver.wait(self.driver, By.XPATH, "//a[@value='21-24']")
