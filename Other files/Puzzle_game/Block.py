from PyQt5.QtWidgets import QWidget

class Block(QLabel):
    """ Number block """
    def __init__(self, number):
        super().__init__()
        self.number = number
        self.setFixedSize(80, 80)
        # Set the number font.
        font = QFont()
        font.setPointSize(30)
        font.setBold(True)
        self.setFont(font)
        # Set text color.
        pa = QPalette()
        pa.setColor(QPalette.WindowText, Qt.white)
        self.setPalette(pa)
        # Set the text alignment.
        self.setAlignment(Qt.AlignCenter)
        # Set background color, filleted corner and text content.
        if self.number == 0:
            self.setStyleSheet("background-color:white;border-radius:10px;")
        else:
            self.setStyleSheet("background-color:red;border-radius:10px;")
            self.setText(str(self.number))