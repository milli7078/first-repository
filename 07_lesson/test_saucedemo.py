from selenium import webdriver
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
import allure

@allure.id("SKYPRO-1")
@allure.title("Функция сложения в калькуляторе")
def test_order_total():
    with allure.step("Создание драйвера"):
        driver = webdriver.Chrome()
        driver.implicitly_wait(5)

    with allure.step("Авторизация"):
        login = LoginPage(driver)
        login.open()
        login.enter_username("standard_user")
        login.enter_password("secret_sauce")
        login.click_login()

    with allure.step("Добавление товаров в корзину"):
        inventory = InventoryPage(driver)
        inventory.add_backpack()
        inventory.add_tshirt()
        inventory.add_onesie()
        inventory.go_to_cart()

    with allure.step("переход в корзину"):
        cart = CartPage(driver)
        cart.click_checkout()

    with allure.step("Заполнение данных"):
        checkout = CheckoutPage(driver)
        checkout.fill_first_name("Alla")
        checkout.fill_last_name("Davydova")
        checkout.fill_zip("123456")
        checkout.continue_checkout()

    with allure.step("Проверка суммы"):
        total = checkout.get_total()
        assert total.endswith("$58.29"), f"Expected total $58.29, got {total}"

    driver.quit()
