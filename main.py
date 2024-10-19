import csv  # Импортируем модуль csv для того, чтобы прочитать данные из csv файла
import matplotlib.pyplot as plt  # Импортируем пакет matplotlib.pyplot из модуля matplotlib для того, чтобы построить
# графики


# Функция, которая принимает путь к файлу и возвращает список продаж
def read_sales_data(file_path: str) -> list:
    array = []
    with open(file_path, mode='r', encoding="utf-8") as file:
        csvFile = csv.reader(file)
        for lines in csvFile:
            d = {"product_name": lines[0].strip(), "quantity": lines[1].strip(), "price": lines[2].strip(),
                 "date": lines[3].strip()}
            array.append(d)
    return array


# Функция, которая принимает список продаж и возвращает словарь, где ключ - название продукта, а значение - общая
# сумма продаж этого продукта
def total_sales_per_product(sales_data: list) -> dict:
    d = dict()
    for sales in sales_data:
        if sales["product_name"] in d:
            d[sales["product_name"]] += int(sales["quantity"]) * float(sales["price"])
        else:
            d[sales["product_name"]] = int(sales["quantity"]) * float(sales["price"])
    return d


# Функция, которая принимает список продаж и возвращает словарь, где ключ - дата, а значение общая сумма продаж за
# эту дату.
def sales_over_time(sales_data: list) -> dict:
    d = dict()
    for sales in sales_data:
        if sales["date"] in d:
            d[sales["date"]] += int(sales["quantity"]) * float(sales["price"])
        else:
            d[sales["date"]] = int(sales["quantity"]) * float(sales["price"])
    d = dict(sorted(d.items()))
    return d


# Функция, которая выводит список продуктов, принёсших наибольшую выручку
def max_money_per_product(list_products_money: dict) -> None:
    maxi_money = max(list_products_money.values())
    arr = []
    for product in list_products_money.keys():
        if list_products_money[product] == maxi_money:
            arr.append(product)
    print(f"Продукт(-ы) принесший(-ие) наибольшую прибыль: {arr}")


# Функция, которая выводит список самых прибыльных дней
def max_money_per_day(list_day_money: dict) -> None:
    maxi_money = max(list_day_money.values())
    arr = []
    for day in list_day_money.keys():
        if list_day_money[day] == maxi_money:
            arr.append(day)
    print(f"Самый(-ые) прибыльный(-ые) день(дни): {arr}")


lst = read_sales_data("data.csv")

dict_products = total_sales_per_product(lst)
dict_day = sales_over_time(lst)

max_money_per_product(dict_products)
max_money_per_day(dict_day)

# Создаём массивы данных для построения графика общей суммы продаж по каждому продукту
x_products = dict_products.keys()
y_products = dict_products.values()

plt.plot(x_products, y_products)
plt.show()

# Создаём массивы данных для построения графика общей суммы продаж по дням
x_days = dict_day.keys()
y_days = dict_day.values()

plt.plot(x_days, y_days)
plt.show()
