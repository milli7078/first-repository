from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()

try:

    driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")

    wait = WebDriverWait(driver, 10)


    third_img_locator = (By.XPATH, "(//img)[3]")
    third_img = wait.until(EC.presence_of_element_located(third_img_locator))

    wait.until(lambda d: third_img.get_attribute("src") and third_img.get_attribute("src").strip())


    src_value = third_img.get_attribute("src")


    print("SRC третьей картинки:", src_value)

finally:
    driver.quit()
