from selenium.webdriver.support.wait import WebDriverWait
import time


class Addfriend:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 5)

    def add(self):
        self.wait.until(lambda driver: self.driver.find_element_by_id("com.ttmv.bobo_client:id/btn_filmTVLayout")).click()
        self.wait.until(lambda driver: self.driver.find_element_by_id("com.ttmv.bobo_client:id/btnRight_contacts")).click()
        self.wait.until(lambda driver: self.driver.find_element_by_id("com.ttmv.bobo_client:id/addfriend_layout")).click()
        self.wait.until(lambda driver: self.driver.find_element_by_id("com.ttmv.bobo_client:id/searchFriendLayout")).click()

    def login(self):
        time.sleep(2)
        self.driver.find_element_by_id("com.ttmv.bobo_client:id/login_userName_text").send_keys("18334783765")
        self.driver.find_element_by_id("com.ttmv.bobo_client:id/login_pwd_text").send_keys("123456")
        self.driver.find_element_by_id("com.ttmv.bobo_client:id/lgoin_btn_login").click()

    def send_request(self, tt, line):
        self.wait.until(lambda driver: self.driver.find_element_by_id("com.ttmv.bobo_client:id/edit_search")).send_keys(tt)
        self.wait.until(lambda driver: self.driver.find_element_by_id("com.ttmv.bobo_client:id/btn_search")).click()
        text = self.wait.until(lambda driver: self.driver.find_element_by_id("com.ttmv.bobo_client:id/addBtn")).text
        if text == "已添加":
            self.driver.find_element_by_id("com.ttmv.bobo_client:id/edit_search").clear()
        else:
            self.wait.until(lambda driver: self.driver.find_element_by_id("com.ttmv.bobo_client:id/addBtn")).click()
            try:
                self.wait.until(lambda driver: self.driver.find_element_by_id("com.ttmv.bobo_client:id/btnRight")).click()
            except:
                print("-----添加失败------", line)
