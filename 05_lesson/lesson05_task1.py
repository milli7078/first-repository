from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


chrome_options = Options()
chrome_options.add_argument("--start-maximized")  # Открыть окно браузера в максимальном размере



service = Service()


driver = webdriver.Chrome(service=service, options=chrome_options)

try:

    driver.get("http://uitestingplayground.com/classattr")

    # Явное ожидание появления кнопки с классом 'btn-primary'
    wait = WebDriverWait(driver, 10)
    button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "btn-primary")))

    # Клик по кнопке
    button.click()


    time.sleep(2)


