import requests
import json

url = "https://restcountries.com/v3.1/region/europe"
response = requests.get(url)
data = response.json()

results = []

for country in data:
    name = country.get("name", {}).get("common")
    capital = country.get("capital", ["N/A"])[0]
    area = country.get("area", 0)
    population = country.get("population", 0)
    currencies = country.get("currencies", {})
    currency_names = [currencies[c]["name"] for c in currencies] if currencies else ["N/A"]

    if area > 150000 and "Euro" not in currency_names:
        density = population / area if area else 0
        results.append({
            "name": name,
            "capital": capital,
            "area": area,
            "population": population,
            "currency": ", ".join(currency_names),
            "density": density,
            "flag_url": country.get("flags", {}).get("png")
        })

with open("results.json", "w", encoding="utf-8") as f:
    json.dump(results, f, ensure_ascii=False, indent=4)

top3 = sorted(results, key=lambda x: x["density"], reverse=True)[:3]
print("Топ-3 страны по плотности населения:")
for c in top3:
    print(c["name"])

for c in top3:
    flag_url = c["flag_url"]
    if flag_url:
        flag_resp = requests.get(flag_url)
        with open(f"{c['name']}_flag.png", "wb") as f:
            f.write(flag_resp.content)
