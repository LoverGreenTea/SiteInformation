from PyQt5.QtWidgets import *
import requests
import json
from bs4 import BeautifulSoup

app = QApplication([])
window = QWidget()
main_line = QVBoxLayout()
#код
GameCode_ = QLineEdit()
GameCode_.setPlaceholderText("код ігри")
convert = QPushButton("нажати")
GameName = QLineEdit()
GameName.setPlaceholderText("Введіть назву ігри")
GameCost = QLineEdit()
GameCost.setPlaceholderText("ціна")
GameYear = QLineEdit()
GameYear.setPlaceholderText("рік")
GameLink = QLineEdit()
GameLink.setPlaceholderText("link")

main_line.addWidget(GameName)
main_line.addWidget(GameCode_)
main_line.addWidget(GameCost)
main_line.addWidget(GameYear)
main_line.addWidget(GameLink)
main_line.addWidget(convert)

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
            GameCode_.setText(url['data']['data-ds-appid'])
            return json.dumps(game, indent=4, ensure_ascii=False)
        else:
            return json.dumps({"error": "Гра не знайдена"}, indent=4, ensure_ascii=False)
    else:
        return json.dumps({"error": f"Помилка: Код відповіді {response.status_code}"}, indent=4, ensure_ascii=False)

def get_game():
    gamename = GameName.text()
    info =search_steam_game(gamename)
    print(info)


convert.clicked.connect(get_game)
window.setLayout(main_line)
window.show()
app.exec()