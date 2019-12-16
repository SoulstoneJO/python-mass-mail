import configparser
from emailUtils import *
from emailElement import *


# 导入Excel配置
excelPath = config["ExcelToList"]["excelPath"]
replaceKeyFrom = config["ExcelToList"]["replaceKeyFrom"]
replaceKeyTo = config["ExcelToList"]["replaceKeyTo"]
replaceContentFrom = config["ExcelToList"]["replaceContentFrom"]
replaceContentTo = config["ExcelToList"]["replaceContentTo"]

# 从excel中获取需要的参数，并组合成替换列表
tempHead = generate_list(excelPath, replaceKeyFrom, replaceKeyTo)
tempList = generate_list(excelPath, replaceContentFrom, replaceContentTo)


constructList = []  # 生成一个临时信息表
emailList = []      # 生成电子邮件表

for item in tempList:
    temp = dict(zip(tempHead[0], item))
    constructList.append(temp)

for item in constructList:
    element = EmailElement(item)
    element.body = replace(element.replaceList, mailTemplate)  # 生成邮件本体
    element.send()  # 发送邮件



