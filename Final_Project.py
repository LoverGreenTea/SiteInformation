from PyQt5.QtWidgets import *
import requests
import json
from bs4 import BeautifulSoup

import Test3

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


def get_game():
    gamename = GameName.text()
    info =Test3.search_steam_game(gamename)
    print(info)
    print(info['url'])
    GameCode_.setText(info['appid'])
    GameCost.setText(info['price'])
    GameLink.setText(info['url'])

window.resize(300, 300)
convert.clicked.connect(get_game)
window.setLayout(main_line)
app.setStyleSheet("""
        QWidget {
            background: #3C2A21;
        }
        
        QlineEdit
        {
            background: D5CEA3;
            border-color: #1A3636;
        }
        
        QPushButton
        {
            background: #D5CEA3;
        }
    """)
window.show()
app.exec()