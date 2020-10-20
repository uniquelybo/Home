import time


# 前一年
def last_year(driver):
    driver.swipe(277, 1215, 277, 1370, 600)


# 下一年
def next_year(driver):
    driver.swipe(277, 1370, 277, 1215, 600)


# 前一月
def last_month(driver):
    driver.swipe(570, 1215, 570, 1370, 600)


# 下一月
def next_month(driver):
    driver.swipe(570, 1370, 570, 1215, 600)


# 前一天
def last_day(driver):
    driver.swipe(850, 1215, 850, 1370, 600)


# 下一天
def next_day(driver):
    driver.swipe(850, 1370, 570, 1215, 600)


def start_(driver):

    driver.find_element_by_id("com.ttmv.myhome:id/tv_time").click()
    time.sleep(0.5)
    last_month(driver)
    driver.find_element_by_id("com.ttmv.myhome:id/end").click()
    next_month(driver)
    time.sleep(0.5)
    driver.find_element_by_id("com.ttmv.myhome:id/ok_btn").click()
