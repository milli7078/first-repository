import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_slow_calculator():

    options = Options()
    options.add_argument("--start-maximized")

    driver = webdriver.Chrome(options=options)
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    try:
        delay_input = driver.find_element(By.ID, "delay")
        delay_input.clear()
        delay_input.send_keys("45")

        for char in ['7', '+', '8', '=']:
            button = driver.find_element(By.XPATH, f"//span[text()='{char}']")
            button.click()

        WebDriverWait(driver, 60).until(
            EC.text_to_be_present_in_element((By.CLASS_NAME, "screen"), "15")
        )

        result = driver.find_element(By.CLASS_NAME, "screen").text
        assert result == "15", f"Ожидалось '15', но получено '{result}'"

    finally:
        driver.quit()
