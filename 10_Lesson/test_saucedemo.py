from selenium import webdriver
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage

def test_order_total():
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)

    login = LoginPage(driver)
    login.open()
    login.enter_username("standard_user")
    login.enter_password("secret_sauce")
    login.click_login()

    inventory = InventoryPage(driver)
    inventory.add_backpack()
    inventory.add_tshirt()
    inventory.add_onesie()
    inventory.go_to_cart()

    cart = CartPage(driver)
    cart.click_checkout()

    checkout = CheckoutPage(driver)
    checkout.fill_first_name("Alla")
    checkout.fill_last_name("Davydova")
    checkout.fill_zip("123456")
    checkout.continue_checkout()

    total = checkout.get_total()
    assert total.endswith("$58.29"), f"Expected total $58.29, got {total}"

    driver.quit()
