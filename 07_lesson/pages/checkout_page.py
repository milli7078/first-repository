from selenium.webdriver.common.by import By

class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver

    def fill_first_name(self, name):
        self.driver.find_element(By.ID, "first-name").send_keys(name)

    def fill_last_name(self, last):
        self.driver.find_element(By.ID, "last-name").send_keys(last)

    def fill_zip(self, zip_code):
        self.driver.find_element(By.ID, "postal-code").send_keys(zip_code)

    def continue_checkout(self):
        self.driver.find_element(By.ID, "continue").click()

    def get_total(self):
        return self.driver.find_element(By.CLASS_NAME, "summary_total_label").text
