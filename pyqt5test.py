import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QApplication, QVBoxLayout, QLCDNumber, QSlider


class Principale(QWidget):
    def __init__(self):
        super().__init__()
        self.setUI()

    def setUI(self):
        lcd = QLCDNumber(self)
        slider = QSlider(Qt.Horizontal, self)

        miseEnPage = QVBoxLayout()
        miseEnPage.addWidget(slider)
        miseEnPage.addWidget(lcd)
        self.setLayout(miseEnPage)

        slider.valueChanged.connect(lcd.display)

        self.setGeometry(300, 300, 200, 100)
        self.setWindowTitle('Fenêtre principale')

        self.show()


monApp = QApplication(sys.argv)
fenetre = Principale()
sys.exit(monApp.exec_())