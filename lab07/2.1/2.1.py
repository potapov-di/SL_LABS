import csv

def find_min_max_stock(data):
    print("Минимальное по Stock")
    min_stock = min(data , key=lambda d: int(d["Stock"]))  
    print(min_stock)
    print("Максимальное по Stock")
    max_stock = max(data , key=lambda d: int(d["Stock"]))  
    print(max_stock)

def count_low_stock_items(data):
    i = 0
    print ("Товары , запасы которых ниже минимального уровня")
    for d in data:
        if int(d["MinStock"]) > int(d["Stock"]):
            print (d)
            i+=1
    print("Их кол-во")
    print(i)


def calculate_avg_electronics_stock(data):
    print("Вычисления среднего запаса товаров по категории Electronics")
    value = []
    for i in data:
        if i["Category"] == "Electronics":
            value.append(int(i['Stock']))
    print(sum(value)/len(value))

def count_products_by_category(data):
    need_found = input("Введите категорию для поиска ")
    print(f"Количество товаров категории {need_found}")
    value = []
    for i in data:
        if i["Category"] == need_found:
            value.append(int(i['Stock']))
    print(sum(value))
    


with open("8.csv" , newline= "") as file:
    reader = csv.DictReader(file,delimiter=";")
    data = [row for row in reader]

for i in data:
    print (i)

find_min_max_stock(data)
count_low_stock_items(data)
calculate_avg_electronics_stock(data)
count_products_by_category(data)