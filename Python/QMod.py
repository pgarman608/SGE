# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'QMod.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from Videojuegos import Videojuegos

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        self.videojuegos = Videojuegos()
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        Dialog.setMinimumSize(QtCore.QSize(400, 300))
        Dialog.setMaximumSize(QtCore.QSize(400, 300))
        Dialog.setBaseSize(QtCore.QSize(400, 300))
        self.btnSalir = QtWidgets.QDialogButtonBox(Dialog)
        self.btnSalir.setGeometry(QtCore.QRect(310, 260, 81, 32))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btnSalir.setFont(font)
        self.btnSalir.setOrientation(QtCore.Qt.Horizontal)
        self.btnSalir.setStandardButtons(QtWidgets.QDialogButtonBox.Ok)
        self.btnSalir.setObjectName("btnSalir")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(10, 30, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(10, 70, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(10, 110, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.leCodigo = QtWidgets.QLineEdit(Dialog)
        self.leCodigo.setGeometry(QtCore.QRect(80, 30, 113, 20))
        self.leCodigo.setObjectName("leCodigo")
        self.btnBuscar = QtWidgets.QPushButton(Dialog)
        self.btnBuscar.setGeometry(QtCore.QRect(220, 30, 75, 23))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.btnBuscar.setFont(font)
        self.btnBuscar.setObjectName("btnBuscar")
        self.leNombre = QtWidgets.QLineEdit(Dialog)
        self.leNombre.setEnabled(False)
        self.leNombre.setGeometry(QtCore.QRect(80, 70, 113, 20))
        self.leNombre.setObjectName("leNombre")
        self.leGenero = QtWidgets.QLineEdit(Dialog)
        self.leGenero.setEnabled(False)
        self.leGenero.setGeometry(QtCore.QRect(80, 110, 113, 20))
        self.leGenero.setObjectName("leGenero")
        self.btnModificar = QtWidgets.QPushButton(Dialog)
        self.btnModificar.setEnabled(False)
        self.btnModificar.setGeometry(QtCore.QRect(100, 150, 75, 23))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.btnModificar.setFont(font)
        self.btnModificar.setObjectName("btnModificar")

        self.retranslateUi(Dialog)
        self.btnSalir.accepted.connect(Dialog.accept) # type: ignore
        self.btnSalir.rejected.connect(Dialog.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        self.btnBuscar.clicked.connect(self.buscarVideojuego)
        self.btnModificar.clicked.connect(self.modificarVideojuego)
        self.btnSalir.clicked.connect(self.videojuegos.exportarVideojuegos)
    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Modificar Videojuego"))
        self.label.setText(_translate("Dialog", "Codigo"))
        self.label_2.setText(_translate("Dialog", "Nombre"))
        self.label_3.setText(_translate("Dialog", "Genero"))
        self.btnBuscar.setText(_translate("Dialog", "Buscar"))
        self.btnModificar.setText(_translate("Dialog", "Modificar"))

    def buscarVideojuego(self):
        dialog = QtWidgets.QDialog()
        codigo = self.leCodigo.text()
        if codigo != "":
            if not(self.videojuegos.comprobarCodigo(codigo)):
                self.leCodigo.setEnabled(False)
                self.btnBuscar.setEnabled(False)
                self.leGenero.setEnabled(True)
                self.leNombre.setEnabled(True)
                self.btnModificar.setEnabled(True)
                nombre,Genero = self.videojuegos.buscarVideojuego(codigo)
                self.leGenero.setText(Genero)
                self.leNombre.setText(nombre)
            else:
                QtWidgets.QMessageBox.question(dialog, 'Error', 'No existe ningun videojuego con es codigo',
                    QtWidgets.QMessageBox.Yes)
        else:
            QtWidgets.QMessageBox.question(dialog, 'Error', 'No puede haber campos vacios',
                    QtWidgets.QMessageBox.Yes)
    
    def modificarVideojuego(self):
        if self.leGenero.text() != "" or  self.leNombre.text() != "":
            self.videojuegos.modificarVideojuego(self.leCodigo.text(),self.leNombre.text(),self.leGenero.text())
            QtWidgets.QMessageBox.question(dialog, '', 'Videojuego Modificado',
                    QtWidgets.QMessageBox.Yes)
        else:
            QtWidgets.QMessageBox.question(dialog, 'Error', 'No puede haber campos vacios',
                    QtWidgets.QMessageBox.Yes)