import datetime
import requests
from Read_API_Data import Read_API_Data
from Request_Get_Token import get_token
import unittest
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

class Test(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        # cls.read_api = Read_API_Data()
        # cls.token = get_token()
        print("----")

    def setUp(self) -> None:
        print("执行之前")


    def test_api(self):
        print("----执行")

    def tearDown(self) -> None:
        print("执行之后")

    @classmethod
    def tearDownClass(cls) -> None:
        print(datetime.datetime.now())
        from_username = "uniquelybo@163.com"
        from_password = "CSEXBHFAMLOYAHYC"
        to_user = "uniquelybo@163.com,18334783765@163.com"
        massage = MIMEMultipart()
        # 邮件文本内容
        massage.attach(MIMEText("ceshineirong"))
        # 邮件附件
        file = MIMEApplication(open("log.txt", "r", encoding="utf-8").read())
        file.add_header('Content-Disposition', 'attachment', filename="log.txt")
        massage.attach(file)
        massage['Subject'] = "ceshi"
        massage['From'] = from_username
        massage['To'] = to_user
        print(type(to_user))
        try:
            server = smtplib.SMTP()
            server.connect("smtp.163.com", 25)
            server.login(from_username, from_password)
            server.sendmail(from_username, to_user.split(","), massage.as_string())
            print("shibai")
        except Exception as x:
            print(x)
        server.quit()

if __name__ == "__main__":
    unittest.main()
print(datetime.datetime.now())
read_api = Read_API_Data()
read_api.execute_api()
url = "http://liveapi.ttmv.com/MobileLive/getLastOpus"
data = {"token_userid": 348295,
        "anchorid": 346696,
        "version": "4.6.3",
        "device": 2,
        "platform": 1,
        "token": "qrex6kfspjx0a5i2"}
response = requests.post(url=url, data=data)
print(response.content.decode("utf-8"))
requests.post()
