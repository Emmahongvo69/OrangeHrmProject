from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AddEmployee():

    def __init__(self, driver):

        self.driver = driver

        self.wait = WebDriverWait(driver, 20)

        # locate elements
        self.firstname_textbox_id = "firstName"
        self.middlename_textbox_id = "middleName"
        self.lastname_textbox_id = "lastName"
        self.employeeId_textbox_id = "employeeId"
        self.chooseFile_btn_id = "photofile"
        self.loginDetail_checkbox_id = "chkLogin"

        self.username_textbox_id = "user_name"
        self.password_textbox_id = "user_password"
        self.confirmPassword_textbox_id = "re_password"
        self.status_drpbox_id = "status"
        self.save_btn_id = "btnSave"

        # locate message   //*[@id="frmAddEmp"]/fieldset/ol/li[6]/span
        self.msg_requiredFirst_xpath = '//*[@id="frmAddEmp"]/fieldset/ol/li[1]/ol/li[1]/span'
        self.msg_requiredLast_xpath = '//*[@id="frmAddEmp"]/fieldset/ol/li[1]/ol/li[3]/span'
        self.msg_invalidUser_xpath = '//*[@id="frmAddEmp"]/fieldset/ol/li[5]/span'
        self.msg_invalidPass_xpath = '//*[@id="frmAddEmp"]/fieldset/ol/li[6]/span'
        self.msg_failConfirmPass_xpath = '//*[@id="frmAddEmp"]/fieldset/ol/li[7]/span'
        self.msg_failToSave_xpath = '//*[@id="addEmployeeTbl"]/div'  # message disappear within 2 seconds

        # locate element in page directed after add successfully
        self.employee_page_elm_xpath = '//*[@id="pdMainContainer"]/div[1]/h1'

    def get_status_checked_checkbox(self):
        return self.driver.find_element_by_id(self.loginDetail_checkbox_id).is_selected()

    def get_status_displayed_username(self):
        return self.driver.find_element_by_id(self.username_textbox_id).is_displayed()

    def get_status_displayed_password(self):
        return self.driver.find_element_by_id(self.password_textbox_id).is_displayed()

    def get_status_displayed_confirmPass(self):
        return self.driver.find_element_by_id(self.confirmPassword_textbox_id).is_displayed()

    def get_status_displayed_status(self):
        return self.driver.find_element_by_id(self.status_drpbox_id).is_displayed()

    def clear_fields(self):
        self.driver.find_element_by_id(self.firstname_textbox_id).clear()
        self.driver.find_element_by_id(self.middlename_textbox_id).clear()
        self.driver.find_element_by_id(self.lastname_textbox_id).clear()

        if self.get_status_checked_checkbox():
            self.driver.find_element_by_id(self.username_textbox_id).clear()
            self.driver.find_element_by_id(self.password_textbox_id).clear()
            self.driver.find_element_by_id(self.confirmPassword_textbox_id).clear()

    def enter_firstname(self, firstname):
        self.driver.find_element_by_id(self.firstname_textbox_id).send_keys(firstname)

    def enter_middlename(self, middlename):
        self.driver.find_element_by_id(self.middlename_textbox_id).send_keys(middlename)

    def enter_lastname(self, lastname):
        self.driver.find_element_by_id(self.lastname_textbox_id).send_keys(lastname)

    def enter_id(self, id):
        self.driver.find_element_by_id(self.employeeId_textbox_id).clear()
        self.driver.find_element_by_id(self.employeeId_textbox_id).send_keys(id)

    def upload_file(self, filepath):
        self.driver.find_element_by_id(self.chooseFile_btn_id).send_keys(filepath)

    def click_checkbox(self):
        self.driver.find_element_by_id(self.loginDetail_checkbox_id).click()

    def enter_username(self, username):
        self.driver.find_element_by_id(self.username_textbox_id).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element_by_id(self.password_textbox_id).send_keys(password)

    def enter_confirmPassword(self, confirmPassword):
        self.driver.find_element_by_id(self.confirmPassword_textbox_id).send_keys(confirmPassword)

    def select_disable_status(self):
        Select(self.driver.find_element_by_id(self.status_drpbox_id)).select_by_index(1)

    def select_enable_status(self):
        Select(self.driver.find_element_by_id(self.status_drpbox_id)).select_by_index(0)

    def click_btn_save(self):
        self.driver.find_element_by_id(self.save_btn_id).click()

    def get_message_required_firstname(self):
        return self.driver.find_element_by_xpath(self.msg_requiredFirst_xpath).text

    def get_message_required_lastname(self):
        return self.driver.find_element_by_xpath(self.msg_requiredLast_xpath).text

    def get_message_invalid_username(self):
        return self.driver.find_element_by_xpath(self.msg_invalidUser_xpath).text

    def get_message_invalid_password(self):
        return self.driver.find_element_by_xpath(self.msg_invalidPass_xpath).text

    def get_message_fail_confirmPassword(self):
        return self.driver.find_element_by_xpath(self.msg_failConfirmPass_xpath).text

    def get_message_fail_to_save(self):
        # message need time to be shown, using explicit wait
        self.wait.until(EC.visibility_of_element_located((By.XPATH, self.msg_failToSave_xpath)))
        msg = self.driver.find_element_by_xpath(self.msg_failToSave_xpath).text
        return msg

    def get_text_employee_page(self):
        # return self.driver.find_element_by_xpath(self.employee_page_elm_xpath).text
        self.wait.until(EC.visibility_of_element_located((By.XPATH, self.employee_page_elm_xpath)))
        text = self.driver.find_element_by_xpath(self.employee_page_elm_xpath).text
        return text











