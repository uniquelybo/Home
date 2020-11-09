# 登录
from selenium.webdriver.support.wait import WebDriverWait
import sys


class User_Login():
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 5)

    def user_login(self, username, password):
        try:
            self.wait.until(
                lambda driver: self.driver.find_element_by_id("com.ttmv.myhome:id/et_login_phone")).send_keys(username)
            self.wait.until(
                lambda driver: self.driver.find_element_by_id("com.ttmv.myhome:id/et_login_password")).send_keys(
                password)
            self.wait.until(
                lambda driver: self.driver.find_element_by_id("com.ttmv.myhome:id/btn_login_commit")).send_keys(
                username)
        except Exception as ex:
            print("---------登录-问题---------", ex)
            sys.exit()
