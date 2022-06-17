from PyQt5.QtWidgets import QLabel
from PyQt5.QtGui import QFont, QPalette
from PyQt5.QtCore import Qt

class Block(QLabel):
    """ Number block """
    def __init__(self, number, fixed_size):
        super().__init__()
        self.number = number
        self.fixed_size = fixed_size
        self.setFixedSize(self.fixed_size, self.fixed_size)
        # Set text font.
        font = QFont()
        font.setPointSize(30)
        font.setBold(True)
        self.setFont(font)
        # Set text color.
        pa = QPalette()
        pa.setColor(QPalette.WindowText, Qt.white)
        self.setPalette(pa)
        # Set text alignment.
        self.setAlignment(Qt.AlignCenter)
        # Set background color, filleted corner and text content。
        if self.number == 0:
            self.setStyleSheet("background-color:white;border-radius:10px;")
        else:
            self.setStyleSheet("background-color:red;border-radius:10px;")
            self.setText(str(self.number)) 
