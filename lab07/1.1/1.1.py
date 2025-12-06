def info(x):
    for os_data in x:
        values = os_data.values()
        yield sum(values) / len(values)

def max_value(x):
        for os_data in x:
            max_val = max(os_data.values())
            for year, value in os_data.items():
                if value == max_val:
                    yield year


def min_value(x):
    for os_data in x:
        min_val = min(os_data.values())
        for year, value in os_data.items():
            if value == min_val:
                yield year


os_market = {
    "Windows": {"2018": 76.5, "2019": 74.3, "2020": 72.1, "2021": 69.8, "2022": 67.2},
    "macOS": {"2018": 12.8, "2019": 14.2, "2020": 15.1, "2021": 16.5, "2022": 17.9},
    "Linux": {"2018": 1.9, "2019": 2.1, "2020": 2.3, "2021": 2.6, "2022": 2.9},
    "Chrome OS": {"2018": 0.8, "2019": 1.2, "2020": 1.8, "2021": 2.3, "2022": 3.1},
    "Android": {"2018": 2.1, "2019": 2.8, "2020": 3.5, "2021": 4.2, "2022": 5.1},
    "iOS": {"2018": 1.5, "2019": 2.0, "2020": 2.8, "2021": 3.5, "2022": 4.3},
    "Other": {"2018": 4.4, "2019": 3.4, "2020": 2.4, "2021": 2.1, "2022": 0.5}
}

print("Все OC и их средняя доля на рынке за 5 лет")
count = info(os_market.values())

for j in os_market.keys():
    print (j)
    print(next(count))

print("Год с минимальной и год с максимальной долей на рынке каждой OC")

max_v = max_value(os_market.values())
min_v = min_value(os_market.values())


for j in os_market.items():
    print (j)
    max_val = next(max_v)
    min_val = next(min_v)
    print(f"Максимальное значение:{max_val}")
    print(f"Минимальное значение:{min_val}")


for j , v in os_market.items():
    print (f"{j} (2020) : {v['2020']}")

increased_os = []

for j , v in os_market.items():
    first_year = v["2018"]
    last_year = v["2022"]
    if last_year > first_year * 1.2:
        print(f"{j} : {first_year} -> {last_year}")
        increased_os.append(j)


import shelve
with shelve.open('os_market_data') as db:
    db['os_market'] = os_market
    db['increased_os'] = increased_os