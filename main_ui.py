from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1920, 1000)
        MainWindow.setStyleSheet(u"background-color: rgb(25, 25, 25);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.lblOrVideo = QLabel(self.centralwidget)
        self.lblOrVideo.setObjectName(u"lblOrVideo")
        self.lblOrVideo.setGeometry(QRect(10, 70, 940, 902))
        self.lblOrVideo.setStyleSheet(u"background-color: rgb(49, 49, 49);\n"
"border-radius: 25px;")
        self.lblEditVideo = QLabel(self.centralwidget)
        self.lblEditVideo.setObjectName(u"lblEditVideo")
        self.lblEditVideo.setGeometry(QRect(970, 70, 940, 902))
        self.lblEditVideo.setStyleSheet(u"background-color: rgb(49, 49, 49);\n"
"border-radius: 25px;")
        self.btnSobel = QPushButton(self.centralwidget)
        self.btnSobel.setObjectName(u"btnSobel")
        self.btnSobel.setGeometry(QRect(100, 20, 111, 41))
        font = QFont()
        font.setFamily(u"Arial Narrow")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.btnSobel.setFont(font)
        self.btnSobel.setStyleSheet(u"background-color: rgb(0, 170, 0);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 20px;")
        self.btnLaplacian = QPushButton(self.centralwidget)
        self.btnLaplacian.setObjectName(u"btnLaplacian")
        self.btnLaplacian.setGeometry(QRect(230, 20, 111, 41))
        font1 = QFont()
        font1.setFamily(u"Arial Narrow")
        font1.setPointSize(10)
        font1.setBold(True)
        font1.setWeight(75)
        self.btnLaplacian.setFont(font1)
        self.btnLaplacian.setStyleSheet(u"background-color: rgb(0, 170, 0);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 20px;")

        self.lblSketch = QLabel(self.centralwidget)
        self.lblSketch.setObjectName(u"lblSketch")
        self.lblSketch.setGeometry(QRect(14, 5, 941, 61))
        font2 = QFont()
        font2.setBold(True)
        font2.setWeight(75)
        self.lblSketch.setFont(font2)
        self.lblSketch.setStyleSheet(u"color: rgb(203, 203, 203);\n"
"padding-left: 15px;")
        self.lblSketch.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.lblCartoon = QLabel(self.centralwidget)
        self.lblCartoon.setObjectName(u"lblCartoon")
        self.lblCartoon.setGeometry(QRect(400, 5, 941, 61))
        self.lblCartoon.setFont(font2)
        self.lblCartoon.setStyleSheet(u"color: rgb(203, 203, 203);\n"
"padding-left: 25px;\n"
"border-left: 2px solid #a1a1a1;")
        self.lblCartoon.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.lblchannelSplit = QLabel(self.centralwidget)
        self.lblchannelSplit.setObjectName(u"lblchannelSplit")
        self.lblchannelSplit.setGeometry(QRect(400, 5, 941, 61))
        self.lblchannelSplit.setFont(font2)
        self.lblchannelSplit.setStyleSheet(u"color: rgb(203, 203, 203);\n"
                                     "padding-left: 15px;")
        self.lblchannelSplit.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.btnThreshold1 = QPushButton(self.centralwidget)
        self.btnThreshold1.setObjectName(u"btnThreshold1")
        self.btnThreshold1.setGeometry(QRect(520, 20, 111, 41))
        self.btnThreshold1.setFont(font1)
        self.btnThreshold1.setStyleSheet(u"background-color: rgb(255, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 20px;")
        self.btnThreshold2 = QPushButton(self.centralwidget)
        self.btnThreshold2.setObjectName(u"btnThreshold2")
        self.btnThreshold2.setGeometry(QRect(780, 20, 111, 41))
        self.btnThreshold2.setFont(font)
        self.btnThreshold2.setStyleSheet(u"background-color: rgb(255, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 20px;")
        self.btnExit = QPushButton(self.centralwidget)
        self.btnExit.setObjectName(u"btnExit")
        self.btnExit.setGeometry(QRect(1820, 10, 81, 51))
        font3 = QFont()
        font3.setFamily(u"Arial Narrow")
        font3.setPointSize(12)
        font3.setBold(True)
        font3.setWeight(75)
        self.btnExit.setFont(font3)
        self.btnExit.setStyleSheet(u"background-color: #F2DD6C;\n"
"color: rgb(0,0,0);\n"
"border-radius: 20px;")
        self.btnOpen = QPushButton(self.centralwidget)
        self.btnOpen.setObjectName(u"btnOpen")
        self.btnOpen.setGeometry(QRect(1720, 10, 81, 51))
        self.btnOpen.setFont(font3)
        self.btnOpen.setStyleSheet(u"background-color: #F2DD6C;\n"
"color: rgb(0,0,0);\n"
"border-radius: 20px;")
        self.btnstylization = QPushButton(self.centralwidget)
        self.btnstylization.setObjectName(u"btnstylization")
        self.btnstylization.setGeometry(QRect(650, 20, 111, 41))
        self.btnstylization.setFont(font)
        self.btnstylization.setStyleSheet(u"background-color: rgb(255, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 20px;")

        self.btnred = QPushButton(self.centralwidget)
        self.btnred.setObjectName(u"btnred")
        self.btnred.setGeometry(QRect(1200, 20, 130, 41))
        self.btnred.setFont(font)
        self.btnred.setStyleSheet(u"background-color: rgb(0, 0, 255);\n"
                                        "color: rgb(255, 255, 255);\n"
                                        "border-radius: 20px;")

        self.btnGreen = QPushButton(self.centralwidget)
        self.btnGreen.setObjectName(u"btnGreen")
        self.btnGreen.setGeometry(QRect(1340, 20, 130, 41))
        self.btnGreen.setFont(font)
        self.btnGreen.setStyleSheet(u"background-color: rgb(0, 0, 255);\n"
                                        "color: rgb(255, 255, 255);\n"
                                        "border-radius: 20px;")


        self.btnblue = QPushButton(self.centralwidget)
        self.btnblue.setObjectName(u"btnblue")
        self.btnblue.setGeometry(QRect(1480, 20, 130, 41))
        self.btnblue.setFont(font)
        self.btnblue.setStyleSheet(u"background-color: rgb(0, 0, 255);\n"
                                        "color: rgb(255, 255, 255);\n"
                                        "border-radius: 20px;")

        MainWindow.setCentralWidget(self.centralwidget)
        self.lblchannelSplit.raise_()
        self.lblSketch.raise_()
        self.lblOrVideo.raise_()
        self.lblEditVideo.raise_()
        self.btnSobel.raise_()
        self.btnLaplacian.raise_()
        self.lblCartoon.raise_()
        self.btnThreshold1.raise_()
        self.btnThreshold2.raise_()
        self.btnExit.raise_()
        self.btnOpen.raise_()
        self.btnstylization.raise_()
        self.btnred.raise_()
        self.btnGreen.raise_()
        self.btnblue.raise_()
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1920, 26))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Application of Video Processing", None))
        self.lblOrVideo.setText("")
        self.lblEditVideo.setText("")
        self.btnSobel.setText(QCoreApplication.translate("MainWindow", u"Sobel", None))
        self.btnLaplacian.setText(QCoreApplication.translate("MainWindow", u"Laplacian", None))
        self.lblchannelSplit.setText(QCoreApplication.translate("MainWindow", u"CHANNEL SPLIT", None))
        self.lblSketch.setText(QCoreApplication.translate("MainWindow", u"SKETCH", None))
        self.lblCartoon.setText(QCoreApplication.translate("MainWindow", u"CARTOON", None))
        self.btnThreshold1.setText(QCoreApplication.translate("MainWindow", u"Threshold 1", None))
        self.btnThreshold2.setText(QCoreApplication.translate("MainWindow", u"Stylization", None))
        self.btnExit.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.btnOpen.setText(QCoreApplication.translate("MainWindow", u"Open", None))
        self.btnstylization.setText(QCoreApplication.translate("MainWindow", u"Threshold 2", None))
        self.btnblue.setText(QCoreApplication.translate("MainWindow", u"Blue Channel", None))
        self.btnGreen.setText(QCoreApplication.translate("MainWindow", u"Green Channel", None))
        self.btnred.setText(QCoreApplication.translate("MainWindow", u"Red Channel", None))
    # retranslateUi

