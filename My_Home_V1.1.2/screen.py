class Screen:
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

    def screen_bool(self):
        # 首页
        self.wait.until(lambda driver: self.driver.find_element_by_xpath("//div/section/aside/div/ul/div[2]")).click()
        # 账单明细
        self.wait.until(lambda driver: self.driver.find_element_by_xpath(
            "//div/section/section/main/div/div/header/div/div[2]/div/div[2]")).click()
        # 是否存在
        try:
            # 查询
            self.wait.until(lambda driver: self.driver.find_element_by_xpath("//div/span[text()='查询:']"))
        except:
            print("------不存在查询------")
        try:
            # 缴费时间范围
            self.wait.until(lambda driver: self.driver.find_element_by_xpath("//div/span[text()='缴费时间范围:']"))
        except:
            print("------不存在缴费时间范围------")
        try:
            # 重置筛选按钮
            self.wait.until(lambda driver: self.driver.find_element_by_xpath("//button/span[text()='重置筛选']"))
        except:
            print("------不存在重置筛选按钮-------")

        # 首页
        self.wait.until(
            lambda driver: self.driver.find_element_by_xpath("//div/section/aside/div/ul/div[2]")).click()
        # 缴费记录
        self.wait.until(lambda driver: self.driver.find_element_by_xpath(
            "//div/section/section/main/div/div/header/div/div[3]/div/div[2]")).click()
        # 是否存在
        try:
            # 查询
            self.wait.until(lambda driver: self.driver.find_element_by_xpath("//div/span[text()='查询:']"))
        except:
            print("------不存在查询------")
        try:
            # 缴费时间范围
            self.wait.until(lambda driver: self.driver.find_element_by_xpath("//div/span[text()='缴费时间范围:']"))
        except:
            print("------不存在缴费时间范围------")
        try:
            # 重置筛选按钮
            self.wait.until(lambda driver: self.driver.find_element_by_xpath("//button/span[text()='重置筛选']"))
        except:
            print("------不存在重置筛选按钮-------")
