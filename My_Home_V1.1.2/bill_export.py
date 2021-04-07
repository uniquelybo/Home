class Bill_Export:
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

    def export(self):
        # 首页
        self.wait.until(lambda driver: self.driver.find_element_by_xpath("//div/section/aside/div/ul/div[2]")).click()
        # 账单明细
        self.wait.until(lambda driver: self.driver.find_element_by_xpath(
            "//div/section/section/main/div/div/header/div/div[2]/div/div[2]")).click()
        # 导出
        self.wait.until(lambda driver: self.driver.find_element_by_xpath("//button/span[text()='导出']")).click()
