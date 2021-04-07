from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from user_login import User_Login
from page.First_Page import First_Page
from page.user_list import User_List
from page.device_details import Device_Details
from page.Payment_Record import Payment_Record
from page.Bill_Details_Page import Bill_Details_Page
from page.Set_Payment_Items import Set_Payment_Items
from selenium.webdriver.common.action_chains import ActionChains
from building import Building
from payment_record import Payment_Record
from paid_bill import Paid
from page.index import Index

options = Options()
options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
driver = webdriver.Chrome("/Users/tuishoutest/Downloads/chromedriver", options=options)
wait = WebDriverWait(driver, 5)

# index = Index(driver)
# index.click_login("ceshixiaoqu1", "123456")


first_page = First_Page(driver)


# 设备控制按钮名称
def check_device_button_name():
    user_list = User_List(driver)
    device_details = Device_Details(driver)
    first_page.choose_floor(1).click()
    first_page.choose_unit(1).click()
    user_list.choose_cat(2).click()

    content = {1: "强制开启", 2: "强制关闭", 3: "恢复计费"}
    for item in content.items():
        con = device_details.choose_device_control(2, item[0]).text
        if con == item[1]:
            print(con, "已修改")
        else:
            print(con, "未修改")

    print(driver.title)


def check_pay_type():
    first_page.index_page.click()
    first_page.pay.click()
    payment_record = Payment_Record(driver)
    try:
        payment_record.find_menu_by_str("支付方式")
    except:
        print("缴费记录未显示支付方式")


def bill_indexes():
    first_page.index_page.click()
    first_page.bill.click()
    bill_details_page = Bill_Details_Page(driver)
    pay_state = bill_details_page.pay_state
    ActionChains(driver).move_to_element(pay_state).perform()
    try:
        driver.find_element_by_xpath("//[text()='身份']")
        print("索引到缴费记录")
    except:
        print("--------")


def screen():
    first_page.index_page.click()
    first_page.bill.click()
    bill_details_page = Bill_Details_Page(driver)
    first_page.index_page.click()
    first_page.pay.click()
    payment_record = Payment_Record(driver)


def payment_name():
    first_page.index_page.click()
    first_page.add_payment.click()
    set_payment_items = Set_Payment_Items(driver)
    # 缴费项名称
    content = [
        '缴费项名称缴费项名称缴费项名称',
        '缴费项名称缴费项名称缴费项名',
        '缴费项名称缴费项名称缴费项',
        '缴费',
        '缴',
        '012345601234567',
        '01234560123456',
        '0123456012345',
        '01',
        '0',
        'abcdefghijklmno',
        'abcdefghijklmn',
        'abcdefghijklm',
        'ab',
        'a',
        '缴费项jfx123',
        '缴费项**&$^'
    ]
    pay_name = set_payment_items.payment_name
    for con in content:
        set_payment_items.input_content(pay_name, con)
        set_payment_items.submit.click()
        try:
            set_payment_items.except_element()
        except:
            print(con, "不符合条件")
        set_payment_items.clear_content(pay_name)
# 设备控制按钮名称
# check_device_button_name()
# 缴费记录显示支付方式
# check_pay_type()
# 账单索引到缴费记录
# bill_indexes()
# 账单列表/缴费记录筛选功能
# screen()
# 缴费项名称
payment_name()