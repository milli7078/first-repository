from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SlowCalculatorPage:
    def __init__(self, driver):
        self.driver = driver
        self.delay_input = (By.ID, "delay")
        self.result_display = (By.CSS_SELECTOR, "div.screen")

    def open(self):
        self.driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    def set_delay(self, seconds):
        delay_field = self.driver.find_element(*self.delay_input)
        delay_field.clear()
        delay_field.send_keys(str(seconds))

    def click_button(self, value):
        btn = self.driver.find_element(By.XPATH, f"//span[text()='{value}']")
        btn.click()

    def wait_for_result(self, expected_result, timeout=60):
        WebDriverWait(self.driver, timeout).until(
            EC.text_to_be_present_in_element(self.result_display, expected_result)
        )

    def get_result_text(self):
        return self.driver.find_element(*self.result_display).text
