from selenium import webdriver
import unittest
from datetime import datetime
import HtmlTestRunner
import time

import sys
sys.path.append("/Users/hongvt/PycharmProjects/OrangeHrmProject")
from Services.login_by_cookies import LoginByCookies
from Pages.add_employee_page import AddEmployee


class AddNewTest(unittest.TestCase):
    driver = webdriver.Chrome("/Users/hongvt/PycharmProjects/OrangeHrmProject/Drivers/chromedriver")
    url = "https://opensource-demo.orangehrmlive.com/index.php/pim/addEmployee"

    # create instance of add_employee_page
    add_employee = AddEmployee(driver)

    # create instance of datetime to set the unique username
    now = datetime.now()

    # Valid data
    first_name = "Amy"
    middle_name = "Lynn"
    last_name = "Smith"
    username = "User" + now.strftime('%Y%m%d%H%M%S')
    username2 = "User2" + now.strftime('%Y%m%d%H%M%S')
    password = "Password123"
    password_wrong = "password123"

    # invalid data
    id_exist = "0001"
    username_invalid = "o0i1" # 4 chars
    password_invalid = "1234567" # 7 chars
    username_exist = "Admin"

    # image file path
    gif_image = "/Users/hongvt/PycharmProjects/OrangeHrmProject/Files/gif_image.gif"
    over_1MB_image = "/Users/hongvt/PycharmProjects/OrangeHrmProject/Files/over1MB_Photo.PNG"
    under_1MB_jpg_image = "/Users/hongvt/PycharmProjects/OrangeHrmProject/Files/under1MB_image.jpg"
    under_1MB_png_image = "/Users/hongvt/PycharmProjects/OrangeHrmProject/Files/under_1MB_image.png"
    wrong_type_image = "/Users/hongvt/PycharmProjects/OrangeHrmProject/Files/wrong_type_image.tif"

    @classmethod
    def setUpClass(cls):
        # get url by cookies
        cls.login_by_cookies = LoginByCookies()
        cls.login_by_cookies.login_cookies(cls.driver)

        cls.driver.get(cls.url)

        cls.driver.maximize_window()
        cls.driver.implicitly_wait(10)

    @classmethod
    def setUp(self):
        # get url by cookies
        self.driver.refresh()

    # Test default unchecked checkbox
    def test_default_checkbox(self):
        self.assertFalse(self.add_employee.get_status_checked_checkbox())

    def test_checked_checkbox(self):
        # checked checkbox
        if not self.add_employee.get_status_checked_checkbox():
            self.add_employee.click_checkbox()

        # verify visible of elements
        self.assertTrue(self.add_employee.get_status_displayed_username())
        self.assertTrue(self.add_employee.get_status_displayed_password())
        self.assertTrue(self.add_employee.get_status_displayed_confirmPass())
        self.assertTrue(self.add_employee.get_status_displayed_status())

    # Test fail adding employee without login details
    def test_exist_id_add(self):
        # unchecked checkbox
        if self.add_employee.get_status_checked_checkbox():
            self.add_employee.click_checkbox()

        self.add_employee.enter_firstname(self.first_name)
        self.add_employee.enter_lastname(self.last_name)
        self.add_employee.enter_id(self.id_exist)
        self.add_employee.click_btn_save()

        # print(self.add_employee.get_message_fail_to_save())
        self.assertEqual( "Failed To Save: Employee Id Exists", self.add_employee.get_message_fail_to_save())

    def test_over_size_upload(self): # >1 MB
        # unchecked checkbox
        if self.add_employee.get_status_checked_checkbox():
            self.add_employee.click_checkbox()

        self.add_employee.enter_firstname(self.first_name)
        self.add_employee.enter_lastname(self.last_name)
        self.add_employee.upload_file(self.over_1MB_image)
        self.add_employee.click_btn_save()

        # print(self.add_employee.get_message_fail_to_save())
        self.assertEqual("Failed to Save: File Size Exceeded", self.add_employee.get_message_fail_to_save())

    def test_wrong_type_upload(self): # .tif & <1MB
        # unchecked checkbox
        if self.add_employee.get_status_checked_checkbox():
            self.add_employee.click_checkbox()

        self.add_employee.enter_firstname(self.first_name)
        self.add_employee.enter_lastname(self.last_name)
        self.add_employee.upload_file(self.wrong_type_image)
        self.add_employee.click_btn_save()

        # print(self.add_employee.get_message_fail_to_save())
        self.assertEqual("Failed to Save: File Type Not Allowed", self.add_employee.get_message_fail_to_save())

    def test_no_required_fields(self):
        # empty firstname, lastname
        if self.add_employee.get_status_checked_checkbox():
            self.add_employee.click_checkbox()

        self.add_employee.click_btn_save()

        self.assertEqual("Required", self.add_employee.get_message_required_firstname())
        self.assertEqual("Required", self.add_employee.get_message_required_lastname())

    # Test successful adding employee without login details
    def test_success_add_required_fields(self):
        if self.add_employee.get_status_checked_checkbox():
            self.add_employee.click_checkbox()

        self.add_employee.enter_firstname(self.first_name)
        self.add_employee.enter_lastname(self.last_name)
        self.add_employee.click_btn_save()

        # print(self.add_employee.get_text_employee_page())
        self.assertEqual("Personal Details", self.add_employee.get_text_employee_page(), "add failed")

        # back to the add employee page
        self.driver.get(self.url)

    def test_success_add_full_01(self): # .jpg photo
        if self.add_employee.get_status_checked_checkbox():
            self.add_employee.click_checkbox()

        self.add_employee.enter_firstname(self.first_name)
        self.add_employee.enter_lastname(self.last_name)
        self.add_employee.upload_file(self.under_1MB_jpg_image)
        self.add_employee.click_btn_save()

        # print(self.add_employee.get_text_employee_page())
        self.assertEqual("Personal Details", self.add_employee.get_text_employee_page(), "add failed")

        # back to the add employee page
        self.driver.get(self.url)

    def test_success_add_full_02(self):  # .png photo
        if self.add_employee.get_status_checked_checkbox():
            self.add_employee.click_checkbox()

        self.add_employee.enter_firstname(self.first_name)
        self.add_employee.enter_lastname(self.last_name)
        self.add_employee.upload_file(self.under_1MB_png_image)
        self.add_employee.click_btn_save()

        # print(self.add_employee.get_text_employee_page())
        self.assertEqual("Personal Details", self.add_employee.get_text_employee_page(), "add failed")

        # back to the add employee page
        self.driver.get(self.url)

    # Test fail adding employee with login details
    def test_no_required_fields_loginDetail(self):
        # empty first, last, user, password
        if not self.add_employee.get_status_checked_checkbox():
            self.add_employee.click_checkbox()

        self.add_employee.click_btn_save()

        self.assertEqual("Required", self.add_employee.get_message_required_firstname())
        self.assertEqual("Required", self.add_employee.get_message_required_lastname())
        self.assertEqual("Should have at least 5 characters", self.add_employee.get_message_invalid_username())
        self.assertEqual("Should have at least 8 characters", self.add_employee.get_message_invalid_password())

        # print(self.add_employee.get_message_invalid_username())

    def test_invalid_username(self): # 4 digits
        if not self.add_employee.get_status_checked_checkbox():
            self.add_employee.click_checkbox()

        self.add_employee.enter_firstname(self.first_name)
        self.add_employee.enter_lastname(self.last_name)
        self.add_employee.enter_username(self.username_invalid)
        self.add_employee.enter_password(self.password)
        self.add_employee.enter_confirmPassword(self.password)
        self.add_employee.click_btn_save()

        # print(self.add_employee.get_message_invalid_username())
        self.assertEqual("Should have at least 5 characters", self.add_employee.get_message_invalid_username())

    def test_invalid_password(self): # 7 digits
        if not self.add_employee.get_status_checked_checkbox():
            self.add_employee.click_checkbox()

        self.add_employee.enter_firstname(self.first_name)
        self.add_employee.enter_lastname(self.last_name)
        self.add_employee.enter_username(self.username)
        self.add_employee.enter_password(self.password_invalid)
        self.add_employee.enter_confirmPassword(self.password_invalid)
        self.add_employee.click_btn_save()

        # print(self.add_employee.get_message_invalid_password())
        self.assertEqual("Should have at least 8 characters", self.add_employee.get_message_invalid_password())

    def test_wrong_confirmPassword(self):
        # self.driver.refresh()

        if not self.add_employee.get_status_checked_checkbox():
            self.add_employee.click_checkbox()

        self.add_employee.enter_firstname(self.first_name)
        self.add_employee.enter_lastname(self.last_name)
        self.add_employee.enter_username(self.username)
        self.add_employee.enter_password(self.password)
        self.add_employee.enter_confirmPassword(self.password_wrong)
        self.add_employee.click_btn_save()

        # print(self.add_employee.get_message_fail_confirmPassword())
        self.assertEqual("Passwords do not match", self.add_employee.get_message_fail_confirmPassword())

    # Test successful adding employee with login details
    def test_success_add_with_loginDetail_01(self): # required fields, enable status,

        if not self.add_employee.get_status_checked_checkbox():
            self.add_employee.click_checkbox()

        self.add_employee.enter_firstname(self.first_name)
        self.add_employee.enter_lastname(self.last_name)
        self.add_employee.enter_username(self.username)
        self.add_employee.enter_password(self.password)
        self.add_employee.enter_confirmPassword(self.password)
        self.add_employee.click_btn_save()

        # print(self.add_employee.get_text_employee_page())
        self.assertEqual("Personal Details", self.add_employee.get_text_employee_page(), "add failed")

        # back to the add employee page
        self.driver.get(self.url)

    @unittest.skip("I skip this test to check the report")
    def test_success_add_with_loginDetail_02(self):  # full fields, gif photo,  disable status,

        if not self.add_employee.get_status_checked_checkbox():
            self.add_employee.click_checkbox()

        self.add_employee.enter_firstname(self.first_name)
        self.add_employee.enter_lastname(self.last_name)
        self.add_employee.upload_file(self.gif_image)
        self.add_employee.enter_username(self.username2)
        self.add_employee.enter_password(self.password)
        self.add_employee.enter_confirmPassword(self.password)
        self.add_employee.select_disable_status()
        self.add_employee.click_btn_save()

        # print(self.add_employee.get_text_employee_page())
        self.assertEqual("Personal Details", self.add_employee.get_text_employee_page(), "add failed")

        # back to the add employee page
        self.driver.get(self.url)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("test completed")


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="/Users/hongvt/PycharmProjects/OrangeHrmProject/Reports"))