# 登录
# from appium.webdriver.common.touch_action import TouchAction


def user_login(driver, time):
    # driver.find_element_by_id("com.ttmv.myhome:id/et_login_phone").send_keys("18334783765")
    driver.find_element_by_id("com.ttmv.myhome:id/et_login_phone").send_keys("17363905237")
    driver.find_element_by_id("com.ttmv.myhome:id/et_login_password").send_keys("qqqqqq")
    # driver.find_element_by_id("com.ttmv.myhome:id/et_login_password").send_keys("123456")
    driver.find_element_by_id("com.ttmv.myhome:id/btn_login_commit").click()
    time.sleep(5)
