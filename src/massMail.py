import configparser

# 从`fields.ini`中接收配置参数

import configparser

config = configparser.ConfigParser()
config.read('fields.ini', 'utf-8')

smtp_server = config["mailServer"]["smtp_server"]
server_port = config["mailServer"]["server_port"]
from_address = config["mailServer"]["from_address"]
from_password = config["mailServer"]["from_password"]

mailTemplate = config["mailContent"]["mailTemplate"]
message_type = config["mailContent"]["message_type"]
email_subject = config["mailContent"]["email_subject"]

to_names = (config["mailContent"]["to_names"]).split(",")
address_list = (config["mailContent"]["address_list"]).split(",")


# 用来替换html模板中的字符串的方法
def replace(replaces):
    with open('../emailTemplate.html', 'r', encoding='utf-8') as file:
        html = file.read()
        for item in replaces:
            html = html.replace(item[0], item[1])
    return html

# 给邮件模板注入字符串数组，并生成邮件列表

# 发送邮件
