from PyQt5.QtWidgets import *
import requests
import json
from bs4 import BeautifulSoup
from PyQt5.QtGui import QImage, QPixmap

import Test3

app = QApplication([])
window = QWidget()
main_line = QVBoxLayout()
#код
GameCode_ = QLineEdit()
GameCode_.setPlaceholderText("код ігри")
convert = QPushButton("Нажати")
GameName = QLineEdit()
GameName.setPlaceholderText("Введіть назву ігри")
GameCost = QLineEdit()
GameCost.setPlaceholderText("ціна")
GameYear = QLineEdit()
GameYear.setPlaceholderText("Картинка")
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
    GameCode_.setText("код: "+ info['appid'])
    GameCost.setText("ціна: "+ info['price'])
    GameLink.setText(info['url'])
    GameYear.setText(info['image'])

window.resize(300, 300)
convert.clicked.connect(get_game)
window.setLayout(main_line)
app.setStyleSheet("""
        QWidget {
            background: #F7F7F7;
        }
        
        QlineEdit 
        {
            background: yellow;
            border-radius: 5px;
            font-size: 20px;
        }
        
        QPushButton
        {
            background-color: #FFB22C;
            padding: 6px;
            border-style: groove;
            border-radius: 5px;
            font-size: 20px;
        }
    """)
window.show()
app.exec()