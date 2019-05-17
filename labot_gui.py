# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem, QListWidget
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
from selenium.webdriver.firefox.options import Options
import time

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(513, 610)
        Dialog.setStyleSheet("")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(90, 60, 331, 31))
        self.lineEdit.setStyleSheet("font: 15pt Arial;margin: 1px; border-color: #0c457e; border-style: outset; border-radius: 2px;border-width: 1px;color: white;background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #2198c0, stop: 1 #0d5ca6);}QPushButton:pressed { background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #0d5ca6, stop: 1 #2198c0);")
        self.lineEdit.setObjectName("lineEdit")
        self.label_titulo = QtWidgets.QLabel(Dialog)
        self.label_titulo.setGeometry(QtCore.QRect(120, 20, 271, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_titulo.setFont(font)
        self.label_titulo.setStyleSheet("")
        self.label_titulo.setObjectName("label_titulo")
        self.btn_buscar = QtWidgets.QPushButton(Dialog)
        self.btn_buscar.setGeometry(QtCore.QRect(200, 110, 111, 41))
        self.btn_buscar.setStyleSheet("font: 15pt Arial;margin: 1px; border-color: #0c457e; border-style: outset; border-radius: 8px;border-width: 1px;color: white;background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #2198c0, stop: 1 #0d5ca6);}QPushButton:pressed { background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #0d5ca6, stop: 1 #2198c0);")
        self.btn_buscar.setObjectName("btn_buscar")
        self.tableView = QtWidgets.QTableWidget(Dialog)
        self.tableView.setGeometry(QtCore.QRect(60, 210, 401, 271))
        self.tableView.setObjectName("tableView")
        self.btn_selecionar = QtWidgets.QPushButton(Dialog)
        self.btn_selecionar.setGeometry(QtCore.QRect(170, 500, 161, 41))
        self.btn_selecionar.setStyleSheet("font: 15pt Arial;margin: 1px; border-color: #0c457e; border-style: outset; border-radius: 8px;border-width: 1px;color: white;background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #2198c0, stop: 1 #0d5ca6);}QPushButton:pressed { background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #0d5ca6, stop: 1 #2198c0);")
        self.btn_selecionar.setObjectName("btn_selecionar")
        self.label_titulo_2 = QtWidgets.QLabel(Dialog)
        self.label_titulo_2.setGeometry(QtCore.QRect(90, 170, 341, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_titulo_2.setFont(font)
        self.label_titulo_2.setStyleSheet("")
        self.label_titulo_2.setObjectName("label_titulo_2")
        self.label_titulo_3 = QtWidgets.QLabel(Dialog)
        self.label_titulo_3.setGeometry(QtCore.QRect(100, 560, 341, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_titulo_3.setFont(font)
        self.label_titulo_3.setStyleSheet("")
        self.label_titulo_3.setObjectName("label_titulo_3")

        self.tableView.setRowCount(10)
        self.tableView.setAlternatingRowColors(True)
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    #---------------------- CONECTA SIGNALS -------------------------------
        self.btn_buscar.clicked.connect(self.busca_videos)

    #-----------------------------------------------------------------------------------



    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Laboratório da Júlia"))
        self.label_titulo.setText(_translate("Dialog", "Digite o título do vídeo"))
        self.btn_buscar.setText(_translate("Dialog", "BUSCAR"))
        self.btn_selecionar.setText(_translate("Dialog", "SELECIONAR"))
        self.label_titulo_2.setText(_translate("Dialog", "Escolha um resultado abaixo"))
        self.label_titulo_3.setText(_translate("Dialog", "Vídeo adicionado ao bot!"))


    #-----------------------------------------------------------------------------------


    def busca_videos(self):

        titulo = self.lineEdit.text()
        print(titulo)

        if titulo != '':

            options = Options()
            options.headless = True
            driver = webdriver.Firefox(options=options)  # seu path do driver
            driver.get('https://www.youtube.com/')
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID,"search")))
            driver.find_element_by_name('search_query').send_keys(titulo)
            driver.find_element_by_name('search_query').submit()
            time.sleep(2)
            url_atual = driver.current_url

            req = Request(url_atual, headers={'User-Agent': 'Mozilla/5.0'})
            page = urlopen(req).read()
            soup = BeautifulSoup(page, 'html.parser')
            soup.prettify()

            lista = []

            for link in soup.find_all('a'):
                if link.get('title') != None:
                    lista.append(link.get('title'))
            del lista[:41]


            print(lista)




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

