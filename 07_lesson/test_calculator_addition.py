import pytest
from selenium import webdriver
from slow_calculator_page import SlowCalculatorPage  # Импорт вашего класса страницы

def test_addition_operation():
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)

    try:
        calc = SlowCalculatorPage(driver)
        calc.open()
        calc.set_delay(45)
        calc.click_button('7')
        calc.click_button('+')
        calc.click_button('8')
        calc.click_button('=')

        calc.wait_for_result("15", timeout=60)
        result = calc.get_result_text()
        assert result == "15", f"Expected result to be 15 but got {result}"

    finally:
        driver.quit()
