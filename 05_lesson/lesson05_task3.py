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

    driver.get("http://the-internet.herokuapp.com/inputs")

    wait = WebDriverWait(driver, 10)

    input_field = wait.until(EC.presence_of_element_located((By.TAG_NAME, "input")))


    input_field.send_keys("Sky")


    input_field.clear()


    input_field.send_keys("Pro")

finally:

    driver.quit()
