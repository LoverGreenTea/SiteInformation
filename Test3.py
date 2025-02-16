import requests
from bs4 import BeautifulSoup
import json
from datetime import datetime


def search_steam_game(game_name):
    session = requests.Session()
    url = f"https://store.steampowered.com/search/suggest?term={game_name}&f=games&cc=UA&l=ukrainian"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"
    }

    response = session.get(url, headers=headers)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        match = soup.find("a", class_="match")

        if match:
            release_date_tag = match.find("div", class_="match_released")
            release_date = release_date_tag.text.strip() if release_date_tag else "Дата виходу не вказана"

            game = {
                "name": match.find("div", class_="match_name").text,
                "appid": match.get("data-ds-appid", "N/A"),
                "url": match["href"],
                "image": match.find("img")["src"],
                "price": match.find("div", class_="match_price").text.strip() if match.find("div",
                                                                                            class_="match_price") else "Ціна не вказана",
            }
            return game
        else:
            return {"error": "Гра не знайдена"}
    else:
        return {"error": f"Помилка: Код відповіді {response.status_code}"}