import json
import requests
import self
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import *
from googletrans import Translator
import main

app = QApplication([])
window = QWidget()

app.setStyleSheet("""
    QWidget{
        background-image: url('download1.jpg');
        background-position: center; 
        background-repeat: no-repeat; 
        background-size: cover; 
        background-width: 100%;
    }
    QLabel{
        background-image: none;
    }
    QPushButton{
        background-image: none;
        border: 2px solid;
        border-radius: 9.5px;
        border-color:qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1,stop: 0 maroon, stop: 0.4 blue,stop: 1 violet);
        background:qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1,stop: 0.1 gold, stop: 0.4 lime,stop: 1 blue);
    }
    QLineEdit{
        background-image: none;
        border: 4px solid;
        border-radius: 7px;
        border-color:qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1,stop: 0.3 crimson, stop: 0.47 yellow,stop: 0.86 green);
        background:qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1,stop: 0.05 violet, stop: 0.75 lime,stop: 0.95 aquamarine);
    }


    QPushButton:hover {
        background-image: none;
        background:qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1,stop: 0 red, stop: 0.4 gold,stop: 1 aqua);
    }
""")

mainline = QVBoxLayout()
hline = QHBoxLayout()

label = QLabel()
text = QLabel("Введіть назву держави:")
countryname = QLineEdit()
getinfo = QPushButton("Отримати всі дані про державу:")
info = QLabel("Результат: ")

pixmap = QPixmap('png-transparent-europe-map-europe-white-photography-computer-wallpaper.png')
pixmap=pixmap.scaledToWidth(200)
label.setPixmap(pixmap)

mainline.addLayout(hline)
hline.addWidget(label)
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
        info_text = name_text = f"name: {data['name']['common']}"
        area_text = f"area: {data.get('area')} km per square"
        borders_text = f"borders: {data.get('borders')}"
        capital_text = f"capital: {data.get('capital')}"
        continents_text = f"continents: {data.get('region')}"
        languages_text = f"languages: {', '.join(data.get('languages', {}).keys())}"
        currencies_text = f"currencies: {', '.join(data.get('currencies', {}).keys())}"
        population_text = f"population: {data.get('population')} people"
        info.setText(info_text, area_text, borders_text, capital_text, continents_text, languages_text, currencies_text, population_text)
    else:
        info.setText("Помилка отримання даних з сервера")

getinfo.clicked.connect(source)
window.show()
app.exec()
