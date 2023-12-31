# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from gameboard import GameBoard

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Pacman")
        Form.resize(600, 600)
        self.gameBoard = GameBoard(Form)
        self.gameBoard.setColumnCount(3)
        self.gameBoard.setRowCount(3)
        self.gameBoard.resize(600,600)
        self.gameBoard.setColumnWidth(0,199)
        self.gameBoard.setColumnWidth(1,199)
        self.gameBoard.setColumnWidth(2,199)
        self.gameBoard.setRowHeight(0,199)
        self.gameBoard.setRowHeight(1,199)
        self.gameBoard.setRowHeight(2,199)
        self.gameBoard.setStyleSheet('font: 100px;')
        self.gameBoard.horizontalHeader().close()
        self.gameBoard.verticalHeader().close()
        self.gameBoard.setItem(0,0,QtWidgets.QTableWidgetItem(''))
        self.gameBoard.setItem(0,1,QtWidgets.QTableWidgetItem(''))
        self.gameBoard.setItem(0,2,QtWidgets.QTableWidgetItem(''))
        self.gameBoard.setItem(1,0,QtWidgets.QTableWidgetItem(''))
        self.gameBoard.setItem(1,1,QtWidgets.QTableWidgetItem(''))
        self.gameBoard.setItem(1,2,QtWidgets.QTableWidgetItem(''))
        self.gameBoard.setItem(2,0,QtWidgets.QTableWidgetItem(''))
        self.gameBoard.setItem(2,1,QtWidgets.QTableWidgetItem(''))
        self.gameBoard.setItem(2,2,QtWidgets.QTableWidgetItem(''))
        self.gameBoard.item(0,0).setTextAlignment(QtCore.Qt.Alignment(QtCore.Qt.AlignmentFlag.AlignCenter))
        self.gameBoard.item(0,1).setTextAlignment(QtCore.Qt.Alignment(QtCore.Qt.AlignmentFlag.AlignCenter))
        self.gameBoard.item(0,2).setTextAlignment(QtCore.Qt.Alignment(QtCore.Qt.AlignmentFlag.AlignCenter))
        self.gameBoard.item(1,0).setTextAlignment(QtCore.Qt.Alignment(QtCore.Qt.AlignmentFlag.AlignCenter))
        self.gameBoard.item(1,1).setTextAlignment(QtCore.Qt.Alignment(QtCore.Qt.AlignmentFlag.AlignCenter))
        self.gameBoard.item(1,2).setTextAlignment(QtCore.Qt.Alignment(QtCore.Qt.AlignmentFlag.AlignCenter))
        self.gameBoard.item(2,0).setTextAlignment(QtCore.Qt.Alignment(QtCore.Qt.AlignmentFlag.AlignCenter))
        self.gameBoard.item(2,1).setTextAlignment(QtCore.Qt.Alignment(QtCore.Qt.AlignmentFlag.AlignCenter))
        self.gameBoard.item(2,2).setTextAlignment(QtCore.Qt.Alignment(QtCore.Qt.AlignmentFlag.AlignCenter))
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))

