class LoginPage:
    def enter_username(self, username: str) -> None:
        """
        Ввод имени пользователя в поле логина.

        Args:
            username (str): Имя пользователя для ввода.
        """
        self.driver.find_element(*self.USERNAME_INPUT).send_keys(username)
