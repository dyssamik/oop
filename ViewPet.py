import json

from PyQt5 import QtWidgets
from PyQt5 import QtGui
from PyQt5 import QtCore

from Pet import *
from design import ViewPetForm

class ViewPet(QtWidgets.QWidget, ViewPetForm.Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.existingPet = Pet()

        self.pushButton.clicked.connect(self.open_pet_file)
        self.pushButton_2.clicked.connect(self.close)

    def open_pet_file(self):
        self.filename = QtWidgets.QFileDialog.getOpenFileName(self)
        self.file = open(self.filename[0], "r")
        self.data = self.file.read()
        self.dictData = json.loads(self.data)
        self.existingPet.process_pet_data(0, self.dictData)
        self.label.setText(self.existingPet.name)
        self.labelAge.setText(str(self.existingPet.age))
        self.labelType.setText(self.existingPet.type)
        if self.existingPet.type == "Кот/Кошка":
            self.pixmap = QtGui.QPixmap("./images/cat.png")
        elif self.existingPet.type == "Пёс/Собака":
            self.pixmap = QtGui.QPixmap("./images/dog.png")
        else:
            pass
        self.pixmap_scaled = self.pixmap.scaled(192, 192, QtCore.Qt.KeepAspectRatio)
        self.label_2.setPixmap(self.pixmap_scaled)
            