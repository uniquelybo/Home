class Apply_Cost_Type:
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

    def apply_cost_type(self):
        # 首页
        self.wait.until(lambda driver: self.driver.find_element_by_xpath("//div/section/aside/div/ul/div[2]")).click()
        # 财务管理
        self.wait.until(lambda driver: self.driver.find_element_by_xpath(
            "//div/section/section/main/div/div/header/div/div[1]/div/div[2]")).click()
        # 申请
        self.wait.until(lambda driver: self.driver.find_element_by_xpath(
            "//div/section/section/main/div/div[2]/div[2]/button")).click()
        # 费用类型
        self.wait.until(lambda driver: self.driver.find_element_by_xpath("//div/section/section/main/div/form/div[3]/div[2]/div/div/div[2]/input")).click()
