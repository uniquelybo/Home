from selenium.webdriver.support.wait import WebDriverWait
import sys


class Mobile_Jurisdiction(object):
    def __init__(self, driver):
        wait = WebDriverWait(driver, 10, 0.5)
        try:
            wait.until(lambda driver: driver.find_element_by_id(
                "com.android.permissioncontroller:id/permission_allow_foreground_only_button")).click()
        except Exception as ex:
            print(ex)
            pass
        while True:
            try:
                driver.find_element_by_id(
                    "com.android.permissioncontroller:id/permission_allow_button").click()
            except Exception as ex:
                print("---------无弹框---------")
                try:
                    wait.until(lambda driver: driver.find_element_by_id("com.ttmv.myhome:id/et_login_phone"))
                    return
                except:
                    print("------手机权限处理错误------")
                    sys.exit()
