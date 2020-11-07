# 登录

class User_Login(object):

    def __init__(self, driver):
        self.driver = driver

    def user_login(self, username, password):
        self.driver.find_element_by_id("com.ttmv.myhome:id/et_login_phone").send_keys(username)
        self.driver.find_element_by_id("com.ttmv.myhome:id/et_login_password").send_keys(password)
        self.driver.find_element_by_id("com.ttmv.myhome:id/btn_login_commit").click()
