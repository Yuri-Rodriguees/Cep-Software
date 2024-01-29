# -*- coding: utf-8 -*-

"""Developer Yuri Rodrigues"""

from PyQt5 import QtCore, QtGui, QtWidgets
import requests
import json

class Ui_MainWindow(object):

    def consult(self):

        # Pegando campo digitado
        cep_consult = self.cep_input.text()

        # URL API
        cep_url = f'https://viacep.com.br/ws/{cep_consult}/json/'
        requisicao = requests.get(cep_url)
        dic = requisicao.json()

        # Imprimindo pesquisa
        cep = self.caixa_info.append(str('CEP Consultado: {}\n'.format(dic['cep'])))
        end = self.caixa_info.append(str('Endereço: {}\n'.format(dic['logradouro'])))
        comple = self.caixa_info.append(str('Complemento: {}\n'.format(dic['complemento'])))
        bairro = self.caixa_info.append(str('Bairro: {}\n'.format(dic['bairro'])))
        estado = self.caixa_info.append(str('Estado: {}\n'.format(dic['localidade'])))
        uf = self.caixa_info.append(str('UF: {}\n'.format(dic['uf'])))
        dd = self.caixa_info.append(str('DD: {}\n'.format(dic['ddd'])))
        linha = self.caixa_info.append('------------------------------------------------------------------')

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(318, 542)
        MainWindow.setMinimumSize(QtCore.QSize(318, 542))
        MainWindow.setMaximumSize(QtCore.QSize(318, 542))
        MainWindow.setSizeIncrement(QtCore.QSize(318, 542))
        MainWindow.setStyleSheet("background: rgb(143, 143, 143)")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.botao = QtWidgets.QPushButton(self.centralwidget)
        self.botao.setGeometry(QtCore.QRect(100, 110, 121, 51))
        self.botao.setStyleSheet("QPushButton{\n"
"color: rgb(255, 255, 255);\n"
"border-style: solid;\n"
"background: rgb(84, 84, 84);\n"
"border-radius: 22px;\n"
"padding: 15px;\n"
"}\n"
"QPushButton:hover {\n"
"    border: 2px solid rgb(0, 85, 255);\n"
"}\n"
"QPushButton:focus {\n"
"    border: 2px solid rgb(0, 255, 0);    \n"
"    color: rgb(200, 200, 200);\n"
"}")
        self.botao.setObjectName("botao")
        self.cep_input = QtWidgets.QLineEdit(self.centralwidget)
        self.cep_input.setGeometry(QtCore.QRect(10, 50, 301, 51))
        self.cep_input.setStyleSheet("QLineEdit {\n"
"    border: 2px solid rgb(74, 74, 111);\n"
"    border-radius: 5px;\n"
"    padding: 15px;\n"
"    background-color: rgb(30, 30, 30);    \n"
"    color: rgb(100, 100, 100);\n"
"}\n"
"QLineEdit:hover {\n"
"    border: 2px solid rgb(0, 85, 255);\n"
"}\n"
"QLineEdit:focus {\n"
"    border: 2px solid rgb(250, 252, 95);    \n"
"    color: rgb(200, 200, 200);\n"
"}")
        self.cep_input.setMaxLength(9)
        self.cep_input.setObjectName("cep_input")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(140, 20, 41, 20))
        self.label.setStyleSheet("font: 14pt \"Lucida Fax\";\n"
"color: rgb(39, 39, 39);")
        self.label.setObjectName("label")
        self.caixa_info = QtWidgets.QTextEdit(self.centralwidget)
        self.caixa_info.setGeometry(QtCore.QRect(3, 170, 311, 371))
        self.caixa_info.setObjectName("caixa_info")
        MainWindow.setCentralWidget(self.centralwidget)
        
        self.botao.clicked.connect(self.consult)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Consult CEP - CDAW"))
        self.botao.setText(_translate("MainWindow", "Consultar"))
        self.label.setText(_translate("MainWindow", "CEP"))
        self.caixa_info.setPlaceholderText(_translate("MainWindow", "Informações:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
