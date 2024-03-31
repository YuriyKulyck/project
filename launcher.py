import json
import requests
import self
import share
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import *
from googletrans import Translator
import main

app = QApplication([])
window = QWidget()

app.setStyleSheet("""
    QWidget{
        background-image: url('HD-wallpaper-beautiful-sea-view-sea-nature.jpg');
        background-position: center; 
        background-repeat: no-repeat; 
        background-size: cover; 
        background-width: 100%;
    }
    QLabel{
        background: transparent;
        color: LightSkyBlue;
        border: 2.5px solid;
        border-radius: 6.5px;
        background-color: rgba(0, 0, 0, 0.55);
        border-color:qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1,stop: 0 violet, stop: 0.4 yellow,stop: 1 Lightskyblue);
        font: italic semi bold 1.6em system-ui;
        font-size: 15px;
    }
    QPushButton{
        background-image: none;
        border: 2px solid;
        border-radius: 9.5px;
        color: crimson;
        border-color:qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1,stop: 0 maroon, stop: 0.4 blue,stop: 1 violet);
        background:qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1,stop: 0.1 gold, stop: 0.4 lime,stop: 1 blue);
        font: bold 2.2em system-ui;
    }
    QLineEdit{
        background-image: none;
        border: 4px solid;
        border-radius: 7px;
        border-color:qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1,stop: 0.3 crimson, stop: 0.47 yellow,stop: 0.86 green);
        background:qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1,stop: 0.05 violet, stop: 0.75 lime,stop: 0.95 aquamarine);
        color: yellow;
        font: italic bold 1.9em system-ui;  
    }
    

    QPushButton:hover {
        background-image: none;
        background:qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1,stop: 0 red, stop: 0.4 gold,stop: 1 aqua);
    }
""")

mainline = QVBoxLayout()
hline = QHBoxLayout()
label = QLabel()

label1 = QLabel()
label1.hide()
label2 = QLabel()
label2.hide()
label3 = QLabel()
label3.hide()
label4 = QLabel()
label4.hide()
label5 = QLabel()
label5.hide()
label6 = QLabel()
label6.hide()
label7 = QLabel()
label7.hide()
label8 = QLabel()
label8.hide()

text = QLabel("Введіть назву держави:")
countryname = QLineEdit()
getinfo = QPushButton("Отримати всі дані про державу:")
info = QLabel("Результат: ")
translatebut = QPushButton("Відкрити перекладач.")
translator = Translator()

pixmap = QPixmap('png-transparent-europe-map-europe-white-photography-computer-wallpaper-Photoroom.png-Photoroom.png')
pixmap=pixmap.scaledToWidth(200)
label.setPixmap(pixmap)

mainline.addLayout(hline)
mainline.addWidget(translatebut)
hline.addWidget(label)
mainline.addWidget(countryname)
hline.addWidget(text)
mainline.addWidget(getinfo)
mainline.addWidget(info)
mainline.addWidget(label1)
mainline.addWidget(label2)
mainline.addWidget(label3)
mainline.addWidget(label4)
mainline.addWidget(label5)
mainline.addWidget(label6)
mainline.addWidget(label7)
mainline.addWidget(label8)

window.setLayout(mainline)

def trnwindow():
    window1 = QDialog()
    window1.resize(50, 100)
    languages = QComboBox()
    languages.addItem("Українська")
    languages.addItem("Німецька")
    languages.addItem("Італійська")
    languages.addItem("Французька")
    languages.addItem("Англійська")
    languages.addItem("Іспанська")
    languages.addItem("Португальська")
    languages.addItem("Шведська")
    languages.addItem("Фінська")
    languages.addItem("Польська")
    languages.addItem("Угорська")
    languages.addItem("Хорватська")
    languages.addItem("Грецька")
    languages.addItem("Болгарська")
    languages.addItem("Турецька")
    languages.addItem("Арабська")
    languages.addItem("Китайська")
    languages.addItem("Японська")
    def changelang():
        if languages.currentText() == "Англійська":
            share.language = "en"
        if languages.currentText() == "Французька":
            share.language = "fr"
        if languages.currentText() == "Італійська":
            share.language = "it"
        if languages.currentText() == "Німецька":
            share.language = "de"
        if languages.currentText() == "Українська":
            share.language = "uk"
        if languages.currentText() == "Іспанська":
            share.language = "es"
        if languages.currentText() == "Португальська":
            share.language = "pt"
        if languages.currentText() == "Шведська":
            share.language = "sv"
        if languages.currentText() == "Фінська":
            share.language = "fi"
        if languages.currentText() == "Польська":
            share.language = "pl"
        if languages.currentText() == "Угорська":
            share.language = "hu"
        if languages.currentText() == "Хорватська":
            share.language = "hr"
        if languages.currentText() == "Грецька":
            share.language = "el"
        if languages.currentText() == "Болгарська":
            share.language = "bg"
        if languages.currentText() == "Турецька":
            share.language = "tr"
        if languages.currentText() == "Арабська":
            share.language = "ar"
        if languages.currentText() == "Китайська":
            share.language = "zh-cn"
        if languages.currentText() == "Японська":
            share.language = "ja"

    setlanguage = QPushButton("Перекласти цією мовою.")
    setlanguage.clicked.connect(changelang)
    mainline1 = QVBoxLayout()
    mainline1.addWidget(languages)
    mainline1.addWidget(setlanguage)
    window1.setLayout(mainline1)
    window1.exec()

def source():
    url = f"https://restcountries.com/v3.1/name/{countryname.text()}"
    response = requests.get(url)
    if response.status_code == 200:
        countries = response.json()
        data = countries[0]

        b = str(data.get('borders')).replace('[', '').replace(']', '').replace("'", '')
        c = str(data.get('capital')).replace('[', '').replace(']', '').replace("'", '')
        name_text = translator.translate(f"name: {data['name']['common']}", share.language).text
        area_text = translator.translate(f"area: {data.get('area')} km per square", share.language).text
        borders_text = translator.translate(f"borders: {str(b)}", share.language).text
        capital_text = translator.translate(f"capital: {str(c)}", share.language).text
        continents_text = translator.translate(f"continents: {data.get('region')}", share.language).text
        languages_text = translator.translate(f"languages: {', '.join(data.get('languages', {}).keys())}", share.language).text
        currencies_text = translator.translate(f"currencies: {', '.join(data.get('currencies', {}).keys())}", share.language).text
        population_text = translator.translate(f"population: {data.get('population')} people", share.language).text
        info.hide()
        label1.setText(name_text)
        label1.show()
        label2.setText(area_text)
        label2.show()
        label3.setText(borders_text)
        label3.show()
        label4.setText(capital_text)
        label4.show()
        label5.setText(continents_text)
        label5.show()
        label6.setText(languages_text)
        label6.show()
        label7.setText(currencies_text)
        label7.show()
        label8.setText(population_text)
        label8.show()
    else:
        info.setText("Помилка отримання даних з сервера")

getinfo.clicked.connect(source)
translatebut.clicked.connect(trnwindow)
window.show()
app.exec()
