

# 注册信息
def appInit():
    desired_caps = {}
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '10'
    desired_caps['deviceName'] = '华为P40'
    desired_caps['appPackage'] = 'com.ttmv.myhome'
    desired_caps['appActivity'] = '.ui.activity.SplashActivity'

    print(desired_caps)
    print("-----------设备信息注册完成------------")
    return desired_caps
    # print(desired_caps)
    # desired_caps['unicodeKeyboard']='True'
    # desired_caps['resetKeyboard']='False'


# app初次启动权限设置
def jurisdiction_init(driver, time):
    driver.tap([(120, 1871), (960, 1912)])
    # driver.find_element_by_xpath("//android.widget.TextView[@resource-id='com.android.permissioncontroller:id/current_page_message']").click()
    time.sleep(0.5)
    driver.tap([(553, 2136), (984, 2214)])
    # driver.find_element_by_xpath("//android.widget.Button[@resource-id='com.android.permissioncontroller:id/permission_allow_button']").click()
    time.sleep(0.5)
    driver.tap([(553, 2136), (984, 2214)])
    # driver.find_element_by_xpath("//android.widget.Button[@resource-id='com.android.permissioncontroller:id/permission_allow_button']").click()
    time.sleep(0.5)
    driver.tap([(553, 2136), (984, 2214)])
    time.sleep(0.5)
    print("------------app初次启动操作完成----------")
