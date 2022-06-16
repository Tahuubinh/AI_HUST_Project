import sys
from PyQt5.QtWidgets import QWidget, QApplication

class NumberPuzzle(QWidget):
    """ N-puzzle game class """
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        # Set game container frame width and height.
        self.setFixedSize(400, 400)
        # Set game window title.
        self.setWindowTitle('N-Puzzle Game')
        # Set the background color.
        self.setStyleSheet("background-color:gray;")
        self.show()
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = NumberPuzzle()
    sys.exit(app.exec_())