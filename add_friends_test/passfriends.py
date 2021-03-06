from appium import webdriver
import time
import random
from selenium.webdriver.support.wait import WebDriverWait
from addfriends import Addfriend
from read_tt import Readfile


class PassFriends:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 5)

    def bb_login(self, tt):
        try:
            self.wait.until(lambda x: self.driver.find_element_by_xpath("//*[@text='我的']")).click()
        except Exception as e:
            print("-----我的----", e)
        self.wait.until(lambda driver: self.driver.find_element_by_id("com.ttmv.bobo_client:id/switchLoginSelectTV")).click()
        self.wait.until(lambda driver: driver.find_element_by_id("com.ttmv.bobo_client:id/login_userName_text")).send_keys(tt)
        self.driver.find_element_by_id("com.ttmv.bobo_client:id/login_pwd_text").send_keys("123456")
        self.driver.find_element_by_id("com.ttmv.bobo_client:id/lgoin_btn_login").click()

    def logout(self):
        self.wait.until(lambda x: self.driver.find_element_by_xpath("//*[@text='我的']")).click()
        self.wait.until(lambda x: self.driver.find_element_by_id("com.ttmv.bobo_client:id/settingImage")).click()
        self.wait.until(lambda x: self.driver.find_element_by_id("com.ttmv.bobo_client:id/setting_set_loginout")).click()

    def newfriend(self):
        self.wait.until(lambda driver: driver.find_element_by_id("com.ttmv.bobo_client:id/btn_filmTVLayout")).click()
        self.wait.until(lambda driver: driver.find_element_by_xpath("//*[@text='新的朋友']")).click()

    def pass_request(self, tt):
        # friends = self.driver.find_elements_by_id("com.ttmv.bobo_client:id/name")
        # f = 1
        # for friend in friends:
        #     if friend.text == "Aaaaaa":
        #         ele = self.driver.find_element_by_xpath("//android.support.v7.widget.RecyclerView[1]/android.widget.LinearLayout[%d]/android.widget.LinearLayout[1]/android.widget.TextView[1]" % f)
        #         if ele.text == "已添加":
        #             break
        #         else:
                    # self.driver.find_element_by_xpath("//android.support.v7.widget.RecyclerView[1]/android.widget.LinearLayout[%d]/android.widget.LinearLayout[1]/android.widget.TextView[2]" % f).click()
                    # self.driver.find_element_by_id("com.ttmv.bobo_client:id/agree_add_tv").click()
            #         break
            # else:
            #     f += 1
        # self.wait.until(lambda driver: self.driver.find_element_by_id("com.ttmv.bobo_client:id/agree_add_tv")).click()
        # self.wait.until(lambda driver: self.driver.find_element_by_id("com.ttmv.bobo_client:id/btnLeft")).click()
        self.wait.until(lambda driver: self.driver.find_element_by_id("com.ttmv.bobo_client:id/edit_search")).send_keys(
            tt)
        self.wait.until(lambda driver: self.driver.find_element_by_id("com.ttmv.bobo_client:id/btn_search")).click()
        text = self.wait.until(lambda driver: self.driver.find_element_by_id("com.ttmv.bobo_client:id/addBtn")).text
        if text == "已添加":
            self.driver.find_element_by_id("com.ttmv.bobo_client:id/edit_search").clear()
        else:
            self.wait.until(lambda driver: self.driver.find_element_by_id("com.ttmv.bobo_client:id/addBtn")).click()
            # try:
            #     self.wait.until(
            #         lambda driver: self.driver.find_element_by_id("com.ttmv.bobo_client:id/btnRight")).click()
            # except:
            #     print("-----添加失败------", line)
