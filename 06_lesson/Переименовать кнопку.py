from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time


chrome_options = Options()
chrome_options.add_argument("--start-maximized")


service = Service('путь/к/chromedriver')  # Замените на актуальный путь


driver = webdriver.Chrome()

try:

    driver.get("http://uitestingplayground.com/textinput")



    input_field = driver.find_element(By.ID, "newButtonName")
    input_field.send_keys("SkyPro")


    button = driver.find_element(By.ID, "updatingButton")
    button.click()


    time.sleep(1)


    updated_text = button.text
    print(f"Текст кнопки после нажатия: \"{updated_text}\"")

finally:

    driver.quit()
