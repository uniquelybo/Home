import time


class Query_Collection():
    def __init__(self, driver, num1, screen_names_len):
        self.driver = driver
        self.num1 = num1
        self.screen_names_len = screen_names_len

    # 一种类型
    def one_number(self):
        for screen_num in range(1, self.screen_names_len + 1):
            print("--------------------------")
            # 小区
            self.driver.find_element_by_id("com.ttmv.myhome:id/name_text").click()
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
                names = []
                for item in range(1, len(item_rela) + 1):
                    name = self.driver.find_element_by_xpath(
                        "//android.support.v7.widget.RecyclerView[@resource-id='com.ttmv.myhome:id/billRv']/android.widget.RelativeLayout[%d]/android.widget.TextView[1]" % item).text
                    names.append(name)

                while len(item_rela) == 7:
                    first_element_time = self.driver.find_element_by_xpath(
                        "//android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.RelativeLayout[2]/android.widget.LinearLayout[1]/android.view.ViewGroup[1]/android.support.v7.widget.RecyclerView[1]/android.widget.RelativeLayout[7]/android.widget.TextView[3]").text
                    self.driver.swipe(1032, 917, 1032, 655, 500)
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
            time.sleep(0.5)
            self.driver.find_element_by_id("com.ttmv.myhome:id/tv_filter").click()
            time.sleep(0.5)

    # 两种类型
    def double_number(self):
        self.one_number()
        while True:
            for i in range(self.num1, self.screen_names_len):
                self.driver.find_element_by_id("com.ttmv.myhome:id/back_img").click()
                self.driver.find_element_by_id("com.ttmv.myhome:id/record_tv").click()
                time.sleep(0.5)
                self.driver.find_element_by_id("com.ttmv.myhome:id/tv_filter").click()
                time.sleep(0.5)
                print(self.num1, i + 1)
                print("--------------------------")
                # 小区
                self.driver.find_element_by_id("com.ttmv.myhome:id/name_text").click()
                # 类型
                screen_name1 = self.driver.find_element_by_xpath(
                    "//android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.ScrollView[1]/android.widget.LinearLayout[1]/android.support.v7.widget.RecyclerView[2]/android.widget.RelativeLayout[%d]/android.widget.CompoundButton[1]" % self.num1).text
                screen_name2 = self.driver.find_element_by_xpath(
                    "//android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.ScrollView[1]/android.widget.LinearLayout[1]/android.support.v7.widget.RecyclerView[2]/android.widget.RelativeLayout[%d]/android.widget.CompoundButton[1]" % (
                            i + 1)).text
                self.driver.find_element_by_xpath(
                    "//android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.ScrollView[1]/android.widget.LinearLayout[1]/android.support.v7.widget.RecyclerView[2]/android.widget.RelativeLayout[%d]/android.widget.CompoundButton[1]" % self.num1).click()
                self.driver.find_element_by_xpath(
                    "//android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.ScrollView[1]/android.widget.LinearLayout[1]/android.support.v7.widget.RecyclerView[2]/android.widget.RelativeLayout[%d]/android.widget.CompoundButton[1]" % (
                            i + 1)).click()
                print("查询" + screen_name1, screen_name2)
                self.driver.find_element_by_id("com.ttmv.myhome:id/sure").click()
                try:
                    self.driver.find_element_by_id("com.ttmv.myhome:id/emptyImg")
                    print("无缴费记录")
                    pass
                except:
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
                        self.driver.swipe(1032, 917, 1032, 655, 500)
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
                    return

    # 三种类型
    def triple_number(self):
        self.double_number()
        while True:
            for i in range(self.num1, self.screen_names_len - 1):
                self.driver.find_element_by_id("com.ttmv.myhome:id/back_img").click()
                self.driver.find_element_by_id("com.ttmv.myhome:id/record_tv").click()
                time.sleep(0.5)
                self.driver.find_element_by_id("com.ttmv.myhome:id/tv_filter").click()
                time.sleep(0.5)
                print(self.num1, self.num1 + 1, i + 2)
                print("--------------------------")
                # 小区
                self.driver.find_element_by_id("com.ttmv.myhome:id/name_text").click()
                # 类型
                screen_name1 = self.driver.find_element_by_xpath(
                    "//android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.ScrollView[1]/android.widget.LinearLayout[1]/android.support.v7.widget.RecyclerView[2]/android.widget.RelativeLayout[%d]/android.widget.CompoundButton[1]" % self.num1).text
                screen_name2 = self.driver.find_element_by_xpath(
                    "//android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.ScrollView[1]/android.widget.LinearLayout[1]/android.support.v7.widget.RecyclerView[2]/android.widget.RelativeLayout[%d]/android.widget.CompoundButton[1]" % (
                            self.num1 + 1)).text
                screen_name3 = self.driver.find_element_by_xpath(
                    "//android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.ScrollView[1]/android.widget.LinearLayout[1]/android.support.v7.widget.RecyclerView[2]/android.widget.RelativeLayout[%d]/android.widget.CompoundButton[1]" % (
                            i + 2)).text
                self.driver.find_element_by_xpath(
                    "//android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.ScrollView[1]/android.widget.LinearLayout[1]/android.support.v7.widget.RecyclerView[2]/android.widget.RelativeLayout[%d]/android.widget.CompoundButton[1]" % self.num1).click()
                self.driver.find_element_by_xpath(
                    "//android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.ScrollView[1]/android.widget.LinearLayout[1]/android.support.v7.widget.RecyclerView[2]/android.widget.RelativeLayout[%d]/android.widget.CompoundButton[1]" % (
                            self.num1 + 1)).click()
                self.driver.find_element_by_xpath(
                    "//android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.ScrollView[1]/android.widget.LinearLayout[1]/android.support.v7.widget.RecyclerView[2]/android.widget.RelativeLayout[%d]/android.widget.CompoundButton[1]" % (
                            i + 2)).click()

                print("查询" + screen_name1, screen_name2, screen_name3)
                self.driver.find_element_by_id("com.ttmv.myhome:id/sure").click()
                try:
                    self.driver.find_element_by_id("com.ttmv.myhome:id/emptyImg")
                    print("无缴费记录")
                    pass
                except:
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
                        self.driver.swipe(1032, 917, 1032, 655, 500)
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
                if self.num1 == len(self.screen_names_len) - 1:
                    break

    # 四种类型
    def quadruple_number(self):
        self.triple_number()
        while True:
            for i in range(self.num1, self.screen_names_len - 2):
                self.driver.find_element_by_id("com.ttmv.myhome:id/back_img").click()
                self.driver.find_element_by_id("com.ttmv.myhome:id/record_tv").click()
                time.sleep(0.5)
                self.driver.find_element_by_id("com.ttmv.myhome:id/tv_filter").click()
                time.sleep(0.5)
                print(self.num1, self.num1 + 1, self.num1 + 2, i + 3)
                print("--------------------------")
                # 小区
                self.driver.find_element_by_id("com.ttmv.myhome:id/name_text").click()
                # 类型
                screen_name1 = self.driver.find_element_by_xpath(
                    "//android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.ScrollView[1]/android.widget.LinearLayout[1]/android.support.v7.widget.RecyclerView[2]/android.widget.RelativeLayout[%d]/android.widget.CompoundButton[1]" % self.num1).text
                screen_name2 = self.driver.find_element_by_xpath(
                    "//android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.ScrollView[1]/android.widget.LinearLayout[1]/android.support.v7.widget.RecyclerView[2]/android.widget.RelativeLayout[%d]/android.widget.CompoundButton[1]" % (
                                self.num1 + 1)).text
                screen_name3 = self.driver.find_element_by_xpath(
                    "//android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.ScrollView[1]/android.widget.LinearLayout[1]/android.support.v7.widget.RecyclerView[2]/android.widget.RelativeLayout[%d]/android.widget.CompoundButton[1]" % (
                                self.num1 + 2)).text
                screen_name4 = self.driver.find_element_by_xpath(
                    "//android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.ScrollView[1]/android.widget.LinearLayout[1]/android.support.v7.widget.RecyclerView[2]/android.widget.RelativeLayout[%d]/android.widget.CompoundButton[1]" % (
                                i + 3)).text

                self.driver.find_element_by_xpath(
                    "//android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.ScrollView[1]/android.widget.LinearLayout[1]/android.support.v7.widget.RecyclerView[2]/android.widget.RelativeLayout[%d]/android.widget.CompoundButton[1]" % self.num1).click()
                self.driver.find_element_by_xpath(
                    "//android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.ScrollView[1]/android.widget.LinearLayout[1]/android.support.v7.widget.RecyclerView[2]/android.widget.RelativeLayout[%d]/android.widget.CompoundButton[1]" % (
                                self.num1 + 1)).click()
                self.driver.find_element_by_xpath(
                    "//android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.ScrollView[1]/android.widget.LinearLayout[1]/android.support.v7.widget.RecyclerView[2]/android.widget.RelativeLayout[%d]/android.widget.CompoundButton[1]" % (
                                self.num1 + 2)).click()
                self.driver.find_element_by_xpath(
                    "//android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.ScrollView[1]/android.widget.LinearLayout[1]/android.support.v7.widget.RecyclerView[2]/android.widget.RelativeLayout[%d]/android.widget.CompoundButton[1]" % (
                                i + 3)).click()

                print("查询" + screen_name1, screen_name2, screen_name3, screen_name4)
                self.driver.find_element_by_id("com.ttmv.myhome:id/sure").click()
                try:
                    self.driver.find_element_by_id("com.ttmv.myhome:id/emptyImg")
                    print("无缴费记录")
                    pass
                except:
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
                        self.driver.swipe(1032, 917, 1032, 655, 500)
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
                if self.num1 == len(self.screen_names_len) - 2:
                    break
