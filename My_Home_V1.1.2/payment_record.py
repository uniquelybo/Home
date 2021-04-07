from selenium import webdriver


class Payment_Record:
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

    def cat_pay_type(self):
        # 首页
        self.wait.until(lambda driver: self.driver.find_element_by_xpath("//div/section/aside/div/ul/div[2]")).click()
        # 缴费记录
        self.wait.until(lambda driver: self.driver.find_element_by_xpath("//div/section/section/main/div/div/header/div/div[3]/div/div[2]")).click()
        try:
            # 查找内容
            content = self.wait.until(lambda driver: self.driver.find_element_by_xpath("//div/section/section/main/div/div[2]/div[1]/div[2]/table/thead/tr/th/div[text()='缴费人']")).text
            print("-------存在%s-------" % content)
        except:
            print("-----支付方式-----")
