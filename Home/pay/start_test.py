from appium import webdriver
import time
import device_init
import User_Login
from Home.pay.Pay import Pay
from Home.pay.Households import Households


def home_page():
    # 加入注册信息启动app
    desired_caps = device_init.appInit()
    driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)
    time.sleep(2)
    # APP初始化权限
    device_init.jurisdiction_init(driver, time)
    # 登录
    User_Login.user_login(driver, time)
    return driver


if __name__ == "__main__":
    driver = home_page()

    pay = Pay(driver)
    households = Households(driver)

    households.switch_House()
    pay.switch_pay()


