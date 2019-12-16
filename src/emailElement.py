import configparser
import smtplib
from email.header import Header
from email.mime.text import MIMEText

# 从`fields.ini`中接收配置参数
config = configparser.ConfigParser()
config.read('../fields.ini', 'utf-8')

# 导入服务器相关配置
smtp_server = config["mailServer"]["smtp_server"]
server_port = config["mailServer"]["server_port"]
from_address = config["mailServer"]["from_address"]
from_password = config["mailServer"]["from_password"]

# 导入Email基本配置
mailTemplate = config["mailContent"]["mailTemplate"]
message_type = config["mailContent"]["message_type"]
from_name = config["mailContent"]["from_name"]


class EmailElement:
    to_name = ""
    address = ""
    email_subject = ""
    replaceList = []
    body = ""

    def __init__(self, dict):   # 构造器方法
        self.to_name = dict["to_name"]
        self.address = dict["address"]
        self.email_subject = dict["email_subject"]
        for k in dict:
            if "#" in k:
                self.replaceList.append([k, dict[k]])

    def send(self):
        message = MIMEText(self.body, message_type, 'utf-8')

        message['From'] = Header(from_name, 'utf-8')
        message['To'] = Header(self.to_name, 'utf-8')
        message['Subject'] = Header(self.email_subject, 'utf-8')

        server = smtplib.SMTP(smtp_server, server_port)
        server.set_debuglevel(1)
        server.starttls()
        server.login(from_address, from_password)
        server.sendmail(from_address, [self.address], message.as_string())
        print(from_address, " --> ", "地址为 ", self.address)
        server.quit()
        return print("发送成功")

