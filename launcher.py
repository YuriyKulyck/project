import json
import requests
from PyQt5.QtWidgets import *
import main

app = QApplication([])
window = QWidget()

mainline = QVBoxLayout()
hline = QHBoxLayout()

text = QLabel("Введіть назву держави:")
countryname = QLineEdit()
getinfo = QPushButton("Отримати всі дані про державу:")
info = QLabel("Результат: ")

mainline.addLayout(hline)
mainline.addWidget(countryname)
hline.addWidget(text)
mainline.addWidget(getinfo)
mainline.addWidget(info)

window.setLayout(mainline)

def source():
    url = f"https://restcountries.com/v3.1/name/{countryname.text()}"
    response = requests.get(url)
    if response.status_code == 200:
        countries = response.json()
        data = countries[0]
        info_text = f"name: {data['name']['common']}\n" \
                    f"area: {data.get('area')} km per square\n" \
                    f"borders: {data.get('borders')}\n" \
                    f"capital: {data.get('capital')}\n" \
                    f"continents: {data.get('region')}\n" \
                    f"languages: {', '.join(data.get('languages', {}).keys())}\n" \
                    f"currencies: {', '.join(data.get('currencies', {}).keys())}\n" \
                    f"population: {data.get('population')} people\n"
        info.setText(info_text)
    else:
        info.setText("Помилка отримання даних з сервера")

getinfo.clicked.connect(source)
window.show()
app.exec()
