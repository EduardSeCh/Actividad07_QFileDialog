# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainWindow.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(408, 382)
        self.actionGuardar_archivo = QAction(MainWindow)
        self.actionGuardar_archivo.setObjectName(u"actionGuardar_archivo")
        self.actionAbrir_archivo = QAction(MainWindow)
        self.actionAbrir_archivo.setObjectName(u"actionAbrir_archivo")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(9, 9, 180, 320))
        self.gridLayout = QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(u"gridLayout")
        self.sbRed = QSpinBox(self.groupBox)
        self.sbRed.setObjectName(u"sbRed")

        self.gridLayout.addWidget(self.sbRed, 6, 1, 1, 1)

        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 4, 0, 1, 1)

        self.label_8 = QLabel(self.groupBox)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout.addWidget(self.label_8, 1, 0, 1, 1)

        self.leDestinoY = QLineEdit(self.groupBox)
        self.leDestinoY.setObjectName(u"leDestinoY")

        self.gridLayout.addWidget(self.leDestinoY, 4, 1, 1, 1)

        self.pbAgregarInicio = QPushButton(self.groupBox)
        self.pbAgregarInicio.setObjectName(u"pbAgregarInicio")

        self.gridLayout.addWidget(self.pbAgregarInicio, 9, 0, 1, 2)

        self.pbMostrar = QPushButton(self.groupBox)
        self.pbMostrar.setObjectName(u"pbMostrar")

        self.gridLayout.addWidget(self.pbMostrar, 11, 0, 1, 2)

        self.sbGreen = QSpinBox(self.groupBox)
        self.sbGreen.setObjectName(u"sbGreen")

        self.gridLayout.addWidget(self.sbGreen, 7, 1, 1, 1)

        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 6, 0, 1, 1)

        self.pbAgregaFinal = QPushButton(self.groupBox)
        self.pbAgregaFinal.setObjectName(u"pbAgregaFinal")

        self.gridLayout.addWidget(self.pbAgregaFinal, 10, 0, 1, 2)

        self.leDestinoX = QLineEdit(self.groupBox)
        self.leDestinoX.setObjectName(u"leDestinoX")

        self.gridLayout.addWidget(self.leDestinoX, 3, 1, 1, 1)

        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 5, 0, 1, 1)

        self.label_5 = QLabel(self.groupBox)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 7, 0, 1, 1)

        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 3, 0, 1, 1)

        self.sbBlue = QSpinBox(self.groupBox)
        self.sbBlue.setObjectName(u"sbBlue")

        self.gridLayout.addWidget(self.sbBlue, 8, 1, 1, 1)

        self.label_7 = QLabel(self.groupBox)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout.addWidget(self.label_7, 2, 0, 1, 1)

        self.leOrigenx = QLineEdit(self.groupBox)
        self.leOrigenx.setObjectName(u"leOrigenx")

        self.gridLayout.addWidget(self.leOrigenx, 1, 1, 1, 1)

        self.leOrigenY = QLineEdit(self.groupBox)
        self.leOrigenY.setObjectName(u"leOrigenY")

        self.gridLayout.addWidget(self.leOrigenY, 2, 1, 1, 1)

        self.leVelocidad = QLineEdit(self.groupBox)
        self.leVelocidad.setObjectName(u"leVelocidad")

        self.gridLayout.addWidget(self.leVelocidad, 5, 1, 1, 1)

        self.label_6 = QLabel(self.groupBox)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout.addWidget(self.label_6, 8, 0, 1, 1)

        self.label_9 = QLabel(self.groupBox)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout.addWidget(self.label_9, 0, 0, 1, 1)

        self.leId = QLineEdit(self.groupBox)
        self.leId.setObjectName(u"leId")

        self.gridLayout.addWidget(self.leId, 0, 1, 1, 1)

        self.salida = QPlainTextEdit(self.centralwidget)
        self.salida.setObjectName(u"salida")
        self.salida.setGeometry(QRect(195, 9, 201, 320))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 408, 22))
        self.menuArchivo = QMenu(self.menubar)
        self.menuArchivo.setObjectName(u"menuArchivo")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuArchivo.menuAction())
        self.menuArchivo.addAction(self.actionGuardar_archivo)
        self.menuArchivo.addAction(self.actionAbrir_archivo)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionGuardar_archivo.setText(QCoreApplication.translate("MainWindow", u"Guardar archivo", None))
#if QT_CONFIG(shortcut)
        self.actionGuardar_archivo.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+O", None))
#endif // QT_CONFIG(shortcut)
        self.actionAbrir_archivo.setText(QCoreApplication.translate("MainWindow", u"Abrir archivo", None))
#if QT_CONFIG(shortcut)
        self.actionAbrir_archivo.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+S", None))
#endif // QT_CONFIG(shortcut)
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Particula", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Destino y", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"origen x", None))
        self.pbAgregarInicio.setText(QCoreApplication.translate("MainWindow", u"Agregar Inicio", None))
        self.pbMostrar.setText(QCoreApplication.translate("MainWindow", u"Mostrar", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Red", None))
        self.pbAgregaFinal.setText(QCoreApplication.translate("MainWindow", u"Agregar Final", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Velocidad", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Green", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Destino x", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"origen y", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Blue", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Id", None))
        self.menuArchivo.setTitle(QCoreApplication.translate("MainWindow", u"Archivo", None))
    # retranslateUi

