import requests
from bs4 import BeautifulSoup
import json


def search_steam_game(game_name):
    url = f"https://store.steampowered.com/search/suggest?term={game_name}&f=games&cc=UA&l=ukrainian"
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        match = soup.find("a", class_="match")

        if match:
            game = {
                "name": match.find("div", class_="match_name").text,
                "appid": match.get("data-ds-appid", "N/A"),
                "url": match["href"],
                "image": match.find("img")["src"],
                "price": match.find("div", class_="match_price").text.strip() if match.find("div",
                                                                                            class_="match_price") else "Ціна не вказана"
            }
            return json.dumps(game, indent=4, ensure_ascii=False)
        else:
            return json.dumps({"error": "Гра не знайдена"}, indent=4, ensure_ascii=False)
    else:
        return json.dumps({"error": f"Помилка: Код відповіді {response.status_code}"}, indent=4, ensure_ascii=False)


# Приклад використання
if __name__ == "__main__":
    game_name = input("Введіть назву гри: ")
    print(search_steam_game(game_name))