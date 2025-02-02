import requests
import json
from bs4 import BeautifulSoup


def search_steam_game(game_name):
    url = f"https://store.steampowered.com/search/suggest?term={game_name}&f=games&cc=UA&l=ukrainian"
    response = requests.get(url)

    if response.status_code == 200:
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

        return json.dumps(games, indent=4, ensure_ascii=False)
    else:
        return json.dumps({"error": f"Помилка: Код відповіді {response.status_code}"}, indent=4, ensure_ascii=False)


# Приклад використання
if __name__ == "__main__":
    game_name = input("Введіть назву гри: ")
    print(search_steam_game(game_name))