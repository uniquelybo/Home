from appium import webdriver
import time, sys
import device_init
import User_Login
from Home.screen.query_collection import Query_Collection
# from appium.webdriver.common.touch_action import TouchAction


def home_page():
    # 加入注册信息启动app
    desired_caps = device_init.appInit()
    driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)
    # APP初始化权限
    device_init.jurisdiction_init(driver, time)
    # 登录
    User_Login.user_login(driver, time)
    return driver


# 判断类型个数选取执行方法
def bool_screen_names_len(screen_names_len):
    qc = Query_Collection(driver, 1, screen_names_len)
    if screen_names_len == 1:
        qc.one_number()
    elif screen_names_len == 2:
        qc.double_number()
    elif screen_names_len == 3:
        qc.triple_number()
    elif screen_names_len == 4:
        qc.quadruple_number()


def screen_():
    # 首页进入“我”
    driver.find_element_by_id("com.ttmv.myhome:id/tv3").click()
    # 缴费记录
    driver.find_element_by_id("com.ttmv.myhome:id/record_tv").click()
    time.sleep(0.5)
    try:
        driver.find_element_by_id("com.ttmv.myhome:id/emptyImg")
        print("无缴费记录")
        driver.quit()
    except Exception as ex:
        # 筛选
        time.sleep(2)
        driver.find_element_by_id("com.ttmv.myhome:id/tv_filter").click()
        time.sleep(1)
        # screen
        # 获取可筛选类型
        screen_names = driver.find_elements_by_id("com.ttmv.myhome:id/type_text")
        screen_names_len = len(screen_names)
        print(screen_names_len)
        bool_screen_names_len(screen_names_len)
        driver.quit()


if __name__ == "__main__":
    driver = home_page()
    screen_()
