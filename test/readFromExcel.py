"""
从`client_messages.xls`中获取信息，并生成对应信息的二维数组
[['客户编号', '客户姓名', '客户邮箱地址'],
 [1, 'Jorakuten', 'jorakuten1995@gmail.com'],
 [2, 'Jorakuten', 'jorakuten1995@gmail.com'],
 [3, 'Jorakuten', 'jorakuten1995@gmail.com'],
 ...
 ...
 [...........................................]]

 注意：由于现在没有其它业务需求，暂时生成的数组：如下所示：

 该二维数组作用主要用来填充SMTP协议中的收信者addressx参数应该
 作为xlsx的path："client_messages.xlsx"
 生成二维数组的cell范围
                area_from：'A1'
                area_to: 'C7'
"""
import openpyxl
from emailElement import EmailElement


def generate_list(path, area_from, area_to):
    client_list = []
    wb = openpyxl.load_workbook(path)
    sheet = wb["Sheet1"]

    for objectsInRow in sheet[area_from:area_to]:
        temp_list = []
        for obj in objectsInRow:
            temp_list.append(obj.value)
        client_list.append(temp_list)
    return client_list


tempHead = generate_list("../parameters.xlsx", "A1", "G1")
tempList = generate_list("../parameters.xlsx", "A2", "G3")

constructList = []

for item in tempList:
    # print(item)
    # print(tempHead[0])
    temp = dict(zip(tempHead[0], item))
    constructList.append(temp)

print(constructList)

# constructList每一个item表示一封邮件

email = []

for item in constructList:
    element = EmailElement(item)
    email.append(element)

print(email)

