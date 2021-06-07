class LoginPage():

    def __init__(self, driver):
        self.driver = driver

        # locator
        self.textbox_username_id = "txtUsername"
        self.textbox_password_id = "txtPassword"
        self.btn_login_id = "btnLogin"
        self.message_id = "spanMessage"

    def clear_textfields(self):
        self.driver.find_element_by_id(self.textbox_username_id).clear()
        self.driver.find_element_by_id(self.textbox_password_id).clear()

    def enter_username(self, username):
        self.driver.find_element_by_id(self.textbox_username_id).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element_by_id(self.textbox_password_id).send_keys(password)

    def click_login(self):
        self.driver.find_element_by_id(self.btn_login_id).click()

    def get_message_invalid_login(self):
        msg = self.driver.find_element_by_id(self.message_id).text
        return msg








