from pages import page_reservation
from utils import Driver, ConfigReader as cr


class TestReservation:
    def setup_method(self):
        self.driver = Driver.get_driver()
        self.driver.get(cr.read_config("url_search"))
        self.page = page_reservation.PageReservation(self.driver)

    def teardown_method(self):
        self.driver.quit()

    def test_reservation_cancel(self):
        self.page.home()
        self.driver.execute_script("arguments[0].click();", self.page.button_reservation)
        self.page.reservation_popup()
        self.driver.execute_script("arguments[0].click();", self.page.button_reservation_cancel)
        self.page.reservation_cancel_page()
        self.page.approval_number.send_keys("123456")
        self.page.email.send_keys("invalid_email@gmail.com")
        self.page.cancellation_reason.send_keys("Test")
        self.page.recaptcha_func()
        self.driver.execute_script("arguments[0].click();", self.page.button_submit)
        file_name = "reservation_cancel.png"
        if cr.read_config("headless") == "1":
            file_name = "reservation_cancel_headless.png"
        Driver.screenshot(self.driver, "../screenshots/reservation", file_name, 2)
