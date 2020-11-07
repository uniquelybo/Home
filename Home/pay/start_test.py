from selenium.webdriver.support.wait import WebDriverWait
from appium import webdriver
import time
from public_config.device_init import Device_Init
from public_config.Mobile_Jurisdiction import Mobile_Jurisdiction
from public_config.User_Login import User_Login
from pay.Pay import Pay
from pay.Households import Households


if __name__ == "__main__":
    # 加入注册信息启动app
    driver = Device_Init().get_driver()
    # APP初始化权限
    Mobile_Jurisdiction(driver)
    # 登录
    User_Login(driver).user_login("18334783765", "123456")
    pay = Pay(driver)
    households = Households(driver)
    #
    households.switch_House()
    pay.switch_pay()

    driver.quit()
    #



