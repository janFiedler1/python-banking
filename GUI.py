from PyQt5.QtWidgets import *
from PyQt5 import QtGui

class GUI():
    def __init__(self):
        app = QApplication([])
        window = QWidget()
        window.setWindowTitle('Python Banking')
        window.setWindowIcon(QtGui.QIcon('images/snake_money.png'))
        window.resize(400,200)
        layout = QVBoxLayout()
        layout.addWidget(QPushButton('Top'))
        layout.addWidget(QPushButton('Bottom'))
        window.setLayout(layout)
        window.show()
        app.exec()


