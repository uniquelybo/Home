from page.BasePage import BasePage
from selenium.webdriver.common.by import By


class Set_Payment_Items(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.payment_name = self.find_element(By.XPATH, "//*[@id='app']/div/section/section/main/div/div/div[3]/div[1]/div/div[2]/form/div[2]/div/div/input")
        self.submit = self.find_element(By.XPATH, "//*[@id='app']/div/section/section/main/div/div/div[3]/div[1]/div/div[2]/form/div[9]/div/button[2]/span")

    def except_element(self, label_name):
        return self.find_element(By.XPATH, "//*[@id='app']/div/section/section/main//div/label[text()='%r']/following-sibling::div/div[2]" % label_name)
