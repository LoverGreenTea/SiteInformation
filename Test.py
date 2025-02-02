import requests
import json
from bs4 import BeautifulSoup

# URL для пошуку гри
url = "https://store.steampowered.com/search/suggest?term=Half-Life&f=games&cc=UA&l=ukrainian"

# Виконання HTTP-запиту
response = requests.get(url)

# Перевірка статусу відповіді
if response.status_code == 200:
    # Обробка HTML-відповіді
    soup = BeautifulSoup(response.text, "html.parser")
    games = []

    for match in soup.find_all("a", class_="match"):
        game = {
            "name": match.find("div", class_="match_name").text,
            "appid": match["data-ds-appid"],
            "url": match["href"],
            "image": match.find("img")["src"],
            "price": match.find("div", class_="match_price").text.strip()
        }
        games.append(game)

    print(json.dumps(games, indent=4, ensure_ascii=False))
else:
    print(f"Помилка: Код відповіді {response.status_code}")
