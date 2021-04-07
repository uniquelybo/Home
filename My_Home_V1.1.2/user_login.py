# class User_Login:
#     def __init__(self, driver, wait):
#         self.driver = driver
#         self.wait = wait
#
#     def login(self):
#         self.wait.until(lambda driver: self.driver.find_element_by_xpath("//input[@type='text']")).send_keys("ceshixiaoqu1")
#         self.driver.find_element_by_xpath("//input[@type='password']").send_keys("123456")
#         self.driver.find_element_by_xpath("//button[@type='button']").click()


import requests
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
# response = requests.get(url="http://testmyhomeapi.cew.cn/gs/client/number/login/tuishou/tuishou123" , params={"name": "tuishou", "password": "tuishou123"})
# print(response.)

# response = requests.get(url="http://testmyhomeadmin.cew.cn/#/index")
option = webdriver.ChromeOptions()
option.add_argument("--headless")
driver = webdriver.Chrome(executable_path="/Users/tuishoutest/Downloads/chromedriver", options=option)
response = driver.get("http://testmyhomeadmin.cew.cn/")
print("--------")
print(response)
driver.quit()
print()
