from page.BasePage import BasePage
from selenium.webdriver.common.by import By


class User_List(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    # 设备详情查看按钮
    def choose_cat(self, num):
        return self.find_element(By.XPATH, "//div/section/section/main/div/div[2]/div[1]/div[3]/table/tbody/tr[%d]/td[14]/div/button" % num)
