from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton
from ethercat import *
import sys


def click_method():
    print("Device id is: ")
    dev_id = find_device_id()
    print(dev_id)
    return


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

init_spi()

win.show()

sys.exit(app.exec_())
