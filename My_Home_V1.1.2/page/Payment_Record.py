from page.BasePage import BasePage
from selenium.webdriver.common.by import By


class Payment_Record(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.export = self.find_element(By.XPATH, "//div/section/section/main/div/div[1]/div[2]/button/span")
        self.search = self.find_element(By.XPATH, "//*[@id='app']/div/section/section/main/div/div[1]/div[1]/input")
        self.start_time = self.find_element(By.XPATH, "//*[@id='app']/div/section/section/main/div/div[1]/div[2]/input")
        self.end_time = self.find_element(By.XPATH, "//*[@id='app']/div/section/section/main/div/div[1]/div[3]/input")
        self.reset = self.find_element(By.XPATH, "//*[@id='app']/div/section/section/main/div/div[1]/button/span")

    def start_time_page(self):
        self.input_start_time = self.find_element(By.XPATH, "/html/body/div[5]/div[1]/div/div[1]/span[1]/div/input")
        self.input_start_time_click = self.find_element(By.XPATH, "/html/body/div[5]/div[2]/button[2]/span")

    def end_time_page(self):
        self.input_end_time = self.find_element(By.XPATH, "/html/body/div[5]/div[1]/div/div[1]/span[1]/div/input")
        self.input_end_time_now = self.find_element(By.XPATH, "/html/body/div[5]/div[2]/button[1]/span")
        self.input_end_time_click = self.find_element(By.XPATH, "/html/body/div[5]/div[2]/button[2]/span")

    def find_menu_by_str(self, con):
        return self.find_element(By.XPATH, "//*[@id='app']/div/section/section/main/div/div[2]/div[1]/div[2]/table/thead/tr/th[1]/div[text()='%r']" % con)

    def find_menu_by_int(self, num):
        return self.find_element(By.XPATH, "//*[@id='app']/div/section/section/main/div/div[2]/div[1]/div[2]/table/thead/tr/th[%d]" % num)
