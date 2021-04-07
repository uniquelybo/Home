class Finance_Form_Print:
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

    def form_print(self):
        # 首页
        self.wait.until(lambda driver: self.driver.find_element_by_xpath("//div/section/aside/div/ul/div[2]")).click()
        # 财务管理
        self.wait.until(lambda driver: self.driver.find_element_by_xpath(
            "//div/section/section/main/div/div/header/div/div[1]/div/div[2]")).click()
        # 申请
        self.wait.until(lambda driver: self.driver.find_element_by_xpath("//div/section/section/main/div/div[2]/div[2]/button")).click()
        # 打印
        self.wait.until(lambda driver: self.driver.find_element_by_xpath("//button/span[text()='打印']")).click()
