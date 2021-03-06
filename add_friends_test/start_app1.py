from appium import webdriver
import sys
from addfriends import Addfriend
from selenium.webdriver.support.wait import WebDriverWait
from passfriends import PassFriends
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

try:
    for i in range(1, 6):
        wait.until(lambda x: driver.find_element_by_xpath("//*[@text='始终允许']")).click()
except:
    pass
passfriends = PassFriends(driver)
readfile = Readfile()
addfriend = Addfriend(driver)

print(readfile.lines)
for line in range(0, readfile.lines):
    tt = readfile.get_line_content(line)
    bool1 = True
    while bool1:
        try:
            passfriends.bb_login(tt)
            bool1 = False
        except Exception as e:
            print("-----登录失败-----", e)
            driver.back()
    try:
        # passfriends.newfriend()
        addfriend.add()
    except:
        print("----无新朋友----")
        sys.exit()
    passfriends.pass_request(10242446)
    driver.back()
    driver.back()
    try:
        # passfriends.pass_request()
        passfriends.logout()
    except Exception as ex:
        print(ex)
        continue
driver.quit()
