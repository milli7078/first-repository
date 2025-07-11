from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Укажите путь к chromedriver, если не в PATH
chrome_options = Options()
chrome_options.add_argument("--start-maximized")
driver = webdriver.Chrome(service=ChromeService(), options=chrome_options)

try:
    driver.get("http://uitestingplayground.com/dynamicid")
    wait = WebDriverWait(driver, 20)

    # Ждём появления синей кнопки по классу btn-primary, потом кликаем
    blue_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "btn-primary")))
    blue_button.click()

finally:
    driver.quit()
