from PyQt5.QtWidgets import *
import requests


app = QApplication([])
window = QWidget()

valcode_ = QLineEdit()
valcode_.setPlaceholderText("Введіть валюту")
year = QLineEdit()
year.setPlaceholderText("рік")
howm_much = QLineEdit()
howm_much.setPlaceholderText("кількість")
resultat = QLineEdit()
resultat.setPlaceholderText("результат")
convert = QPushButton("")
main_line = QVBoxLayout()


main_line.addWidget(valcode_)
main_line.addWidget(year)
main_line.addWidget(howm_much)
main_line.addWidget(resultat)
main_line.addWidget(convert)

def Final():
    valcode = valcode_.text()
    rate = year.text()
    response = requests.get(
        f"https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?valcode={valcode}&date={rate}&json")
    data = response.json()
    rate = data[0]['rate']
    resultat.setText(str(rate))
#HELLO
convert.clicked.connect(Final)

window.setLayout(main_line)
window.show()
app.exec()