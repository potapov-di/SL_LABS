import requests
from bs4 import BeautifulSoup
import csv

base_url = "https://worldathletics.org/records/toplists/throws/{discipline}/outdoor/{gender}/senior/{year}"

disciplines = {
    "shot-put": "Толкание ядра",
    "discus-throw": "Метание диска",
    "javelin-throw": "Метание копья",
    "hammer-throw": "Метание молота"
}

genders = ["men", "women"]

years = range(2001, 2025)

results = []

for discipline in disciplines:
    for gender in genders:
        for year in years:
            url = base_url.format(discipline=discipline, gender=gender, year=year)
            response = requests.get(url)
            soup = BeautifulSoup(response.text, "html.parser")
            table = soup.find("table", class_="records-table")
            if not table:
                continue

            first_row = table.find("tr")
            if not first_row:
                continue

            cells = first_row.find_all("td")
            if len(cells) < 4:
                continue


            result = cells[0].get_text(strip=True)
            athlete = cells[1].get_text(strip=True)
            country = cells[2].get_text(strip=True)
            date = cells[3].get_text(strip=True)

            results.append([year, disciplines[discipline], gender, athlete, country, result, date])
            
with open("top_results.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Год", "Дисциплина", "Пол", "Имя спортсмена", "Страна", "Результат", "Дата"])
    writer.writerows(results)