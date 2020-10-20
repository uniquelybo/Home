from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import random
import time

chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
chrome_driver = "C:\Program Files\Google\Chrome\Application\chromedriver.exe"
driver = webdriver.Chrome(chrome_driver, chrome_options=chrome_options)
print(driver.title)


driver.find_element_by_xpath("//div/section/section/main/div/div[7]/div/div[2]/form/div[2]/div/div/div[1]/input").click()
time.sleep(2)
lis = driver.find_elements_by_xpath("/html/body/div[4]/div[1]/div[1]/ul/li")
ran = random.randint(1, len(lis))
print(ran)
driver.find_element_by_xpath("/html/body/div[4]/div[1]/div[1]/ul/li[%d]" % ran).click()


# labels = driver.find_elements_by_class_name("label")
# labels_num = len(labels)
#
# num1 = 0
# num2 = 1
# while True:
#     ran = random.randint(1, labels_num)
#     if num1 == ran:
#         continue
#     driver.find_elements_by_class_name("label")[ran].click()
#     num1 = ran
#     num2 = num2 + 1
#     if num2 == 4:
#         break


# driver.find_element_by_xpath("//div/section/section/main/div/div[4]/div/div[2]/form/div[1]/div/div[1]/input").send_keys("101")
# driver.find_element_by_xpath("//div/section/section/main/div/div[4]/div/div[2]/form/div[2]/div/div/input").send_keys("101业主")
# driver.find_element_by_xpath("//div/section/section/main/div/div[4]/div/div[2]/form/div[3]/div/div/input").send_keys("18302102102")
# driver.find_element_by_xpath("//div/section/section/main/div/div[4]/div/div[2]/form/div[4]/div/div/input").send_keys("已")
# driver.find_element_by_xpath("//div/section/section/main/div/div[4]/div/div[2]/form/div[5]/div/div/input").send_keys("111")
# driver.find_element_by_xpath("//div/section/section/main/div/div[4]/div/div[2]/form/div[6]/div/div/input").send_keys("ceshi")
# driver.find_element_by_xpath("//div/section/section/main/div/div[4]/div/div[2]/form/div[7]/div/div/input").send_keys("南")
# driver.find_element_by_xpath("//div/section/section/main/div/div[4]/div/div[2]/form/div[8]/div/button[2]/span").click()
#
# driver.find_element_by_xpath("//div/section/section/main/div/div[4]/div/div[2]/form/div[1]/div/div[1]/input").send_keys("102")
# driver.find_element_by_xpath("//div/section/section/main/div/div[4]/div/div[2]/form/div[2]/div/div/input").send_keys("102业主")
# driver.find_element_by_xpath("//div/section/section/main/div/div[4]/div/div[2]/form/div[3]/div/div/input").send_keys("18302102102")
# driver.find_element_by_xpath("//div/section/section/main/div/div[4]/div/div[2]/form/div[4]/div/div/input").send_keys("已")
# driver.find_element_by_xpath("//div/section/section/main/div/div[4]/div/div[2]/form/div[5]/div/div/input").send_keys("111")
# driver.find_element_by_xpath("//div/section/section/main/div/div[4]/div/div[2]/form/div[6]/div/div/input").send_keys("ceshi")
# driver.find_element_by_xpath("//div/section/section/main/div/div[4]/div/div[2]/form/div[7]/div/div/input").send_keys("南")
# driver.find_element_by_xpath("//div/section/section/main/div/div[4]/div/div[2]/form/div[8]/div/button[2]/span").click()
#
# driver.find_element_by_xpath("//div/section/section/main/div/div[4]/div/div[2]/form/div[1]/div/div[1]/input").send_keys("103")
# driver.find_element_by_xpath("//div/section/section/main/div/div[4]/div/div[2]/form/div[2]/div/div/input").send_keys("103业主")
# driver.find_element_by_xpath("//div/section/section/main/div/div[4]/div/div[2]/form/div[3]/div/div/input").send_keys("18302102102")
# driver.find_element_by_xpath("//div/section/section/main/div/div[4]/div/div[2]/form/div[4]/div/div/input").send_keys("已")
# driver.find_element_by_xpath("//div/section/section/main/div/div[4]/div/div[2]/form/div[5]/div/div/input").send_keys("111")
# driver.find_element_by_xpath("//div/section/section/main/div/div[4]/div/div[2]/form/div[6]/div/div/input").send_keys("ceshi")
# driver.find_element_by_xpath("//div/section/section/main/div/div[4]/div/div[2]/form/div[7]/div/div/input").send_keys("南")
# driver.find_element_by_xpath("//div/section/section/main/div/div[4]/div/div[2]/form/div[8]/div/button[2]/span").click()
#

screen_names = ["aaaa", "bbbbb", "ccccc", "ddddd"]
num1 = 1


def lianegeshu(num1):
    while True:
        for i in range(num1, len(screen_names)):
            print(num1, i+1)
        num1 += 1
        if num1 == len(screen_names):
            break


def sangeshu(num1):
    lianegeshu(num1)
    while True:
        for i in range(num1, len(screen_names)-1):
            print(num1, num1+1, i+2)
        num1 += 1
        if num1 == len(screen_names)-1:
            break


def sigeshu(num1):
    sangeshu(num1)
    while True:
        for i in range(num1, len(screen_names)-2):
            print(num1, num1+1, num1+2, i+3)
        num1 += 1
        if num1 == len(screen_names)-2:
            break

# if len(screen_names) == 2:
#     lianegeshu(num1)
# if len(screen_names) == 4:
#     sangeshu(num1)

if len(screen_names) == 4:
    sigeshu(num1)

# screen_names[i1+2])
# num1 += 1
# for i1 in range(num1, len(screen_names)):
#     print(num1, screen_names[i1])
# num1 += 1
# for i2 in range(num1, len(screen_names)):
#     print(num1, screen_names[i2])




    # if i == len(screen_names):
    #     num1 += 1
    #     continue

    # geshu2 = (num1, num3)
    # print(geshu2)
# num2 += 1

# driver, 类型长度, 类型名称
# def collecting_data(driver, screen_names_len, screen_name):


