import json
from collections import defaultdict


with open("8.json", "r", encoding="utf-8") as f:
    data = json.load(f)

software_data = data["software"]


def find_software_by_version(version, data):
    return [sw for sw in data if sw["version"] == version]


def count_software_by_license(data):
    license_count = defaultdict(int)
    for sw in data:
        license_count[sw["license"]] += 1
    return dict(license_count)

def calculate_avg_price_by_vendor(data):
    vendor_prices = defaultdict(list)
    for sw in data:
        vendor_prices[sw["vendor"]].append(sw["price"])
    return {vendor: sum(prices)/len(prices) for vendor, prices in vendor_prices.items()}


filtered_data = find_software_by_version("2023", software_data)

with open("out.json", "w", encoding="utf-8") as f:
    json.dump(filtered_data, f, ensure_ascii=False, indent=4)


print("ПО версии 2023:", find_software_by_version("2023", software_data))
print("Количество по лицензиям:", count_software_by_license(software_data))
print("Средняя цена по вендорам:", calculate_avg_price_by_vendor(software_data))
