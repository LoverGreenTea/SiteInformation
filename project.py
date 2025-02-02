from PyQt5.QtWidgets import *
import requests

app = QApplication([])
window = QWidget()
main_line = QVBoxLayout()
#код
GameCode_ = QLineEdit()
GameCode_.setPlaceholderText("Введіть код ігри")
convert = QPushButton("нажати")
GameName = QLineEdit()
GameName.setPlaceholderText("Назва ігри")
GameCost = QLineEdit()
GameCost.setPlaceholderText("ціна")
GameYear = QLineEdit()
GameYear.setPlaceholderText("рік")
GameLink = QLineEdit()
GameLink.setPlaceholderText("link")


main_line.addWidget(GameCode_)
main_line.addWidget(GameName)
main_line.addWidget(GameCost)
main_line.addWidget(GameYear)
main_line.addWidget(GameLink)
main_line.addWidget(convert)

def Steam_Game():
    GameCode = GameCode_.text()
    gamename = GameName.text()
    response = requests.get(
        f"https://store.steampowered.com/api/appdetails?appids={GameCode}")
    data = response.json()
    gamename = data[GameCode]['data']['name']
    GameName.setText(data[GameCode]['data']['name'])
    GameCost.setText(data[GameCode]['data']['price_overview']['final_formatted'])
    GameYear.setText(data[GameCode]['data']['release_date']['date'])
    GameLink.setText(data[GameCode]['data']['support_info']['url'])
convert.clicked.connect(Steam_Game)
window.setLayout(main_line)
window.show()
app.exec()