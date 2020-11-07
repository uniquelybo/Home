from selenium.webdriver.support.wait import WebDriverWait
import time
import sys


class Households(object):
    def __init__(self, driver):
        self.driver = driver

    def switch_House(self):
        self.driver.find_element_by_id("com.ttmv.myhome:id/item_start").click()
        time.sleep(0.5)
        # 有无第二个住户，有的话选择
        try:
            self.driver.find_element_by_xpath(
                "//android.widget.FrameLayout[1]//android.view.ViewGroup[2]/android.widget.LinearLayout[1]//android.widget.LinearLayout[1]/android.widget.TextView[1]").click()
            time.sleep(0.5)
            self.driver.find_element_by_id("com.ttmv.myhome:id/item_start").click()
            time.sleep(0.5)
            # 当前户标
            try:
                self.driver.find_element_by_xpath(
                    "//android.widget.FrameLayout[1]//android.view.ViewGroup[2]/android.widget.LinearLayout[1]//android.widget.LinearLayout[1]/android.widget.TextView[2]")
                self.driver.find_element_by_xpath(
                    "//android.widget.FrameLayout[@resource-id='com.ttmv.myhome:id/title_bar']/android.widget.LinearLayout[1]/android.widget.TextView[1]").click()
            except:
                print("------------当前户标志没找到-------------")
                sys.exit()
        except:
            # 无其他住户的话，查看有无商户，有的话选择
            try:
                self.driver.find_element_by_xpath(
                    "//android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.view.ViewGroup[1]/android.widget.ExpandableListView[1]/android.view.ViewGroup[3]/android.widget.LinearLayout[1]/android.widget.RelativeLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.TextView[1]").click()
                time.sleep(0.5)
                self.driver.find_element_by_id("com.ttmv.myhome:id/item_start").click()
                time.sleep(0.5)
                # 当前户标
                try:
                    self.driver.find_element_by_xpath(
                        "//android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.view.ViewGroup[1]/android.widget.ExpandableListView[1]/android.view.ViewGroup[3]/android.widget.LinearLayout[1]/android.widget.RelativeLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.TextView[2]").click()
                    self.driver.find_element_by_xpath(
                        "//android.widget.FrameLayout[@resource-id='com.ttmv.myhome:id/title_bar']/android.widget.LinearLayout[1]/android.widget.TextView[1]").click()
                except:
                    print("------------当前户标志没找到-------------")
                    sys.exit()
            except:
                # 无商户的话返回首页
                self.driver.find_element_by_xpath(
                    "//android.widget.FrameLayout[@resource-id='com.ttmv.myhome:id/title_bar']/android.widget.LinearLayout[1]/android.widget.TextView[1]").click()
        time.sleep(0.5)
