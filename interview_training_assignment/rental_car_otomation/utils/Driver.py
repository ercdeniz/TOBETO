import os
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

from utils import ConfigReader


def wait(driver, selector, element, flag="visit", timeout=20):
    if flag == "visit":
        return WebDriverWait(driver, timeout).until(ec.visibility_of_element_located((selector, element)))
    if flag == "click":
        return WebDriverWait(driver, timeout).until(ec.element_to_be_clickable((selector, element)))
    if flag == "url":
        return WebDriverWait(driver, timeout).until(ec.url_to_be(element))


def multiple_wait(driver, selector, element, flag="visit", timeout=20):
    if flag == "visit":
        return WebDriverWait(driver, timeout).until(ec.visibility_of_all_elements_located((selector, element)))


def screenshot(driver, dir_name, file_name, wait_time=0):
    screenshot_dir = dir_name
    os.makedirs(screenshot_dir, exist_ok=True)
    screenshot_path = os.path.join(screenshot_dir, file_name)
    sleep(wait_time)
    driver.save_screenshot(screenshot_path)


def get_driver():
    driver = None
    option = None
    flag = ConfigReader.read_config("headless")

    if flag == "1":
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
