import configparser
import smtplib
import sys
from email import encoders
from email.header import Header
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
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


# 添加附件方法
def add_attachment(filename, count):
    with open(filename, 'rb') as f:
        # 设置附件
        mime = MIMEBase(filename.split(".")[0], filename.split(".")[1], filename=filename)
        # 加上必要的头信息:
        mime.add_header('Content-Disposition', 'attachment', filename=filename)
        count_label = "".join(["<", str(count), ">"])
        mime.add_header('Content-ID', count_label)
        mime.add_header('X-Attachment-Id', str(count))
        # 把附件的内容读进来:
        mime.set_payload(f.read())
        # 用Base64编码:
        encoders.encode_base64(mime)
    return mime


class EmailElement:
    to_name = ""
    address = ""
    email_subject = ""
    replaceList = []
    body = ""
    attachmentList = ""

    def __init__(self, dict):  # 构造器方法
        self.replaceList = []
        self.to_name = dict["to_name"]
        self.address = dict["address"]
        self.email_subject = dict["email_subject"]
        if dict["attachment"] == "null" or dict["attachment"].find(".") < 0:
            self.attachmentList = None
        else:
            self.attachmentList = dict["attachment"].split(",")
        for k in dict:
            if "#" in k:
                self.replaceList.append([k, dict[k]])

    def send_html(self):
        message = MIMEText(self.body, message_type, 'utf-8')

        message['From'] = Header(from_name, 'utf-8')
        message['To'] = Header(self.to_name, 'utf-8')
        message['Subject'] = Header(self.email_subject, 'utf-8')

        server = smtplib.SMTP(smtp_server, server_port)
        # server.set_debuglevel(1)
        server.ehlo()
        server.starttls()
        server.login(from_address, from_password)
        server.sendmail(from_address, [self.address], message.as_string())
        print(from_address, " --> ", "地址为 ", self.address)
        server.quit()

    def send_html_attachment(self):
        # 初始化邮件对象
        message = MIMEMultipart()
        # 设置邮件三要素
        message['From'] = Header(from_name, 'utf-8')
        message['To'] = Header(self.to_name, 'utf-8')
        message['Subject'] = Header(self.email_subject, 'utf-8')
        # 设置邮件正文
        message.attach(MIMEText(self.body, message_type, 'utf-8'))

        # 添加附件
        for index in range(len(self.attachmentList)):
            mime = add_attachment(self.attachmentList[index], index)
            message.attach(mime)

        print("...准备发送...")
        server = smtplib.SMTP(smtp_server, server_port)
        # server.set_debuglevel(1)
        server.starttls()
        server.login(from_address, from_password)
        server.sendmail(from_address, [self.address], message.as_string())
        print(from_address, " --> ", "地址为 ", self.address)
        server.quit()
