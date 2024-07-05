from selenium.webdriver.common.by import By

from utils import Driver


class PageReservation:
    button_reservation = None
    button_reservation_cancel = None
    approval_number = None
    email = None
    cancellation_reason = None
    button_submit = None

    def __init__(self, driver):
        self.driver = driver

    def home(self):
        self.button_reservation = Driver.wait(self.driver, By.XPATH, "//a[text()='Rezervasyon']")

    def reservation_popup(self):
        self.button_reservation_cancel = Driver.wait(self.driver, By.CSS_SELECTOR,
                                                     "a.gtmheader[href=\"/rezervasyon-iptal-formu\"]")

    def reservation_cancel_page(self):
        self.approval_number = Driver.wait(self.driver, By.XPATH, "//input[@id=\"ApprovalNumber\"]")
        self.email = Driver.wait(self.driver, By.XPATH, "//input[@id=\"email\"]")
        self.cancellation_reason = Driver.wait(self.driver, By.XPATH, "//input[@id=\"ReservationCancellationReason\"]")
        self.button_submit = Driver.wait(self.driver, By.XPATH, "//button[@id=\"ReservationCancellationBtn\"]")

    def recaptcha_func(self):
        div_recaptcha = Driver.wait(self.driver, By.CSS_SELECTOR, "div.form-action.d-flex.justify-content-end")
        iframe = div_recaptcha.find_element(By.TAG_NAME, "iframe")
        self.driver.switch_to.frame(iframe)
        button_recaptcha = Driver.wait(self.driver, By.CSS_SELECTOR, "div.recaptcha-checkbox-border")
        self.driver.execute_script("arguments[0].click();", button_recaptcha)
        self.driver.switch_to.default_content()
