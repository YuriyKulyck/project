from PyQt5.QtWidgets import *
import main

app = QApplication([])
window = QWidget()

mainline = QVBoxLayout()
hline = QHBoxLayout()

text = QLabel("Введіть назву держави:")
countryname = QLineEdit()
getinfo = QPushButton("Отримати всі дані про державу:")
info = QLabel()

mainline.addLayout(hline)
mainline.addWidget(text)
hline.addWidget(countryname)
mainline.addWidget(getinfo)
mainline.addWidget(info)

window.setLayout(mainline)

window.show()
app.exec()