from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from utils import ConfigReader


def get_driver(flag=False):
    driver = None
    option = None
    if flag:
        option = Options()
        option.add_argument("--headless")
    browser = ConfigReader.read_config("browser")
    try:
        match browser:
            case "chrome":

                driver = webdriver.Chrome(options=option)
            case "firefox":
                driver = webdriver.Firefox(options=option)
            case "edge":
                driver = webdriver.Edge(options=option)
            case "safari":
                driver = webdriver.Safari(options=option)
            case _:
                raise Exception("Invalid browser")
    except Exception as e:
        print(e)
    driver.maximize_window()
    driver.implicitly_wait(10)
    return driver


def close_driver(self):
    self.driver.quit()
