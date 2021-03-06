from appium import webdriver
import time
import random
from selenium.webdriver.support.wait import WebDriverWait
from addfriends import Addfriend
from read_tt import Readfile

des = {
    "deviceName": "NABDU20407008119",
    "platformName": "Android",
    "platformVersion": "10",
    "appActivity": "com.ttmv.ttlive_client.ui.JPushInitActivity",
    "appPackage": "com.ttmv.bobo_client"
    }
driver = webdriver.Remote('127.0.0.1:4723/wd/hub', des)

wait = WebDriverWait(driver, 5)

for i in range(1, 6):
    wait.until(lambda x: driver.find_element_by_xpath("//*[@text='始终允许']")).click()

wait.until(lambda x: driver.find_element_by_xpath("//*[@text='我的']")).click()

addfriend = Addfriend(driver)
readfile = Readfile()
addfriend.login()
addfriend.add()
print(readfile.lines)
for line in range(0, readfile.lines):
    tt = readfile.get_line_content(line)
    try:
        addfriend.send_request(tt, line)
    except Exception as ex:
        print(ex)
        continue
driver.quit()