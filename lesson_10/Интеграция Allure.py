import allure

@allure.step("Вводим логин: {username}")
def enter_username(username):
    ...

with allure.step("Проверяем, что кнопка активна"):
    assert button.is_enabled()
