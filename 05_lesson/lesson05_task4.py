from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


options = Options()
options.add_argument("--width=1024")
options.add_argument("--height=768")
driver = webdriver.Firefox(service=FirefoxService(), options=options)

try:

    driver.get("http://the-internet.herokuapp.com/login")

    wait = WebDriverWait(driver, 10)

    username_field = wait.until(EC.presence_of_element_located((By.ID, "username")))
    password_field = wait.until(EC.presence_of_element_located((By.ID, "password")))


    username_field.send_keys("tomsmith")  # по инструкции сайта :contentReference[oaicite:1]{index=1}
    password_field.send_keys("SuperSecretPassword!")  # по инструкции сайта :contentReference[oaicite:2]{index=2}


    login_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
    login_button.click()


    flash = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".flash.success")))


    print(flash.text.strip())

finally:

    driver.quit()
