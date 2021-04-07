from page.BasePage import BasePage
from selenium.webdriver.common.by import By


class Financial_Management(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.apply = self.find_element(By.XPATH, "//*[@id=’app‘]/div/section/section/main/div/div[2]/div[2]/button/span")

    def apply_page(self):
        self.apply = self.find_element(By.XPATH, "//*[@id='app']/div/section/section/main/div/form/div[3]/div[2]/div/div/div[2]/input")
        self.print = self.find_element(By.XPATH, "//*[@id='app']//*[text()='打印']")


    def expense_type_page(self):
        pass


