import json

from PyQt5 import QtWidgets

from Pet import *
from design import CreatePetForm
from ViewPet import *

class CreatePet(QtWidgets.QMainWindow, CreatePetForm.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.newPet = Pet()
        
        self.buttonSave.clicked.connect(self.save_pet_to_file)
        self.buttonView.clicked.connect(self.view_pet)

    def save_pet_to_file(self):
        self.create_new_pet()
        self.newPet.process_pet_data(1)
        self.file = open(self.newPet.path_to_file, "w+")
        json.dump(self.newPet.data, self.file, ensure_ascii=False)
        self.file.close()

    def create_new_pet(self):
        self.newPet.name = self.lineEdit.text()
        self.newPet.age = self.spinBox.value()
        self.newPet.type = self.comboBox.currentText()

    def view_pet(self):
        self.another_window = ViewPet()
        self.another_window.show()