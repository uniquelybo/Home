from page.BasePage import BasePage
from selenium.webdriver.common.by import By


class Device_Details(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def choose_device(self, num):
        return self.find_element(By.XPATH, "//div/section/section/main/div/div[2]/div[3]/table/tbody/tr[%d]" % num)

    def choose_device_control(self, num1, num2):
        return self.find_element(By.XPATH, "//div/section/section/main/div/div[2]/div[3]/table/tbody/tr[%d]/td[%d]/div/button" % (num1, (num2+6)))
