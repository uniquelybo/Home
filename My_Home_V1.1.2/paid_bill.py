from selenium.webdriver.common.action_chains import ActionChains


class Paid:
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

    def mouse_move(self):
        # 首页
        self.wait.until(lambda driver: self.driver.find_element_by_xpath("//div/section/aside/div/ul/div[2]")).click()
        # 账单明细
        self.wait.until(lambda driver: self.driver.find_element_by_xpath(
            "//div/section/section/main/div/div/header/div/div[2]/div/div[2]")).click()
        # 已缴费
        paid = self.wait.until(lambda driver: self.driver.find_element_by_xpath("//div/span[text()='已缴费']"))
        # 移动鼠标
        ActionChains(self.driver).move_to_element(paid).perform()
        # 查看
