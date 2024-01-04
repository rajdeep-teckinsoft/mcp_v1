from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton
import sys


def click_method():
    print("Button clicked")


app = QApplication([])
win = QMainWindow()
win.setWindowTitle("Test")
win.resize(1920, 720)
win.move(0, 0)

label = QLabel("This is a text", win)
label.move(20, 0)

button = QPushButton("Click here", win)
button.move(20, 40)
button.clicked.connect(click_method)

win.show()

sys.exit(app.exec_())
