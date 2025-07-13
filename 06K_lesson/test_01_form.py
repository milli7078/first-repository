import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

def test_form_validation():
    driver = webdriver.Chrome()
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

    driver.find_element(By.NAME, "first-name").send_keys("Иван")
    driver.find_element(By.NAME, "last-name").send_keys("Петров")
    driver.find_element(By.NAME, "address").send_keys("Ленина, 55-3")
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "input[type='email']"))
    ).send_keys("test@skypro.com")
    driver.find_element(By.NAME, "phone").send_keys("+7985899998787")
    driver.find_element(By.NAME, "city").send_keys("Москва")
    driver.find_element(By.NAME, "country").send_keys("Россия")
    driver.find_element(By.NAME, "job-position").send_keys("QA")
    driver.find_element(By.NAME, "company").send_keys("SkyPro")

    form = driver.find_element(By.TAG_NAME, "form")
    form.submit()

    try:
        success = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".success-message, .alert-success"))
        )
        print("✅ Форма успешно отправлена:", success.text)
    except TimeoutException:
        print("⚠️ Нет подтверждения успеха, проверяем ошибки…")
        try:
            error = driver.find_element(By.CSS_SELECTOR, ".error-message, .alert-danger")
            print("❌ Обнаружена ошибка:", error.text)
        except NoSuchElementException:
            print("❌ Сообщение об ошибке не найдено — проверьте поведение формы вручную.")

    time.sleep(5)
    driver.quit()
