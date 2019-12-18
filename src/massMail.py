import sys
from emailUtils import *
from emailElement import *


# 导入Excel配置
excelPath = config["ExcelToList"]["excelPath"]
excelStart = config["ExcelToList"]["excelStart"]
excelEnd = config["ExcelToList"]["excelEnd"]

replaceContentFrom = "".join([list(excelStart)[0], "2"])
replaceKeyTo = "".join([list(excelEnd)[0], "1"])

# 检验信息中是否有空值
tempList = generate_list(excelPath, excelStart, excelEnd)
for item in tempList:
    for i in item:
        if i is None:
            print("请检查是否保存Excel文件和初始化配置文件中Excel相关参数是否正确")
            sys.exit(0)

# 从excel中获取需要的参数，并组合成替换列表

tempHead = generate_list(excelPath, excelStart, replaceKeyTo)
tempBody = generate_list(excelPath, replaceContentFrom, excelEnd)

constructList = []  # 生成一个临时信息表
emailList = []

for item in tempBody:
    temp = dict(zip(tempHead[0], item))
    constructList.append(temp)

for item in constructList:
    element = EmailElement(item)
    element.body = replace(element.replaceList, mailTemplate)  # 生成邮件本体
    print("=================================== 这是发给 ", element.to_name, " 的邮件，请检查 ===================================")
    # print(element.body)
    emailList.append(element)


while True:
    isSend = input('是否发送邮件\n1.输入`yes`群发邮件\n2.输入`exit`退出程序\n请在此输入: ')
    if isSend == "yes":
        for element in emailList:
            if element.attachmentList is None:
                # element.send_html()
                print("发送非附件邮件成功")
            else:
                element.send_html_attachment()
                print("发送带附件邮件成功！")
    else:
        if isSend == "exit":
            print("结束程序。")
            sys.exit(0)

