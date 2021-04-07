from appium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
import time

desired_caps = {
    "deviceName": "127.0.0.1:4723",
    "platformName": "Android",
    "platformVersion": "10",
    "appActivity": "com.ttmv.myhome.ui.activity.SplashActivity",
    "appPackage": "com.ttmv.myhome"
}
driver = webdriver.Remote("127.0.0.1:4723/wd/hub", desired_caps)
wait = WebDriverWait(driver, 60)
wait.until(lambda dri: driver.find_element_by_id("com.ttmv.myhome:id/btn_ok")).click()
for i in range(1, 5):
    try:
        wait.until(lambda x: driver.find_element_by_xpath("//*[@text='始终允许']")).click()
    except:
        wait.until(lambda x: driver.find_element_by_xpath("//*[@text='仅使用期间允许']")).click()
wait.until(lambda x: driver.find_element_by_id("com.ttmv.myhome:id/et_login_phone")).send_keys("18735159367")
wait.until(lambda x: driver.find_element_by_id("com.ttmv.myhome:id/et_login_password")).send_keys("123456")
wait.until(lambda x: driver.find_element_by_id("com.ttmv.myhome:id/btn_login_commit")).click()
time.sleep(3)
for i in range(1, 8):
    driver.tap([(500, 500)])
    time.sleep(0.5)
time.sleep(10)
wait.until(lambda x: driver.find_element_by_id("com.ttmv.myhome:id/tv2")).click()
wait.until(lambda x: driver.find_element_by_id("com.ttmv.myhome:id/news_contact")).click()
time.sleep(3)
count = 1
while True:
    wait.until(lambda x: driver.find_element_by_id("com.ttmv.myhome:id/nickNameTV")).click()
    wait.until(lambda x: driver.find_element_by_xpath("//*[@text='这个人很懒，没有留下任何东西']"))
    wait.until(lambda x: driver.find_element_by_id("com.ttmv.myhome:id/delete_friend")).click()
    wait.until(lambda x: driver.find_element_by_id("com.ttmv.myhome:id/tv_confirm")).click()
    print(count)
    count += 1
driver.quit()
