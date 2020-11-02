import time
from appium.webdriver.common.touch_action import TouchAction
# from Home.screen.mouse_move_to import get_touchAction


class Query_Collection():
    def __init__(self, driver, num1, screen_names_len):
        self.driver = driver
        self.num1 = num1
        self.screen_names_len = screen_names_len
        self.action = TouchAction(driver)

    # 一种类型
    def one_number(self):
        for screen_num in range(1, self.screen_names_len + 1):
            print("--------------------------")
            # 小区
            try:
                self.driver.find_element_by_id("com.ttmv.myhome:id/name_text").click()
            except:
                pass
            try:
                self.driver.find_element_by_id("com.ttmv.myhome:id/market_text").click()
                list = self.driver.find_elements_by_id("com.ttmv.myhome:id/type_text")
                screen_name = list[screen_num-1].text
                list[screen_num-1].click()
            except:
                screen_name = self.driver.find_element_by_xpath(
                    "//android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.ScrollView[1]/android.widget.LinearLayout[1]/android.support.v7.widget.RecyclerView[2]/android.widget.RelativeLayout[%d]/android.widget.CompoundButton[1]" % screen_num).text
                self.driver.find_element_by_xpath(
                    "//android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.ScrollView[1]/android.widget.LinearLayout[1]/android.support.v7.widget.RecyclerView[2]/android.widget.RelativeLayout[%d]/android.widget.CompoundButton[1]" % screen_num).click()
            print("查询%s" % screen_name)
            self.driver.find_element_by_id("com.ttmv.myhome:id/sure").click()
            try:
                self.driver.find_element_by_id("com.ttmv.myhome:id/emptyImg")
                print("无缴费记录")
                pass
            except:
                item_rela = self.driver.find_elements_by_id("com.ttmv.myhome:id/item_rela")
                item_rela_num = len(item_rela)
                print(item_rela_num)
                names = []
                for item in range(1, item_rela_num + 1):
                    name = self.driver.find_element_by_xpath(
                        "//android.support.v7.widget.RecyclerView[@resource-id='com.ttmv.myhome:id/billRv']/android.widget.RelativeLayout[%d]/android.widget.TextView[1]" % item).text
                    names.append(name)

                while item_rela_num == 7:
                    first_element_time = self.driver.find_element_by_xpath(
                        "//android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.RelativeLayout[2]/android.widget.LinearLayout[1]/android.view.ViewGroup[1]/android.support.v7.widget.RecyclerView[1]/android.widget.RelativeLayout[7]/android.widget.TextView[3]").text
                    self.driver.swipe(231, 1176, 231, 899, 4000)
                    # get_touchAction(self.driver).move(231, 1176, 231, 231)
                    # TouchAction(self.driver).press(x=231, y=1176).wait(200).move_to(x=231, y=914).wait(200).release().perform()

                    print("下滑一行")
                    last_element_time = self.driver.find_element_by_xpath(
                        "//android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.RelativeLayout[2]/android.widget.LinearLayout[1]/android.view.ViewGroup[1]/android.support.v7.widget.RecyclerView[1]/android.widget.RelativeLayout[7]/android.widget.TextView[3]").text
                    last_name = self.driver.find_element_by_xpath(
                        "//android.support.v7.widget.RecyclerView[@resource-id='com.ttmv.myhome:id/billRv']/android.widget.RelativeLayout[7]/android.widget.TextView[1]").text
                    if first_element_time == last_element_time:
                        break
                    names.append(last_name)
                for name in names:
                    print(name)
                    if name == screen_name:
                        continue
                    print("数据对比错误---")
                    break
            if screen_num == self.screen_names_len:
                break
            self.driver.find_element_by_id("com.ttmv.myhome:id/back_img").click()
            self.driver.find_element_by_id("com.ttmv.myhome:id/record_tv").click()
            time.sleep(2)
            self.driver.find_element_by_id("com.ttmv.myhome:id/tv_filter").click()
            time.sleep(1)

    # 两种类型
    def double_number(self):
        self.one_number()
        while True:
            for i in range(self.num1, self.screen_names_len):
                self.driver.find_element_by_id("com.ttmv.myhome:id/back_img").click()
                self.driver.find_element_by_id("com.ttmv.myhome:id/record_tv").click()
                time.sleep(2)
                self.driver.find_element_by_id("com.ttmv.myhome:id/tv_filter").click()
                time.sleep(1)
                print(self.num1, i + 1)
                print("--------------------------")
                # 小区
                self.driver.find_element_by_id("com.ttmv.myhome:id/name_text").click()
                try:
                    self.driver.find_element_by_id("com.ttmv.myhome:id/market_text").click()
                    list = self.driver.find_elements_by_id("com.ttmv.myhome:id/type_text")
                    screen_name1 = list[self.num1 - 1].text
                    screen_name2 = list[i].text
                    list[self.num1 - 1].click()
                    list[i].click()
                except:
                    # 类型
                    list = self.driver.find_elements_by_id("com.ttmv.myhome:id/type_text")
                    screen_name1 = list[self.num1 - 1].text
                    screen_name2 = list[i].text
                    list[self.num1 - 1].click()
                    list[i].click()
                print("查询" + screen_name1, screen_name2)
                self.driver.find_element_by_id("com.ttmv.myhome:id/sure").click()
                try:
                    self.driver.find_element_by_id("com.ttmv.myhome:id/emptyImg")
                    print("无缴费记录")
                    pass
                except:
                    time.sleep(3)
                    item_rela = self.driver.find_elements_by_id("com.ttmv.myhome:id/item_rela")
                    names = []
                    item_relas = len(item_rela)
                    for item in range(1, item_relas + 1):
                        name = self.driver.find_element_by_xpath(
                            "//android.support.v7.widget.RecyclerView[@resource-id='com.ttmv.myhome:id/billRv']/android.widget.RelativeLayout[%d]/android.widget.TextView[1]" % item).text
                        names.append(name)

                    while item_relas == 7:
                        first_element_time = self.driver.find_element_by_xpath(
                            "//android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.RelativeLayout[2]/android.widget.LinearLayout[1]/android.view.ViewGroup[1]/android.support.v7.widget.RecyclerView[1]/android.widget.RelativeLayout[7]/android.widget.TextView[3]").text
                        self.driver.swipe(231, 1176, 231, 899, 4000)
                        # TouchAction(self.driver).long_press(x=231, y=914).move_to(x=231, y=652).wait(
                        #     300).release().perform()
                        last_element_time = self.driver.find_element_by_xpath(
                            "//android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.RelativeLayout[2]/android.widget.LinearLayout[1]/android.view.ViewGroup[1]/android.support.v7.widget.RecyclerView[1]/android.widget.RelativeLayout[7]/android.widget.TextView[3]").text
                        last_name = self.driver.find_element_by_xpath(
                            "//android.support.v7.widget.RecyclerView[@resource-id='com.ttmv.myhome:id/billRv']/android.widget.RelativeLayout[7]/android.widget.TextView[1]").text
                        if first_element_time == last_element_time:
                            break
                        names.append(last_name)

                    for name in names:
                        print(name)
                        if (name == screen_name1) or (name == screen_name2):
                            continue
                        print("数据对比错误---")
                        break

            self.num1 += 1
            if self.num1 == self.screen_names_len:
                break

    # 三种类型
    def triple_number(self):
        print(self.screen_names_len)
        self.double_number()
        while True:
            for i in range(self.num1, self.screen_names_len - 1):
                time.sleep(0.5)
                self.driver.find_element_by_id("com.ttmv.myhome:id/back_img").click()
                self.driver.find_element_by_id("com.ttmv.myhome:id/record_tv").click()
                time.sleep(3)
                self.driver.find_element_by_id("com.ttmv.myhome:id/tv_filter").click()
                time.sleep(2)
                print(self.num1, self.num1 + 1, i + 2)
                print("--------------------------")
                # 小区
                self.driver.find_element_by_id("com.ttmv.myhome:id/name_text").click()
                try:
                    self.driver.find_element_by_id("com.ttmv.myhome:id/market_text").click()
                    list = self.driver.find_elements_by_id("com.ttmv.myhome:id/type_text")
                    screen_name1 = list[self.num1 - 1].text
                    screen_name2 = list[self.num1].text
                    screen_name3 = list[(i + 1)].text
                    list[self.num1 - 1].click()
                    list[self.num1].click()
                    list[(i + 1)].click()
                except:
                    # 类型
                    list = self.driver.find_elements_by_id("com.ttmv.myhome:id/type_text")
                    screen_name1 = list[self.num1 - 1].text
                    screen_name2 = list[self.num1].text
                    screen_name3 = list[(i + 1)].text
                    list[self.num1 - 1].click()
                    list[self.num1].click()
                    list[(i + 1)].click()

                print("查询" + screen_name1, screen_name2, screen_name3)
                self.driver.find_element_by_id("com.ttmv.myhome:id/sure").click()
                try:
                    self.driver.find_element_by_id("com.ttmv.myhome:id/emptyImg")
                    print("无缴费记录")
                    pass
                except:
                    time.sleep(3)
                    item_rela = self.driver.find_elements_by_id("com.ttmv.myhome:id/item_rela")

                    names = []
                    item_relas = len(item_rela)

                    for item in range(1, item_relas + 1):
                        name = self.driver.find_element_by_xpath(
                            "//android.support.v7.widget.RecyclerView[@resource-id='com.ttmv.myhome:id/billRv']/android.widget.RelativeLayout[%d]/android.widget.TextView[1]" % item).text
                        names.append(name)

                    while item_relas == 7:
                        first_element_time = self.driver.find_element_by_xpath(
                            "//android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.RelativeLayout[2]/android.widget.LinearLayout[1]/android.view.ViewGroup[1]/android.support.v7.widget.RecyclerView[1]/android.widget.RelativeLayout[7]/android.widget.TextView[3]").text
                        self.driver.swipe(231, 1176, 231, 899, 4000)
                        # TouchAction(self.driver).long_press(x=231, y=914).move_to(x=231, y=652).wait(
                        #     300).release().perform()
                        last_element_time = self.driver.find_element_by_xpath(
                            "//android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.RelativeLayout[2]/android.widget.LinearLayout[1]/android.view.ViewGroup[1]/android.support.v7.widget.RecyclerView[1]/android.widget.RelativeLayout[7]/android.widget.TextView[3]").text
                        last_name = self.driver.find_element_by_xpath(
                            "//android.support.v7.widget.RecyclerView[@resource-id='com.ttmv.myhome:id/billRv']/android.widget.RelativeLayout[7]/android.widget.TextView[1]").text
                        if first_element_time == last_element_time:
                            break
                        names.append(last_name)

                    for name in names:
                        print(name)
                        if (name == screen_name1) or (name == screen_name2) or (name == screen_name3):
                            continue
                        print("数据对比错误---")
                        break
            self.num1 += 1
            if self.num1 == self.screen_names_len - 1:
                break

    # 四种类型
    def quadruple_number(self):
        self.triple_number()
        while True:
            for i in range(self.num1, self.screen_names_len - 2):
                time.sleep(0.5)
                self.driver.find_element_by_id("com.ttmv.myhome:id/back_img").click()
                self.driver.find_element_by_id("com.ttmv.myhome:id/record_tv").click()
                time.sleep(3)
                self.driver.find_element_by_id("com.ttmv.myhome:id/tv_filter").click()
                time.sleep(2)
                print(self.num1, self.num1 + 1, self.num1 + 2, i + 3)
                print("--------------------------")
                # 小区
                self.driver.find_element_by_id("com.ttmv.myhome:id/name_text").click()
                # 商场
                try:
                    self.driver.find_element_by_id("com.ttmv.myhome:id/market_text").click()
                    list = self.driver.find_elements_by_id("com.ttmv.myhome:id/type_text")
                    screen_name1 = list[self.num1 - 1].text
                    screen_name2 = list[self.num1].text
                    screen_name3 = list[self.num1 + 1].text
                    screen_name4 = list[(i + 2)].text
                    list[self.num1 - 1].click()
                    list[self.num1].click()
                    list[self.num1 + 1].click()
                    list[(i + 2)].click()
                except:
                    # 类型
                    list = self.driver.find_elements_by_id("com.ttmv.myhome:id/type_text")
                    screen_name1 = list[self.num1 - 1].text
                    screen_name2 = list[self.num1].text
                    screen_name3 = list[self.num1 + 1].text
                    screen_name4 = list[(i + 2)].text
                    list[self.num1 - 1].click()
                    list[self.num1].click()
                    list[self.num1 + 1].click()
                    list[(i + 2)].click()

                print("查询" + screen_name1, screen_name2, screen_name3, screen_name4)
                self.driver.find_element_by_id("com.ttmv.myhome:id/sure").click()
                try:
                    self.driver.find_element_by_id("com.ttmv.myhome:id/emptyImg")
                    print("无缴费记录")
                    pass
                except:
                    time.sleep(3)
                    item_rela = self.driver.find_elements_by_id("com.ttmv.myhome:id/item_rela")

                    names = []
                    item_relas = len(item_rela)

                    for item in range(1, item_relas + 1):
                        name = self.driver.find_element_by_xpath(
                            "//android.support.v7.widget.RecyclerView[@resource-id='com.ttmv.myhome:id/billRv']/android.widget.RelativeLayout[%d]/android.widget.TextView[1]" % item).text
                        names.append(name)

                    while item_relas == 7:
                        first_element_time = self.driver.find_element_by_xpath(
                            "//android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.RelativeLayout[2]/android.widget.LinearLayout[1]/android.view.ViewGroup[1]/android.support.v7.widget.RecyclerView[1]/android.widget.RelativeLayout[7]/android.widget.TextView[3]").text
                        self.driver.swipe(231, 1176, 231, 899, 4000)
                        # TouchAction(self.driver).long_press(x=1032, y=917).move_to(x=1032, y=655).wait(2000).release().perform()
                        last_element_time = self.driver.find_element_by_xpath(
                            "//android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.RelativeLayout[2]/android.widget.LinearLayout[1]/android.view.ViewGroup[1]/android.support.v7.widget.RecyclerView[1]/android.widget.RelativeLayout[7]/android.widget.TextView[3]").text
                        last_name = self.driver.find_element_by_xpath(
                            "//android.support.v7.widget.RecyclerView[@resource-id='com.ttmv.myhome:id/billRv']/android.widget.RelativeLayout[7]/android.widget.TextView[1]").text
                        if first_element_time == last_element_time:
                            break
                        names.append(last_name)

                    for name in names:
                        print(name)
                        if (name == screen_name1) or (name == screen_name2) or (name == screen_name3) or (
                                name == screen_name4):
                            continue
                        print("数据对比错误---")
                        break
            self.num1 += 1
            if self.num1 == self.screen_names_len - 2:
                return
