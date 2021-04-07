class Payment_Name:
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

    def payment_name(self):
        # 首页
        self.wait.until(lambda driver: self.driver.find_element_by_xpath("//div/section/aside/div/ul/div[2]")).click()
        # 添加缴费项
        self.wait.until(lambda driver: self.driver.find_element_by_xpath("//button/span[text()='添加缴费项']")).click()
        # 缴费项名称
        content = [
            '缴费项名称缴费项名称缴费项名称',
            '缴费项名称缴费项名称缴费项名',
            '缴费项名称缴费项名称缴费项',
            '缴费',
            '缴',
            '012345601234567',
            '01234560123456',
            '0123456012345',
            '01',
            '0',
            'abcdefghijklmno',
            'abcdefghijklmn',
            'abcdefghijklm',
            'ab',
            'a',
            '缴费项jfx123',
            '缴费项**&$^'
        ]
        for con in content:
            self.wait.until(lambda driver: self.driver.find_element_by_xpath("//div/section/section/main/div/div/div[3]/div[1]/div/div[2]/form/div[2]/div/div/input")).clear()
            self.wait.until(lambda driver: self.driver.find_element_by_xpath("//div/section/section/main/div/div/div[3]/div[1]/div/div[2]/form/div[2]/div/div/input")).send_keys(con)
            #
            self.wait.until(lambda driver: self.driver.find_element_by_xpath("//div/section/section/main/div/div/div[3]/div[1]/div/div[2]/form/div[2]/label")).click()
            # 查看是否出现隐藏域
            try:
                self.wait.until(lambda driver: self.driver.find_element_by_xpath("//div/section/section/main/div/div/div[3]/div[1]/div/div[2]/form/div[2]/div/div[2]"))
            except:
                print(con, "------内容有问题------")
