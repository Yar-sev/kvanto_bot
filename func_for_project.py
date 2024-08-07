from main_SQL import *
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