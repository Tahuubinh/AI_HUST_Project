import sys
import random
from enum import IntEnum
from PyQt5.QtWidgets import QLabel, QWidget, QApplication, QGridLayout, QMessageBox
from PyQt5.QtGui import QFont, QPalette
from PyQt5.QtCore import Qt
# Using enumeration class to represent direction.
class Direction(IntEnum):
    UP = 1
    DOWN = 0
    LEFT = 3
    RIGHT = 2
class NumberNPuzzle(QWidget):
    """ N-puzzle main program """
    def __init__(self):
        super().__init__()
        self.blocks = []
        self.zero_row = 0
        self.zero_column = 0
        self.num_row = 4
        self.gltMain = QGridLayout()
        self.initUI()
    def initUI(self):      
        # Set number block spacing
        self.gltMain.setSpacing(20)
        self.onInit()
        # Set layout.
        self.setLayout(self.gltMain)
        # Set window width and height.
        self.setFixedSize(400, 400)
        # Set window title.
        self.setWindowTitle('N-puzzle Game.')
        # Set window background color.
        self.setStyleSheet("background-color:gray;")
        self.show()
    # Initialize layout.
    def onInit(self):
        # Create sequential array.
        self.numbers = list(range(1, self.num_row * self.num_row))
        self.numbers.append(0)
        # Add number to the two-dimensional array.
        for row in range(self.num_row):
            self.blocks.append([])
            for column in range(self.num_row):
                temp = self.numbers[row * self.num_row + column]
                if temp == 0:
                    self.zero_row = row
                    self.zero_column = column
                self.blocks[row].append(temp)
        # Scrambling the array.
        for i in range(500):
            random_num = random.randint(0, 3)
            self.move(Direction(random_num))
        self.updatePanel()
    # Detect key press event.
    def keyPressEvent(self, event):
        key = event.key()
        if(key == Qt.Key_Up or key == Qt.Key_W):
            self.move(Direction.DOWN)
        if(key == Qt.Key_Down or key == Qt.Key_S):
            self.move(Direction.UP)
        if(key == Qt.Key_Left or key == Qt.Key_A):
            self.move(Direction.RIGHT)
        if(key == Qt.Key_Right or key == Qt.Key_D):
            self.move(Direction.LEFT)
        self.updatePanel()
        if self.checkResult():
            if QMessageBox.Ok == QMessageBox.information(self, 'Challenge Results', 'Congratulations on completing the challenge!'):
                self.onInit()
    # Block moving algorithm.
    def move(self, direction):
        if(direction == Direction.UP): # Move up.
            if self.zero_row != self.num_row - 1:
                self.blocks[self.zero_row][self.zero_column] = self.blocks[self.zero_row + 1][self.zero_column]
                self.blocks[self.zero_row + 1][self.zero_column] = 0
                self.zero_row += 1
        if(direction == Direction.DOWN): # Move down.
            if self.zero_row != 0:
                self.blocks[self.zero_row][self.zero_column] = self.blocks[self.zero_row - 1][self.zero_column]
                self.blocks[self.zero_row - 1][self.zero_column] = 0
                self.zero_row -= 1
        if(direction == Direction.LEFT): # Move left.
            if self.zero_column != self.num_row - 1:
                self.blocks[self.zero_row][self.zero_column] = self.blocks[self.zero_row][self.zero_column + 1]
                self.blocks[self.zero_row][self.zero_column + 1] = 0
                self.zero_column += 1
        if(direction == Direction.RIGHT): # Move right.
            if self.zero_column != 0:
                self.blocks[self.zero_row][self.zero_column] = self.blocks[self.zero_row][self.zero_column - 1]
                self.blocks[self.zero_row][self.zero_column - 1] = 0
                self.zero_column -= 1
    def updatePanel(self):
        for row in range(self.num_row):
            for column in range(self.num_row):
                self.gltMain.addWidget(Block(self.blocks[row][column]), row, column)
        self.setLayout(self.gltMain)
    # Check whether the challenge is completed or not.
    def checkResult(self):
        # First check whether the block value in the bottom right corner is 0。
        if self.blocks[self.num_row - 1][self.num_row - 1] != 0:
            return False
        for row in range(self.num_row):
            for column in range(self.num_row):
                # The value of the block in the bottom right corner is 0, pass.
                if row == self.num_row - 1 and column == self.num_row - 1:
                    pass
                # Check whether the square block number is correct number.
                elif self.blocks[row][column] != row * self.num_row + column + 1:
                    return False
        return True
class Block(QLabel):
    """ Number block """
    def __init__(self, number):
        super().__init__()
        self.number = number
        self.setFixedSize(80, 80)
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
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = NumberNPuzzle()
    sys.exit(app.exec_())