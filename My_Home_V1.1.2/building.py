import time


class Building:
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

    def cat_name(self):
        self.wait.until(lambda driver: self.driver.find_element_by_xpath("//ul//li[@id='submenu']/div/div")).click()
        self.wait.until(lambda driver: self.driver.find_element_by_xpath("//*[@id='submenu'][1]/ul/span[1]/li")).click()
        self.wait.until(lambda driver: self.driver.find_element_by_xpath("//div/section/section/main/div/div[2]/div[1]/div[3]/table/tbody/tr[2]/td[14]/div/button")).click()
        content1 = self.wait.until(lambda driver: self.driver.find_element_by_xpath("//div/section/section/main/div/div[2]/div[3]/table/tbody/tr[1]/td[7]/div/button/span")).text
        content2 = self.wait.until(lambda driver: self.driver.find_element_by_xpath("//div/section/section/main/div/div[2]/div[3]/table/tbody/tr[1]/td[8]/div/button/span")).text
        content3 = self.wait.until(lambda driver: self.driver.find_element_by_xpath("//div/section/section/main/div/div[2]/div[3]/table/tbody/tr[1]/td[9]/div/button/span")).text
        if content1 == "强制开启":
            print("-----强制开启按钮-----")
        else:
            print(content1)

        if content2 == "强制关闭":
            print("-----强制关闭按钮-----")
        else:
            print(content2)

        if content3 == "恢复计费":
            print("-----恢复计费按钮-----")
        else:
            print(content3)
