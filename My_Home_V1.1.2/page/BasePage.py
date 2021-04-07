#coding=utf-8
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
import time
from selenium import webdriver


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def get_web(self, url):
        self.driver.get(url)

    # 查找元素
    def find_element(self, ele_type, ele_loc):
        try:
            element = self.wait.until(lambda driver: self.driver.find_element(ele_type, ele_loc))
            return element
        except:
            print("------未找到页面元素-------", element)

    # 输入内容
    def input_content(self, element, content):
        element.send_keys(content)

    # 清空内容
    def clear_content(self, element):
        element.clear()

    def close_web(self):
        self.driver.close()
