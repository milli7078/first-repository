from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()

try:

    driver.get("http://uitestingplayground.com/ajax")


    blue_button = driver.find_element(By.CLASS_NAME, "btn-primary")
    blue_button.click()


    wait = WebDriverWait(driver, 15)  # ожидание до 10 секунд
    green_box = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "bg-success")))


    print(green_box.text)

finally:

    driver.quit()
