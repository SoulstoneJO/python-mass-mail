import openpyxl


def generate_list(path, area_from, area_to):  # 从excel获取参数的方法
    client_list = []
    wb = openpyxl.load_workbook(path)
    sheet = wb["Sheet1"]

    for objectsInRow in sheet[area_from:area_to]:
        temp_list = []
        for obj in objectsInRow:
            temp_list.append(obj.value)
        client_list.append(temp_list)
    return client_list


def replace(replaces, templatepath):  # 用来替换字符串，生成邮件实体
    with open(templatepath, 'r', encoding='utf-8') as file:
        html = file.read()
        for item in replaces:
            html = html.replace(item[0], str(item[1]))
    return html