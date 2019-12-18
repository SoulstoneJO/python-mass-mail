import smtplib
from email import encoders
from email.header import Header
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def send_mass_email(address_list, message_type, mail,
                    email_subject, from_name, to_name,
                    from_address, from_password,
                    smtp_server, server_port):
    # 初始化邮件对象
    message = MIMEMultipart()
    # 设置邮件三要素
    message['From'] = Header(from_name, 'utf-8')
    message['To'] = Header(to_name, 'utf-8')
    message['Subject'] = Header(email_subject, 'utf-8')
    # 设置邮件正文
    message.attach(MIMEText(mail, message_type, 'utf-8'))

    # 添加附件
    # with open('test.jpeg', 'rb') as f:
    #     # 设置附件的MIME和文件名，这里是png类型:
    #     mime = MIMEBase('image', 'jpeg', filename='test.png')
    #     # 加上必要的头信息:
    #     mime.add_header('Content-Disposition', 'attachment', filename='test.png')
    #     mime.add_header('Content-ID', '<0>')
    #     mime.add_header('X-Attachment-Id', '0')
    #     # 把附件的内容读进来:
    #     mime.set_payload(f.read())
    #     # 用Base64编码:
    #     encoders.encode_base64(mime)
    #     # 添加到MIMEMultipart:
    #     message.attach(mime)
    #
    # server = smtplib.SMTP(smtp_server, server_port)
    # # server.set_debuglevel(1)
    # server.starttls()
    # server.login(from_address, from_password)
    # server.sendmail(from_address, address_list, message.as_string())
    # print(from_address, " --> ", "地址为 ", address_list)
    # server.quit()
    # return print("发送成功")


send_mass_email(
    ['jorakuten1995@gmail.com'],
    'html',
    '<html><body><h1>Hello</h1>' +
    '<p><img src="cid:0"></p>' +
    '</body></html>', "带附件的测试", "送信者姓名", "收信者姓名", "973798884@qq.com",
    "odnbzsnhackabdgf", "smtp.qq.com", 587)

