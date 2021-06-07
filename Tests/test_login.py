import unittest
from selenium import webdriver
import HtmlTestRunner
import sys
sys.path.append("/Users/hongvt/PycharmProjects/OrangeHrmProject")

from Pages.login_page import LoginPage  # import class from module
from Pages.home_page import HomePage


class LoginTest(unittest.TestCase):

    # define variables used in all testcases
    driver = webdriver.Chrome("/Users/hongvt/PycharmProjects/OrangeHrmProject/Drivers/chromedriver")
    url = "https://opensource-demo.orangehrmlive.com/"
    username = "Admin"
    password = "admin123"
    password_invalid = "admin124"

    @classmethod
    def setUpClass(cls):
        cls.driver.get(cls.url)
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(10)

    def test_invalid_login(self):
        login_page = LoginPage(self.driver)
        login_page.clear_textfields()
        login_page.enter_username(self.username)
        login_page.enter_password(self.password_invalid)
        login_page.click_login()

        self.assertEqual(login_page.get_message_invalid_login(), "Invalid credentials")

    def test_empty_username(self):
        login_page = LoginPage(self.driver)
        login_page.clear_textfields()
        login_page.enter_password(self.password)
        login_page.click_login()

        self.assertEqual(login_page.get_message_invalid_login(), "Username cannot be empty")

    def test_empty_password(self):
        login_page = LoginPage(self.driver)
        login_page.clear_textfields()
        login_page.enter_username(self.username)
        login_page.click_login()

        self.assertEqual(login_page.get_message_invalid_login(), "Password cannot be empty")

    def test_valid_login(self):
        login_page = LoginPage(self.driver)
        login_page.clear_textfields()
        login_page.enter_username(self.username)
        login_page.enter_password(self.password)
        login_page.click_login()

        home_page = HomePage(self.driver)
        home_page.click_welcome()
        home_page.click_logout()

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("test completed")


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="/Users/hongvt/PycharmProjects/OrangeHrmProject/Reports"))