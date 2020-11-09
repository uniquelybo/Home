from appium import webdriver


class Device_Init(object):
    def __init__(self):
        # 注册信息
        self.desired_caps = {}
        self.desired_caps['platformName'] = 'Android'
        self.desired_caps['platformVersion'] = '10'
        self.desired_caps['deviceName'] = '荣耀'
        self.desired_caps['appPackage'] = 'com.ttmv.myhome'
        self.desired_caps['appActivity'] = '.ui.activity.SplashActivity'
        print(self.desired_caps)
        print("-----------设备信息注册完成------------")

    def get_driver(self):
        driver = webdriver.Remote("http://localhost:4723/wd/hub", self.desired_caps)
        return driver
