"""
从emailTemplate读取文件，并生成html的String类型，需要传递一个二维列表，
eg：replaceList:[['#{姓名}', 'Jorakuten'],['#{年龄}', '14']];前者为htmlTemplate
模板中待替换字符串后者为替换字符串
"""


def replace(replaces):
    with open('../emailTemplate.html', 'r', encoding='utf-8') as file:
        html = file.read()
        for item in replaces:
            html = html.replace(item[0], str(item[1]))
    return html


testList = [['#{name}', 'Jorakuten'], ['#{year}', '1995'], ['#{month}', '09'], ['#{date}', '15'], ]
test = replace(testList)
print(test)
