from page.BasePage import BasePage
from selenium.webdriver.common.by import By


class First_Page(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        # 首页按钮
        self.index_page = self.find_element(By.XPATH, "//div/section/aside/div/ul/div[2]")
        # 财务管理
        self.finance = self.find_element(By.XPATH, "//div/section/section/main/div/div/header/div/div[1]/div/div[2]")
        # 账单明细
        self.bill = self.find_element(By.XPATH, "//div/section/section/main/div/div/header/div/div[2]/div/div[2]")
        # 缴费记录
        self.pay = self.find_element(By.XPATH, "//div/section/section/main/div/div/header/div/div[3]/div/div[2]")
        # 楼层信息
        self.floor = self.find_element(By.XPATH, "//div/section/section/main/div/div/header/div/div[4]/div/div[2]")
        # 第一楼
        # self.first_floor = self.find_element(By.XPATH, "//*[@id='submenu'][1]")
        # 添加缴费项
        self.add_payment = self.find_element(By.XPATH, "//*[@id='pane-Payment']/div[1]/button[1]/span")

    # 楼号
    def choose_floor(self, num):
        return self.find_element(By.XPATH, "//ul/li[%d]/div/div/span" % num)

    # 单元号
    def choose_unit(self, num):
        return self.find_element(By.XPATH, "//ul/li/ul/span[%d]/li" % num)
