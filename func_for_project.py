from main_SQL import *
import datetime
okonchanie = {0 : "ов",
              1 : "",
              2 : "а",
              3 : "а",
              4 : "а",
              5 : "ов",
              6 : "ов",
              7 : "ов",
              8 : "ов",
              9 : "ов"}
applic = {"True" : "выполнено",
          "False" : "невыполнено"}
def subnet():
    n = 0
    b = 0
    text = ""
    for i in datafr("store", "products"):
        if i[3] == "service":
             n += 1
        elif i[3] == "product":
             b += 1
    text += f"товаров - {b}, услуги - {n}"
    for i in datafr("store", "products"):
        line = f"{i[0]}. {i[1]}, стоимость {i[4]}"
        text = text + "\n" + line
    return text
def product_def(id):
    text = ""
    if id.isdigit():
        data = datafr("store", "products")
        if int(id) <= len(data):
            for i in data:
                if i[0] == int(id):
                    num = int(i[4])
                    len0 = len(str(num))
                    kvant = "Квантокоин"
                    if len0 > 1:
                        len1 = len0 - 1
                        symbol0 = str(num)[len1]
                        kvant += okonchanie[int(symbol0)]
                    else:
                        kvant += okonchanie[num]
                    text += f"{i[0]}. {i[1]}\n{i[2]}\n{i[4]} {kvant}"
                    return text
        else:
            text = "нет такого товара"
            return text
    else:
        text = "не правильный ввод"
        return text
def application(user, id):
    data = datafr("store", "products")
    for i in data:
        if i[0] == int(id):
            prod = i[1]
    insert_applic(user, prod, datetime.date.today())
def application_list():
    text = ""
    data = datafr("applications", "applications")
    for i in data:
        if i[5] == "False":
            text += f"\n{i[0]}.{i[1]}, {i[2]}, {applic[i[5]]}"
    if text == "":
        text += "нет заявок"
        return text
    else:
        return text
def user_appl_list(id):
    text = ""
    data = datafr("applications", "applications")
    for i in data:
        if i[1] == int(id):
            text += f"\n{i[0]}. {i[1]}, {i[2]}, {applic[i[5]]}"
    if text == "":
        text += "нет покупок"
        return text
    else:
        return text
def user_list():
    text = ""
    data = datafr("user", "users")
    for i in data:
        text += f"\n{i[0]}. {i[4]} {i[1]}, статус - {i[3]}, счёт - {i[2]}"
    return text
def correction():
    data = datafr("store", "products")
    num = 0
    for i in data:
        num += 1
        update_data("store", "products", i[1], "id", num, "article")
def applic_shut(id):
    update_data("applications", "applications", id, "done", "True", "id")
    update_data("applications", "applications", id, "date_comple", datetime.date.today(), "id")
def change(id):
    data = select_data_num(id)
    if data[0][3] == "admin":
        update_data("user", "users", id, "status", "user", "id")
    elif data[0][3] == "user":
        update_data("user", "users", id, "status", "admin", "id")