from PyQt5 import QtWidgets

from design import design
from Pet import Pet

class CreatePet(QtWidgets.QMainWindow, design.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.newPet = Pet()
        
        self.buttonSave.clicked.connect(self.save_pet)

    def save_pet(self):
        self.create_new_pet()
        self.newPet.save_to_file()

    def create_new_pet(self):
        self.newPet.name = self.lineEdit.text()
        self.newPet.age = self.spinBox.value()
        self.newPet.type = self.comboBox.currentText()