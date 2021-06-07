import pickle
import os
import time

from Pages.login_page import LoginPage


class LoginByCookies():

    location = "/Users/hongvt/PycharmProjects/OrangeHrmProject/Files/cookies.txt"
    domain = "https://opensource-demo.orangehrmlive.com/index.php/dashboard"

    def save_cookies(self, driver):
        try:
            file = open(self.location, "wb")
            pickle.dump(driver.get_cookies(), file)
        except:
            print("something went wrong while writing file")
        finally:
            file.close()

    def load_cookies(self, driver): # domain is url to send cookies (login page)
        try:
            file = open(self.location, "rb")
            cookies = pickle.load(file)
        except:
            print("something went wrong while reading file")
        finally:
            file.close()

        driver.get(self.domain)
        driver.delete_all_cookies()  # delete exist cookies before load the new one

        for cookie in cookies:
            driver.add_cookie(cookie)

    def login_cookies(self, driver):  # url want to launch

        # login to the page
        driver.get('https://opensource-demo.orangehrmlive.com/')

        login_page = LoginPage(driver)
        login_page.clear_textfields()
        login_page.enter_username("Admin")
        login_page.enter_password("admin123")
        login_page.click_login()
        time.sleep(2)

        # save cookies to file (if exist then remove file before add new file)
        if os.path.exists("/Users/hongvt/PycharmProjects/OrangeHrmProject/Files/cookies.txt"):
            os.remove("/Users/hongvt/PycharmProjects/OrangeHrmProject/Files/cookies.txt")

        self.save_cookies(driver)
        time.sleep(2)

        # load cookie from file to login page
        self.load_cookies(driver)