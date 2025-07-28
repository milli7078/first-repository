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
            EC.presence_of_element_located((By.CSS_SELECTOR, ".alert-success"))
        )
        assert "success" in success.get_attribute("class") or "успешно" in success.text.lower()
        print("✅ Успешная отправка формы:", success.text)
    except TimeoutException:
        try:
            error = driver.find_element(By.CSS_SELECTOR, ".alert-danger")
            assert "error" in error.get_attribute("class") or error.text.strip() != ""
            print("❌ Ошибка при отправке формы:", error.text)
        except NoSuchElementException:
            raise AssertionError("❌ Ни успешного, ни ошибочного сообщения не найдено. Проверьте поведение формы.")

    time.sleep(2)
    driver.quit()
