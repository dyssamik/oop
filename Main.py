from PyQt5 import QtWidgets
import sys

from CreatePet import *

def main():
    app = QtWidgets.QApplication(sys.argv)
    window = CreatePet()
    window.show()
    app.exec_()

if __name__ == "__main__":
    main()