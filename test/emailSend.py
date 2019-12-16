"""
群发邮件服务，外界需要传送的参数：
    一个包含所有接收者邮件地址的列表: address_list
    一个解析完成的html -> String字符串 mail
        message_type: 'plain' or 'html'
            'plain' for simple message
            'html' for decoding html file
    邮件主题： email_subject
    邮件发出者名称： from_name
    邮件接收者名称： to_name
    邮件发出者地址：from_address
    邮件发出者密码(授权码)：from_password
    SMTP服务器地址： SMTP_server
"""
import smtplib
from email.header import Header
from email.mime.text import MIMEText


def send_mass_email(address_list, message_type, mail,
                    email_subject, from_name, to_name,
                    from_address, from_password,
                    smtp_server, server_port):
    message = MIMEText(mail, message_type, 'utf-8')

    message['From'] = Header(from_name, 'utf-8')
    message['To'] = Header(to_name, 'utf-8')
    message['Subject'] = Header(email_subject, 'utf-8')

    server = smtplib.SMTP(smtp_server, server_port)
    server.set_debuglevel(1)
    server.starttls()
    server.login(from_address, from_password)
    server.sendmail(from_address, address_list, message.as_string())
    print(from_address, " --> ", "地址为 ", address_list)
    server.quit()
    return print("发送成功")


send_mass_email(
    ['jorakuten1995@gmail.com', 'letian1995@softbank.ne.jp'],
    'plain',
    '主体内容：此时测试txt内容', "邮件主题", "送信者", "收信者", "973798884@qq.com",
    "odnbzsnhackabdgf", "smtp.qq.com", 587)

