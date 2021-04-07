from selenium import webdriver
from page.BasePage import BasePage
from selenium.webdriver.common.by import By


class Index(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        # 进入登录页面
        super().get_web("http://testmyhomeadmin.cew.cn/#/login")
        # 用户名框
        self.username = super().find_element(By.XPATH, "//div/div[2]/form/div[1]/div/div/input")
        # 密码框
        self.password = super().find_element(By.XPATH, "//div/div[2]/form/div[2]/div/div/input")
        # 登录按钮
        self.login = super().find_element(By.XPATH, "//div/div[2]/form/button")

    # 点击登录
    def click_login(self, username, password):
        self.username.send_keys(username)
        self.password.send_keys(password)
        self.login.click()
