from appium.webdriver.common.touch_action import TouchAction
import sys
import time


class Pay(object):
    def __init__(self, driver):
        self.driver = driver

    def wx_or_ali(self):
        pay_bool = True
        while pay_bool:
            pay_type = input("Enter your input: \n 1微信；2支付宝 \n")
            if pay_type == "1":
                # 微信支付
                self.driver.find_element_by_id("com.ttmv.myhome:id/wx_rb").click()
                pay_bool = False
            elif pay_type == "2":
                # 支付宝支付
                self.driver.find_element_by_id("com.ttmv.myhome:id/ali_rb").click()
                pay_bool = False
            else:
                pass
        # 支付
        self.driver.find_element_by_id("com.ttmv.myhome:id/pay_btn").click()
        time.sleep(5)
        # 立即支付
        self.driver.find_element_by_xpath(
            "//android.widget.FrameLayout[@resource-id='com.tencent.mm:id/i7p']/android.widget.ImageView[1]").click()
        time.sleep(2)
        TouchAction(self.driver).tap(x=180, y=1800).wait(200).tap(x=190, y=2110).wait(200).tap(x=180, y=1800).wait(
            200).tap(x=190, y=2110).wait(200).tap(x=540, y=1800).wait(200).tap(x=900, y=2100).wait(
            200).perform().release()
        time.sleep(5)
        # [150, 1080, 190, 2110, 150, 1080, 190, 2110, 540, 1800, 900, 2100]
        # 支付成功

    def pay_sure(self):
        try:
            self.driver.find_element_by_xpath("//android.widget.TextView[@text='支付成功']")
        except:
            print("-------没捕捉到支付成功页面1------")
            sys.exit()
        # 返回商家
        self.driver.find_element_by_xpath(
            "//android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout[1]/android.widget.ImageView[1]").click()
        time.sleep(1)
        try:
            self.driver.find_element_by_xpath("//android.widget.TextView[@text='支付成功']")
        except:
            print("-------没捕捉到支付成功页面2------")
            sys.exit()
        # 支付成功确定
        self.driver.find_element_by_id("com.ttmv.myhome:id/ok_btn").click()

    def pay(self):
        try:
            self.driver.find_element_by_xpath(
                "//android.support.v7.widget.RecyclerView[@resource-id='com.ttmv.myhome:id/manyRv']/android.widget.RelativeLayout[1]").click()
            try:
                time.sleep(1)
                self.driver.find_element_by_id("com.ttmv.myhome:id/tv_confirm").click()
                # 支付金额
                time.sleep(1)
                send_price = "0.01"
                # 输入金额
                self.driver.find_element_by_id("com.ttmv.myhome:id/getMoneyEdit").send_keys(send_price)
                # 显示金额
                price = self.driver.find_element_by_id("com.ttmv.myhome:id/price_tv").text
                # 对比金额
                if price == send_price:
                    print("金额一致")
                else:
                    print("金额不一致")
                    sys.exit()
            except:
                print("-----------没捕捉到预交费弹框-----------")
                print("----------------无缴费项--------------")
                sys.exit()
        except:
            print("--------无多表---------")
            try:
                # 缴费账单
                self.driver.find_element_by_id("com.ttmv.myhome:id/status_iv")
                self.driver.swipe(510, 1700, 510, 900, 500)
                self.driver.find_element_by_id("com.ttmv.myhome:id/pay_btn").click()
                self.pay_sure()
            except:
                print("--------无缴费账单，进入预付费---------")
                # 预付费
                time.sleep(1)
                send_price = "0.01"
                try:
                    self.driver.find_element_by_id("com.ttmv.myhome:id/tv_confirm").click()
                    # 支付金额
                    time.sleep(1)
                    # 输入金额
                    self.driver.find_element_by_id("com.ttmv.myhome:id/getMoneyEdit").send_keys(send_price)
                    # 显示金额
                    price = self.driver.find_element_by_id("com.ttmv.myhome:id/price_tv").text
                    # 对比金额
                    if price == send_price:
                        print("金额一致")
                    else:
                        print("金额不一致")
                        sys.exit()
                except:
                    print("-----------没捕捉到预交费弹框-----------")
                    print("----------------无缴费项--------------")
                    sys.exit()
        self.wx_or_ali()
        self.pay_sure()

    def switch_pay(self):
        try:
            # 电
            electric = self.driver.find_element_by_id("com.ttmv.myhome:id/home_ele_lay")
            self.driver.find_element_by_id("com.ttmv.myhome:id/home_eletric").click()
            self.pay()
        except:
            print("---------没有捕捉到电费--------")

        try:
            # 水
            water = self.driver.find_element_by_id("com.ttmv.myhome:id/home_water_lay")
            self.driver.find_element_by_id("com.ttmv.myhome:id/home_water").click()
            self.pay()
        except:
            print("---------没有捕捉到水费--------")

        try:
            # 物业
            self.driver.find_element_by_id("com.ttmv.myhome:id/home_pro_lay")
            self.driver.find_element_by_id("com.ttmv.myhome:id/home_wy").click()
            self.pay()
        except:
            print("---------没有捕捉到物业费--------")
