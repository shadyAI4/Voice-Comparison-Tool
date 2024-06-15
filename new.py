# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'new.ui'
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
        MainWindow.resize(1084, 674)
        MainWindow.setMinimumSize(QSize(1000, 500))
        MainWindow.setStyleSheet(u"background-color:#14213d;")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.frame_top = QFrame(self.centralwidget)
        self.frame_top.setObjectName(u"frame_top")
        self.frame_top.setFrameShape(QFrame.StyledPanel)
        self.frame_top.setFrameShadow(QFrame.Raised)

        self.gridLayout.addWidget(self.frame_top, 4, 0, 1, 1)

        self.progressBar = QProgressBar(self.centralwidget)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.progressBar.setValue(0)

        self.gridLayout.addWidget(self.progressBar, 2, 0, 1, 1)

        self.Content = QFrame(self.centralwidget)
        self.Content.setObjectName(u"Content")
        self.Content.setFrameShape(QFrame.NoFrame)
        self.Content.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.Content)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_left_menu = QFrame(self.Content)
        self.frame_left_menu.setObjectName(u"frame_left_menu")
        self.frame_left_menu.setMinimumSize(QSize(200, 0))
        self.frame_left_menu.setMaximumSize(QSize(70, 16777215))
        self.frame_left_menu.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);")
        self.frame_left_menu.setFrameShape(QFrame.StyledPanel)
        self.frame_left_menu.setFrameShadow(QFrame.Raised)
        self.label_7 = QLabel(self.frame_left_menu)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(0, 0, 201, 201))
        self.label_7.setStyleSheet(u"background-color: rgb(26, 95, 180);")
        self.label_7.setPixmap(QPixmap(u"./images/new_logo.png"))
        self.label_7.setScaledContents(True)
        self.layoutWidget = QWidget(self.frame_left_menu)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 210, 181, 251))
        self.verticalLayout = QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.pushButton_37 = QPushButton(self.layoutWidget)
        self.pushButton_37.setObjectName(u"pushButton_37")
        self.pushButton_37.setStyleSheet(u"background-color: rgb(99, 69, 44);\n"
"color: rgb(255, 255, 255);")

        self.verticalLayout.addWidget(self.pushButton_37)

        self.pushButton_17 = QPushButton(self.layoutWidget)
        self.pushButton_17.setObjectName(u"pushButton_17")
        self.pushButton_17.setStyleSheet(u"background-color: rgb(99, 69, 44);\n"
"color: rgb(255, 255, 255);")

        self.verticalLayout.addWidget(self.pushButton_17)

        self.pushButton_38 = QPushButton(self.layoutWidget)
        self.pushButton_38.setObjectName(u"pushButton_38")
        self.pushButton_38.setStyleSheet(u"background-color: rgb(99, 69, 44);\n"
"color: rgb(255, 255, 255);")

        self.verticalLayout.addWidget(self.pushButton_38)

        self.pushButton_39 = QPushButton(self.layoutWidget)
        self.pushButton_39.setObjectName(u"pushButton_39")
        self.pushButton_39.setStyleSheet(u"background-color: rgb(99, 69, 44);\n"
"color: rgb(255, 255, 255);")

        self.verticalLayout.addWidget(self.pushButton_39)

        self.pushButton_19 = QPushButton(self.layoutWidget)
        self.pushButton_19.setObjectName(u"pushButton_19")
        self.pushButton_19.setStyleSheet(u"background-color: rgb(99, 69, 44);\n"
"color: rgb(255, 255, 255);")

        self.verticalLayout.addWidget(self.pushButton_19)

        self.pushButton_22 = QPushButton(self.layoutWidget)
        self.pushButton_22.setObjectName(u"pushButton_22")
        self.pushButton_22.setStyleSheet(u"background-color: rgb(99, 69, 44);\n"
"color: rgb(255, 255, 255);")

        self.verticalLayout.addWidget(self.pushButton_22)

        self.pushButton_23 = QPushButton(self.layoutWidget)
        self.pushButton_23.setObjectName(u"pushButton_23")
        self.pushButton_23.setStyleSheet(u"background-color: rgb(99, 69, 44);\n"
"color: rgb(255, 255, 255);")

        self.verticalLayout.addWidget(self.pushButton_23)

        self.pushButton_36 = QPushButton(self.layoutWidget)
        self.pushButton_36.setObjectName(u"pushButton_36")
        self.pushButton_36.setStyleSheet(u"background-color: rgb(99, 69, 44);\n"
"color: rgb(255, 255, 255);")

        self.verticalLayout.addWidget(self.pushButton_36)


        self.horizontalLayout_2.addWidget(self.frame_left_menu)

        self.frame_pages = QFrame(self.Content)
        self.frame_pages.setObjectName(u"frame_pages")
        self.frame_pages.setFrameShape(QFrame.StyledPanel)
        self.frame_pages.setFrameShadow(QFrame.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.frame_pages)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.stackedWidget = QStackedWidget(self.frame_pages)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page_5 = QWidget()
        self.page_5.setObjectName(u"page_5")
        self.gridLayout_24 = QGridLayout(self.page_5)
        self.gridLayout_24.setObjectName(u"gridLayout_24")
        self.label_3 = QLabel(self.page_5)
        self.label_3.setObjectName(u"label_3")
        font = QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-image: url(./images/voiceAnalysis.png);\n"
"background-position:center;\n"
"background-repeate:no-repeate;")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.gridLayout_24.addWidget(self.label_3, 0, 0, 1, 1)

        self.widget_15 = QWidget(self.page_5)
        self.widget_15.setObjectName(u"widget_15")
        self.gridLayout_25 = QGridLayout(self.widget_15)
        self.gridLayout_25.setObjectName(u"gridLayout_25")
        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.pushButton_24 = QPushButton(self.widget_15)
        self.pushButton_24.setObjectName(u"pushButton_24")
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(True)
        font1.setWeight(75)
        self.pushButton_24.setFont(font1)
        self.pushButton_24.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(26, 95, 180);")

        self.horizontalLayout_11.addWidget(self.pushButton_24)

        self.pushButton_25 = QPushButton(self.widget_15)
        self.pushButton_25.setObjectName(u"pushButton_25")
        self.pushButton_25.setFont(font1)
        self.pushButton_25.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(229, 165, 10);")

        self.horizontalLayout_11.addWidget(self.pushButton_25)


        self.gridLayout_25.addLayout(self.horizontalLayout_11, 0, 0, 1, 1)


        self.gridLayout_24.addWidget(self.widget_15, 1, 0, 1, 1)

        self.stackedWidget.addWidget(self.page_5)
        self.page_6 = QWidget()
        self.page_6.setObjectName(u"page_6")
        self.gridLayout_26 = QGridLayout(self.page_6)
        self.gridLayout_26.setObjectName(u"gridLayout_26")
        self.widget_16 = QWidget(self.page_6)
        self.widget_16.setObjectName(u"widget_16")

        self.gridLayout_26.addWidget(self.widget_16, 0, 0, 1, 5)

        self.pushButton_26 = QPushButton(self.page_6)
        self.pushButton_26.setObjectName(u"pushButton_26")
        self.pushButton_26.setFont(font1)
        self.pushButton_26.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(26, 95, 180);")

        self.gridLayout_26.addWidget(self.pushButton_26, 1, 0, 1, 1)

        self.pushButton_27 = QPushButton(self.page_6)
        self.pushButton_27.setObjectName(u"pushButton_27")
        self.pushButton_27.setFont(font1)
        self.pushButton_27.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(38, 162, 105);")

        self.gridLayout_26.addWidget(self.pushButton_27, 1, 1, 1, 1)

        self.pushButton_28 = QPushButton(self.page_6)
        self.pushButton_28.setObjectName(u"pushButton_28")
        self.pushButton_28.setFont(font1)
        self.pushButton_28.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(229, 165, 10);")

        self.gridLayout_26.addWidget(self.pushButton_28, 1, 2, 1, 1)

        self.pushButton_29 = QPushButton(self.page_6)
        self.pushButton_29.setObjectName(u"pushButton_29")
        self.pushButton_29.setFont(font1)
        self.pushButton_29.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(165, 29, 45);")

        self.gridLayout_26.addWidget(self.pushButton_29, 1, 3, 1, 1)

        self.pushButton_30 = QPushButton(self.page_6)
        self.pushButton_30.setObjectName(u"pushButton_30")
        self.pushButton_30.setFont(font1)
        self.pushButton_30.setStyleSheet(u"background-color: rgb(97, 53, 131);\n"
"color: rgb(255, 255, 255);")

        self.gridLayout_26.addWidget(self.pushButton_30, 1, 4, 1, 1)

        self.stackedWidget.addWidget(self.page_6)
        self.page_1 = QWidget()
        self.page_1.setObjectName(u"page_1")
        self.gridLayout_14 = QGridLayout(self.page_1)
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.label_8 = QLabel(self.page_1)
        self.label_8.setObjectName(u"label_8")
        font2 = QFont()
        font2.setPointSize(25)
        font2.setBold(True)
        font2.setWeight(75)
        self.label_8.setFont(font2)
        self.label_8.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_8.setAlignment(Qt.AlignCenter)

        self.gridLayout_14.addWidget(self.label_8, 0, 0, 1, 1)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.verticalLayout_16 = QVBoxLayout()
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.label_31 = QLabel(self.page_1)
        self.label_31.setObjectName(u"label_31")
        font3 = QFont()
        font3.setPointSize(14)
        font3.setBold(True)
        font3.setWeight(75)
        self.label_31.setFont(font3)
        self.label_31.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_16.addWidget(self.label_31)

        self.lineEdit_6 = QLineEdit(self.page_1)
        self.lineEdit_6.setObjectName(u"lineEdit_6")
        self.lineEdit_6.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout_16.addWidget(self.lineEdit_6)


        self.horizontalLayout_12.addLayout(self.verticalLayout_16)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_5 = QLabel(self.page_1)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font3)
        self.label_5.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_4.addWidget(self.label_5)

        self.lineEdit_5 = QLineEdit(self.page_1)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        self.lineEdit_5.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout_4.addWidget(self.lineEdit_5)


        self.horizontalLayout_12.addLayout(self.verticalLayout_4)


        self.gridLayout_14.addLayout(self.horizontalLayout_12, 1, 0, 1, 1)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_6 = QLabel(self.page_1)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font3)
        self.label_6.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_7.addWidget(self.label_6)

        self.lineEdit_8 = QLineEdit(self.page_1)
        self.lineEdit_8.setObjectName(u"lineEdit_8")
        self.lineEdit_8.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout_7.addWidget(self.lineEdit_8)


        self.horizontalLayout_13.addLayout(self.verticalLayout_7)

        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.label_20 = QLabel(self.page_1)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setFont(font3)
        self.label_20.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_9.addWidget(self.label_20)

        self.dateTimeEdit = QDateTimeEdit(self.page_1)
        self.dateTimeEdit.setObjectName(u"dateTimeEdit")
        self.dateTimeEdit.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout_9.addWidget(self.dateTimeEdit)


        self.horizontalLayout_13.addLayout(self.verticalLayout_9)


        self.gridLayout_14.addLayout(self.horizontalLayout_13, 2, 0, 1, 1)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.label_22 = QLabel(self.page_1)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setFont(font3)
        self.label_22.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_10.addWidget(self.label_22)

        self.lineEdit_9 = QLineEdit(self.page_1)
        self.lineEdit_9.setObjectName(u"lineEdit_9")
        self.lineEdit_9.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout_10.addWidget(self.lineEdit_9)


        self.horizontalLayout_14.addLayout(self.verticalLayout_10)

        self.verticalLayout_13 = QVBoxLayout()
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.label_28 = QLabel(self.page_1)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setFont(font3)
        self.label_28.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_13.addWidget(self.label_28)

        self.lineEdit_11 = QLineEdit(self.page_1)
        self.lineEdit_11.setObjectName(u"lineEdit_11")
        self.lineEdit_11.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout_13.addWidget(self.lineEdit_11)


        self.horizontalLayout_14.addLayout(self.verticalLayout_13)


        self.gridLayout_14.addLayout(self.horizontalLayout_14, 3, 0, 1, 1)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.verticalLayout_12 = QVBoxLayout()
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.label_27 = QLabel(self.page_1)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setFont(font3)
        self.label_27.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_12.addWidget(self.label_27)

        self.lineEdit_10 = QLineEdit(self.page_1)
        self.lineEdit_10.setObjectName(u"lineEdit_10")
        self.lineEdit_10.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout_12.addWidget(self.lineEdit_10)


        self.horizontalLayout_15.addLayout(self.verticalLayout_12)

        self.verticalLayout_11 = QVBoxLayout()
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.label_26 = QLabel(self.page_1)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setFont(font3)
        self.label_26.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_11.addWidget(self.label_26)

        self.comboBox = QComboBox(self.page_1)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setStyleSheet(u"color: rgb(26, 95, 180);\n"
"background-color: rgb(255, 255, 255);")

        self.verticalLayout_11.addWidget(self.comboBox)


        self.horizontalLayout_15.addLayout(self.verticalLayout_11)


        self.gridLayout_14.addLayout(self.horizontalLayout_15, 4, 0, 1, 1)

        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.verticalLayout_14 = QVBoxLayout()
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.label_29 = QLabel(self.page_1)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setFont(font3)
        self.label_29.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_14.addWidget(self.label_29)

        self.lineEdit_12 = QLineEdit(self.page_1)
        self.lineEdit_12.setObjectName(u"lineEdit_12")
        self.lineEdit_12.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout_14.addWidget(self.lineEdit_12)


        self.horizontalLayout_16.addLayout(self.verticalLayout_14)

        self.verticalLayout_15 = QVBoxLayout()
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.label_30 = QLabel(self.page_1)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setFont(font3)
        self.label_30.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_15.addWidget(self.label_30)

        self.comboBox_2 = QComboBox(self.page_1)
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.setObjectName(u"comboBox_2")
        self.comboBox_2.setStyleSheet(u"color: rgb(26, 95, 180);\n"
"background-color: rgb(255, 255, 255);")

        self.verticalLayout_15.addWidget(self.comboBox_2)


        self.horizontalLayout_16.addLayout(self.verticalLayout_15)


        self.gridLayout_14.addLayout(self.horizontalLayout_16, 5, 0, 1, 1)

        self.verticalLayout_17 = QVBoxLayout()
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.label_32 = QLabel(self.page_1)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setFont(font3)
        self.label_32.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_17.addWidget(self.label_32)

        self.dateTimeEdit_2 = QDateTimeEdit(self.page_1)
        self.dateTimeEdit_2.setObjectName(u"dateTimeEdit_2")
        self.dateTimeEdit_2.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout_17.addWidget(self.dateTimeEdit_2)


        self.gridLayout_14.addLayout(self.verticalLayout_17, 6, 0, 1, 1)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_9 = QLabel(self.page_1)
        self.label_9.setObjectName(u"label_9")
        font4 = QFont()
        font4.setPointSize(12)
        self.label_9.setFont(font4)
        self.label_9.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_3.addWidget(self.label_9)

        self.pushButton = QPushButton(self.page_1)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(38, 162, 105);")

        self.horizontalLayout_3.addWidget(self.pushButton)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_10 = QLabel(self.page_1)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font4)
        self.label_10.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_4.addWidget(self.label_10)

        self.pushButton_2 = QPushButton(self.page_1)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(165, 29, 45);")

        self.horizontalLayout_4.addWidget(self.pushButton_2)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)


        self.gridLayout_14.addLayout(self.verticalLayout_2, 7, 0, 1, 1)

        self.horizontalLayout_35 = QHBoxLayout()
        self.horizontalLayout_35.setObjectName(u"horizontalLayout_35")
        self.pushButton_35 = QPushButton(self.page_1)
        self.pushButton_35.setObjectName(u"pushButton_35")
        font5 = QFont()
        font5.setPointSize(15)
        font5.setBold(True)
        font5.setWeight(75)
        self.pushButton_35.setFont(font5)
        self.pushButton_35.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(192, 28, 40);")

        self.horizontalLayout_35.addWidget(self.pushButton_35)

        self.pushButton_3 = QPushButton(self.page_1)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setFont(font5)
        self.pushButton_3.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(26, 95, 180);")

        self.horizontalLayout_35.addWidget(self.pushButton_3)


        self.gridLayout_14.addLayout(self.horizontalLayout_35, 8, 0, 1, 1)

        self.stackedWidget.addWidget(self.page_1)
        self.page_7 = QWidget()
        self.page_7.setObjectName(u"page_7")
        self.gridLayout_27 = QGridLayout(self.page_7)
        self.gridLayout_27.setObjectName(u"gridLayout_27")
        self.pushButton_34 = QPushButton(self.page_7)
        self.pushButton_34.setObjectName(u"pushButton_34")
        self.pushButton_34.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(237, 51, 59);")

        self.gridLayout_27.addWidget(self.pushButton_34, 1, 0, 1, 1)

        self.widget_17 = QWidget(self.page_7)
        self.widget_17.setObjectName(u"widget_17")
        self.widget_17.setStyleSheet(u"background-color: rgb(26, 95, 180);")
        self.gridLayout_15 = QGridLayout(self.widget_17)
        self.gridLayout_15.setObjectName(u"gridLayout_15")
        self.label_4 = QLabel(self.widget_17)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font5)
        self.label_4.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"border-color: rgb(255, 255, 255);")

        self.gridLayout_15.addWidget(self.label_4, 0, 0, 1, 1)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.label_34 = QLabel(self.widget_17)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setFont(font3)
        self.label_34.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_17.addWidget(self.label_34)

        self.label_39 = QLabel(self.widget_17)
        self.label_39.setObjectName(u"label_39")
        self.label_39.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_17.addWidget(self.label_39)


        self.verticalLayout_6.addLayout(self.horizontalLayout_17)

        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.label_35 = QLabel(self.widget_17)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setFont(font3)
        self.label_35.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_18.addWidget(self.label_35)

        self.label_40 = QLabel(self.widget_17)
        self.label_40.setObjectName(u"label_40")
        self.label_40.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_18.addWidget(self.label_40)


        self.verticalLayout_6.addLayout(self.horizontalLayout_18)

        self.horizontalLayout_19 = QHBoxLayout()
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.label_36 = QLabel(self.widget_17)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setFont(font3)
        self.label_36.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_19.addWidget(self.label_36)

        self.label_41 = QLabel(self.widget_17)
        self.label_41.setObjectName(u"label_41")
        self.label_41.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_19.addWidget(self.label_41)


        self.verticalLayout_6.addLayout(self.horizontalLayout_19)

        self.horizontalLayout_32 = QHBoxLayout()
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.label_64 = QLabel(self.widget_17)
        self.label_64.setObjectName(u"label_64")
        self.label_64.setFont(font3)
        self.label_64.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_32.addWidget(self.label_64)

        self.label_65 = QLabel(self.widget_17)
        self.label_65.setObjectName(u"label_65")
        self.label_65.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_32.addWidget(self.label_65)


        self.verticalLayout_6.addLayout(self.horizontalLayout_32)

        self.horizontalLayout_20 = QHBoxLayout()
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.label_37 = QLabel(self.widget_17)
        self.label_37.setObjectName(u"label_37")
        self.label_37.setFont(font3)
        self.label_37.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_20.addWidget(self.label_37)

        self.label_42 = QLabel(self.widget_17)
        self.label_42.setObjectName(u"label_42")
        self.label_42.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_20.addWidget(self.label_42)


        self.verticalLayout_6.addLayout(self.horizontalLayout_20)

        self.horizontalLayout_21 = QHBoxLayout()
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.label_38 = QLabel(self.widget_17)
        self.label_38.setObjectName(u"label_38")
        self.label_38.setFont(font3)
        self.label_38.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_21.addWidget(self.label_38)

        self.label_43 = QLabel(self.widget_17)
        self.label_43.setObjectName(u"label_43")
        self.label_43.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_21.addWidget(self.label_43)


        self.verticalLayout_6.addLayout(self.horizontalLayout_21)

        self.horizontalLayout_23 = QHBoxLayout()
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.label_45 = QLabel(self.widget_17)
        self.label_45.setObjectName(u"label_45")
        self.label_45.setFont(font3)
        self.label_45.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_23.addWidget(self.label_45)

        self.label_46 = QLabel(self.widget_17)
        self.label_46.setObjectName(u"label_46")
        self.label_46.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_23.addWidget(self.label_46)


        self.verticalLayout_6.addLayout(self.horizontalLayout_23)

        self.horizontalLayout_29 = QHBoxLayout()
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.label_47 = QLabel(self.widget_17)
        self.label_47.setObjectName(u"label_47")
        self.label_47.setFont(font3)
        self.label_47.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_29.addWidget(self.label_47)

        self.label_59 = QLabel(self.widget_17)
        self.label_59.setObjectName(u"label_59")
        self.label_59.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_29.addWidget(self.label_59)


        self.verticalLayout_6.addLayout(self.horizontalLayout_29)

        self.horizontalLayout_34 = QHBoxLayout()
        self.horizontalLayout_34.setObjectName(u"horizontalLayout_34")
        self.label_68 = QLabel(self.widget_17)
        self.label_68.setObjectName(u"label_68")
        self.label_68.setFont(font3)
        self.label_68.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_34.addWidget(self.label_68)

        self.label_69 = QLabel(self.widget_17)
        self.label_69.setObjectName(u"label_69")
        self.label_69.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_34.addWidget(self.label_69)


        self.verticalLayout_6.addLayout(self.horizontalLayout_34)


        self.gridLayout_15.addLayout(self.verticalLayout_6, 1, 0, 1, 1)


        self.gridLayout_27.addWidget(self.widget_17, 0, 0, 1, 1)

        self.pushButton_33 = QPushButton(self.page_7)
        self.pushButton_33.setObjectName(u"pushButton_33")
        font6 = QFont()
        font6.setBold(True)
        font6.setWeight(75)
        self.pushButton_33.setFont(font6)
        self.pushButton_33.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(26, 95, 180);")

        self.gridLayout_27.addWidget(self.pushButton_33, 1, 1, 1, 1)

        self.widget_18 = QWidget(self.page_7)
        self.widget_18.setObjectName(u"widget_18")
        self.widget_18.setStyleSheet(u"background-color: rgb(36, 31, 49);")
        self.gridLayout_19 = QGridLayout(self.widget_18)
        self.gridLayout_19.setObjectName(u"gridLayout_19")
        self.label_33 = QLabel(self.widget_18)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setFont(font5)
        self.label_33.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout_19.addWidget(self.label_33, 0, 0, 1, 1)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_24 = QHBoxLayout()
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.label_48 = QLabel(self.widget_18)
        self.label_48.setObjectName(u"label_48")
        self.label_48.setFont(font3)
        self.label_48.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_24.addWidget(self.label_48)

        self.label_49 = QLabel(self.widget_18)
        self.label_49.setObjectName(u"label_49")
        self.label_49.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_24.addWidget(self.label_49)


        self.verticalLayout_3.addLayout(self.horizontalLayout_24)

        self.horizontalLayout_25 = QHBoxLayout()
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.label_50 = QLabel(self.widget_18)
        self.label_50.setObjectName(u"label_50")
        self.label_50.setFont(font3)
        self.label_50.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_25.addWidget(self.label_50)

        self.label_51 = QLabel(self.widget_18)
        self.label_51.setObjectName(u"label_51")
        self.label_51.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_25.addWidget(self.label_51)


        self.verticalLayout_3.addLayout(self.horizontalLayout_25)

        self.horizontalLayout_26 = QHBoxLayout()
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.label_52 = QLabel(self.widget_18)
        self.label_52.setObjectName(u"label_52")
        self.label_52.setFont(font3)
        self.label_52.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_26.addWidget(self.label_52)

        self.label_53 = QLabel(self.widget_18)
        self.label_53.setObjectName(u"label_53")
        self.label_53.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_26.addWidget(self.label_53)


        self.verticalLayout_3.addLayout(self.horizontalLayout_26)

        self.horizontalLayout_33 = QHBoxLayout()
        self.horizontalLayout_33.setObjectName(u"horizontalLayout_33")
        self.label_66 = QLabel(self.widget_18)
        self.label_66.setObjectName(u"label_66")
        self.label_66.setFont(font3)
        self.label_66.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_33.addWidget(self.label_66)

        self.label_67 = QLabel(self.widget_18)
        self.label_67.setObjectName(u"label_67")
        self.label_67.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_33.addWidget(self.label_67)


        self.verticalLayout_3.addLayout(self.horizontalLayout_33)

        self.horizontalLayout_27 = QHBoxLayout()
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.label_54 = QLabel(self.widget_18)
        self.label_54.setObjectName(u"label_54")
        self.label_54.setFont(font3)
        self.label_54.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_27.addWidget(self.label_54)

        self.label_55 = QLabel(self.widget_18)
        self.label_55.setObjectName(u"label_55")
        self.label_55.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_27.addWidget(self.label_55)


        self.verticalLayout_3.addLayout(self.horizontalLayout_27)

        self.horizontalLayout_28 = QHBoxLayout()
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.label_56 = QLabel(self.widget_18)
        self.label_56.setObjectName(u"label_56")
        self.label_56.setFont(font3)
        self.label_56.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_28.addWidget(self.label_56)

        self.label_57 = QLabel(self.widget_18)
        self.label_57.setObjectName(u"label_57")
        self.label_57.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_28.addWidget(self.label_57)


        self.verticalLayout_3.addLayout(self.horizontalLayout_28)

        self.horizontalLayout_31 = QHBoxLayout()
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.label_62 = QLabel(self.widget_18)
        self.label_62.setObjectName(u"label_62")
        self.label_62.setFont(font3)
        self.label_62.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_31.addWidget(self.label_62)

        self.label_63 = QLabel(self.widget_18)
        self.label_63.setObjectName(u"label_63")
        self.label_63.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_31.addWidget(self.label_63)


        self.verticalLayout_3.addLayout(self.horizontalLayout_31)

        self.horizontalLayout_30 = QHBoxLayout()
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.label_60 = QLabel(self.widget_18)
        self.label_60.setObjectName(u"label_60")
        self.label_60.setFont(font3)
        self.label_60.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_30.addWidget(self.label_60)

        self.label_61 = QLabel(self.widget_18)
        self.label_61.setObjectName(u"label_61")
        self.label_61.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_30.addWidget(self.label_61)


        self.verticalLayout_3.addLayout(self.horizontalLayout_30)

        self.horizontalLayout_36 = QHBoxLayout()
        self.horizontalLayout_36.setObjectName(u"horizontalLayout_36")
        self.label_70 = QLabel(self.widget_18)
        self.label_70.setObjectName(u"label_70")
        self.label_70.setFont(font3)
        self.label_70.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_36.addWidget(self.label_70)

        self.label_71 = QLabel(self.widget_18)
        self.label_71.setObjectName(u"label_71")
        self.label_71.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_36.addWidget(self.label_71)


        self.verticalLayout_3.addLayout(self.horizontalLayout_36)


        self.gridLayout_19.addLayout(self.verticalLayout_3, 1, 0, 1, 1)


        self.gridLayout_27.addWidget(self.widget_18, 0, 1, 1, 1)

        self.stackedWidget.addWidget(self.page_7)
        self.page_8 = QWidget()
        self.page_8.setObjectName(u"page_8")
        self.gridLayout_30 = QGridLayout(self.page_8)
        self.gridLayout_30.setObjectName(u"gridLayout_30")
        self.widget_19 = QWidget(self.page_8)
        self.widget_19.setObjectName(u"widget_19")
        self.gridLayout_31 = QGridLayout(self.widget_19)
        self.gridLayout_31.setObjectName(u"gridLayout_31")
        self.verticalLayout_21 = QVBoxLayout()
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.label_58 = QLabel(self.widget_19)
        self.label_58.setObjectName(u"label_58")
        font7 = QFont()
        font7.setFamily(u"Samyak Tamil")
        font7.setPointSize(20)
        font7.setBold(True)
        font7.setItalic(True)
        font7.setWeight(75)
        self.label_58.setFont(font7)
        self.label_58.setStyleSheet(u"color: rgb(26, 95, 180);\n"
"color: rgb(255, 255, 255);")
        self.label_58.setPixmap(QPixmap(u"./newPrefix/Group 1.png"))
        self.label_58.setAlignment(Qt.AlignCenter)
        self.label_58.setWordWrap(True)

        self.verticalLayout_21.addWidget(self.label_58)

        self.horizontalLayout_22 = QHBoxLayout()
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.pushButton_32 = QPushButton(self.widget_19)
        self.pushButton_32.setObjectName(u"pushButton_32")
        self.pushButton_32.setFont(font6)
        self.pushButton_32.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(224, 27, 36);")

        self.horizontalLayout_22.addWidget(self.pushButton_32)

        self.pushButton_31 = QPushButton(self.widget_19)
        self.pushButton_31.setObjectName(u"pushButton_31")
        self.pushButton_31.setFont(font6)
        self.pushButton_31.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(26, 95, 180);")

        self.horizontalLayout_22.addWidget(self.pushButton_31)


        self.verticalLayout_21.addLayout(self.horizontalLayout_22)


        self.gridLayout_31.addLayout(self.verticalLayout_21, 0, 0, 1, 1)


        self.gridLayout_30.addWidget(self.widget_19, 1, 0, 1, 1)

        self.stackedWidget.addWidget(self.page_8)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.gridLayout_3 = QGridLayout(self.page_2)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.widget_2 = QWidget(self.page_2)
        self.widget_2.setObjectName(u"widget_2")
        self.gridLayout_4 = QGridLayout(self.widget_2)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.widget_5 = QWidget(self.widget_2)
        self.widget_5.setObjectName(u"widget_5")
        self.widget_5.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.gridLayout_7 = QGridLayout(self.widget_5)
        self.gridLayout_7.setObjectName(u"gridLayout_7")

        self.gridLayout_4.addWidget(self.widget_5, 1, 0, 1, 2)

        self.widget_6 = QWidget(self.widget_2)
        self.widget_6.setObjectName(u"widget_6")
        self.widget_6.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.gridLayout_9 = QGridLayout(self.widget_6)
        self.gridLayout_9.setObjectName(u"gridLayout_9")

        self.gridLayout_4.addWidget(self.widget_6, 2, 0, 1, 2)

        self.pushButton_6 = QPushButton(self.widget_2)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setFont(font1)
        self.pushButton_6.setStyleSheet(u"background-color: rgb(28, 113, 216);\n"
"color: rgb(255, 255, 255);")

        self.gridLayout_4.addWidget(self.pushButton_6, 3, 0, 1, 1)

        self.pushButton_7 = QPushButton(self.widget_2)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setFont(font1)
        self.pushButton_7.setStyleSheet(u"background-color: rgb(192, 28, 40);\n"
"color: rgb(255, 255, 255);")

        self.gridLayout_4.addWidget(self.pushButton_7, 3, 1, 1, 1)

        self.label_11 = QLabel(self.widget_2)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout_4.addWidget(self.label_11, 0, 0, 1, 2)


        self.gridLayout_3.addWidget(self.widget_2, 0, 1, 1, 1)

        self.widget = QWidget(self.page_2)
        self.widget.setObjectName(u"widget")
        self.gridLayout_5 = QGridLayout(self.widget)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout_5.addWidget(self.label_2, 0, 0, 1, 2)

        self.widget_3 = QWidget(self.widget)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.gridLayout_6 = QGridLayout(self.widget_3)
        self.gridLayout_6.setObjectName(u"gridLayout_6")

        self.gridLayout_5.addWidget(self.widget_3, 1, 0, 1, 2)

        self.widget_4 = QWidget(self.widget)
        self.widget_4.setObjectName(u"widget_4")
        self.widget_4.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.gridLayout_8 = QGridLayout(self.widget_4)
        self.gridLayout_8.setObjectName(u"gridLayout_8")

        self.gridLayout_5.addWidget(self.widget_4, 2, 0, 1, 2)

        self.pushButton_4 = QPushButton(self.widget)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setFont(font1)
        self.pushButton_4.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(28, 113, 216);")

        self.gridLayout_5.addWidget(self.pushButton_4, 3, 0, 1, 1)

        self.pushButton_5 = QPushButton(self.widget)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setFont(font1)
        self.pushButton_5.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(192, 28, 40);")

        self.gridLayout_5.addWidget(self.pushButton_5, 3, 1, 1, 1)


        self.gridLayout_3.addWidget(self.widget, 0, 0, 1, 1)

        self.pushButton_8 = QPushButton(self.page_2)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setFont(font1)
        self.pushButton_8.setStyleSheet(u"background-color: rgb(97, 53, 131);\n"
"color: rgb(255, 255, 255);")

        self.gridLayout_3.addWidget(self.pushButton_8, 1, 1, 1, 1)

        self.pushButton_9 = QPushButton(self.page_2)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setFont(font1)
        self.pushButton_9.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(38, 162, 105);")

        self.gridLayout_3.addWidget(self.pushButton_9, 1, 0, 1, 1)

        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.gridLayout_10 = QGridLayout(self.page_3)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.widget_7 = QWidget(self.page_3)
        self.widget_7.setObjectName(u"widget_7")
        self.gridLayout_11 = QGridLayout(self.widget_7)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.label = QLabel(self.widget_7)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout_11.addWidget(self.label, 0, 0, 1, 1)

        self.widget_11 = QWidget(self.widget_7)
        self.widget_11.setObjectName(u"widget_11")
        self.widget_11.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.gridLayout_20 = QGridLayout(self.widget_11)
        self.gridLayout_20.setObjectName(u"gridLayout_20")

        self.gridLayout_11.addWidget(self.widget_11, 1, 0, 1, 2)

        self.widget_12 = QWidget(self.widget_7)
        self.widget_12.setObjectName(u"widget_12")
        self.widget_12.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.gridLayout_21 = QGridLayout(self.widget_12)
        self.gridLayout_21.setObjectName(u"gridLayout_21")

        self.gridLayout_11.addWidget(self.widget_12, 2, 0, 1, 2)

        self.pushButton_10 = QPushButton(self.widget_7)
        self.pushButton_10.setObjectName(u"pushButton_10")
        self.pushButton_10.setFont(font1)
        self.pushButton_10.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(26, 95, 180);")

        self.gridLayout_11.addWidget(self.pushButton_10, 3, 0, 1, 1)

        self.pushButton_11 = QPushButton(self.widget_7)
        self.pushButton_11.setObjectName(u"pushButton_11")
        self.pushButton_11.setFont(font1)
        self.pushButton_11.setStyleSheet(u"background-color: rgb(192, 28, 40);\n"
"color: rgb(255, 255, 255);")

        self.gridLayout_11.addWidget(self.pushButton_11, 3, 1, 1, 1)


        self.gridLayout_10.addWidget(self.widget_7, 0, 0, 1, 1)

        self.widget_8 = QWidget(self.page_3)
        self.widget_8.setObjectName(u"widget_8")
        self.gridLayout_12 = QGridLayout(self.widget_8)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.label_12 = QLabel(self.widget_8)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout_12.addWidget(self.label_12, 0, 0, 1, 2)

        self.widget_13 = QWidget(self.widget_8)
        self.widget_13.setObjectName(u"widget_13")
        self.widget_13.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.gridLayout_22 = QGridLayout(self.widget_13)
        self.gridLayout_22.setObjectName(u"gridLayout_22")

        self.gridLayout_12.addWidget(self.widget_13, 1, 0, 1, 2)

        self.widget_14 = QWidget(self.widget_8)
        self.widget_14.setObjectName(u"widget_14")
        self.widget_14.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.gridLayout_23 = QGridLayout(self.widget_14)
        self.gridLayout_23.setObjectName(u"gridLayout_23")

        self.gridLayout_12.addWidget(self.widget_14, 2, 0, 1, 2)

        self.pushButton_13 = QPushButton(self.widget_8)
        self.pushButton_13.setObjectName(u"pushButton_13")
        self.pushButton_13.setFont(font1)
        self.pushButton_13.setStyleSheet(u"background-color: rgb(28, 113, 216);\n"
"color: rgb(255, 255, 255);")

        self.gridLayout_12.addWidget(self.pushButton_13, 3, 0, 1, 1)

        self.pushButton_12 = QPushButton(self.widget_8)
        self.pushButton_12.setObjectName(u"pushButton_12")
        self.pushButton_12.setFont(font1)
        self.pushButton_12.setStyleSheet(u"background-color: rgb(192, 28, 40);\n"
"color: rgb(255, 255, 255);")

        self.gridLayout_12.addWidget(self.pushButton_12, 3, 1, 1, 1)


        self.gridLayout_10.addWidget(self.widget_8, 0, 1, 1, 1)

        self.pushButton_14 = QPushButton(self.page_3)
        self.pushButton_14.setObjectName(u"pushButton_14")
        self.pushButton_14.setFont(font1)
        self.pushButton_14.setStyleSheet(u"background-color: rgb(38, 162, 105);\n"
"color: rgb(255, 255, 255);")

        self.gridLayout_10.addWidget(self.pushButton_14, 1, 0, 1, 1)

        self.pushButton_15 = QPushButton(self.page_3)
        self.pushButton_15.setObjectName(u"pushButton_15")
        self.pushButton_15.setFont(font1)
        self.pushButton_15.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(97, 53, 131);")

        self.gridLayout_10.addWidget(self.pushButton_15, 1, 1, 1, 1)

        self.stackedWidget.addWidget(self.page_3)
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.gridLayout_13 = QGridLayout(self.page)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.pushButton_21 = QPushButton(self.page)
        self.pushButton_21.setObjectName(u"pushButton_21")
        self.pushButton_21.setFont(font1)
        self.pushButton_21.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(38, 162, 105);")

        self.gridLayout_13.addWidget(self.pushButton_21, 1, 0, 1, 1)

        self.pushButton_16 = QPushButton(self.page)
        self.pushButton_16.setObjectName(u"pushButton_16")
        self.pushButton_16.setFont(font1)
        self.pushButton_16.setStyleSheet(u"background-color: rgb(26, 95, 180);\n"
"color: rgb(255, 255, 255);")

        self.gridLayout_13.addWidget(self.pushButton_16, 1, 1, 1, 1)

        self.widget_9 = QWidget(self.page)
        self.widget_9.setObjectName(u"widget_9")
        self.gridLayout_16 = QGridLayout(self.widget_9)
        self.gridLayout_16.setObjectName(u"gridLayout_16")
        self.widget_21 = QWidget(self.widget_9)
        self.widget_21.setObjectName(u"widget_21")
        self.widget_21.setStyleSheet(u"background-color: rgb(26, 95, 180);")
        self.gridLayout_32 = QGridLayout(self.widget_21)
        self.gridLayout_32.setObjectName(u"gridLayout_32")
        self.label_44 = QLabel(self.widget_21)
        self.label_44.setObjectName(u"label_44")
        font8 = QFont()
        font8.setPointSize(15)
        font8.setBold(True)
        font8.setItalic(True)
        font8.setWeight(75)
        self.label_44.setFont(font8)
        self.label_44.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_44.setAlignment(Qt.AlignCenter)

        self.gridLayout_32.addWidget(self.label_44, 0, 0, 1, 1)


        self.gridLayout_16.addWidget(self.widget_21, 0, 0, 1, 1)

        self.label_13 = QLabel(self.widget_9)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setFont(font3)
        self.label_13.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_13.setTextFormat(Qt.MarkdownText)
        self.label_13.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_13.setWordWrap(True)

        self.gridLayout_16.addWidget(self.label_13, 1, 0, 1, 1)

        self.label_74 = QLabel(self.widget_9)
        self.label_74.setObjectName(u"label_74")
        self.label_74.setFont(font3)
        self.label_74.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout_16.addWidget(self.label_74, 2, 0, 1, 1)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_75 = QLabel(self.widget_9)
        self.label_75.setObjectName(u"label_75")
        font9 = QFont()
        font9.setPointSize(13)
        font9.setBold(True)
        font9.setWeight(75)
        self.label_75.setFont(font9)
        self.label_75.setStyleSheet(u"color: rgb(246, 245, 244);")

        self.verticalLayout_5.addWidget(self.label_75)

        self.label_76 = QLabel(self.widget_9)
        self.label_76.setObjectName(u"label_76")
        self.label_76.setFont(font9)
        self.label_76.setStyleSheet(u"color: rgb(246, 245, 244);")

        self.verticalLayout_5.addWidget(self.label_76)

        self.label_77 = QLabel(self.widget_9)
        self.label_77.setObjectName(u"label_77")
        self.label_77.setFont(font9)
        self.label_77.setStyleSheet(u"color: rgb(246, 245, 244);")

        self.verticalLayout_5.addWidget(self.label_77)

        self.label_78 = QLabel(self.widget_9)
        self.label_78.setObjectName(u"label_78")
        self.label_78.setFont(font9)
        self.label_78.setStyleSheet(u"color: rgb(246, 245, 244);")

        self.verticalLayout_5.addWidget(self.label_78)


        self.gridLayout_16.addLayout(self.verticalLayout_5, 3, 0, 1, 1)

        self.frame_5 = QFrame(self.widget_9)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setStyleSheet(u"border: 1px solid;\n"
"border-radius:20px;\n"
"padding: 10px;\n"
"box-shadow: 10px 10px 28px 0px #888888;\n"
"background-color: rgb(0, 0, 0);")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_5)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_14 = QLabel(self.frame_5)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setFont(font5)
        self.label_14.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout.addWidget(self.label_14)

        self.label_15 = QLabel(self.frame_5)
        self.label_15.setObjectName(u"label_15")
        font10 = QFont()
        font10.setPointSize(50)
        font10.setBold(True)
        font10.setWeight(75)
        self.label_15.setFont(font10)
        self.label_15.setStyleSheet(u"color: rgb(26, 95, 180);\n"
"border-color: rgb(38, 162, 105);")
        self.label_15.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.label_15)


        self.gridLayout_16.addWidget(self.frame_5, 4, 0, 1, 1)

        self.label_79 = QLabel(self.widget_9)
        self.label_79.setObjectName(u"label_79")
        self.label_79.setFont(font3)
        self.label_79.setStyleSheet(u"color: rgb(246, 245, 244);")
        self.label_79.setWordWrap(True)

        self.gridLayout_16.addWidget(self.label_79, 5, 0, 1, 1)


        self.gridLayout_13.addWidget(self.widget_9, 0, 0, 1, 2)

        self.stackedWidget.addWidget(self.page)
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.gridLayout_17 = QGridLayout(self.page_4)
        self.gridLayout_17.setObjectName(u"gridLayout_17")
        self.widget_10 = QWidget(self.page_4)
        self.widget_10.setObjectName(u"widget_10")
        self.widget_10.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.gridLayout_18 = QGridLayout(self.widget_10)
        self.gridLayout_18.setObjectName(u"gridLayout_18")

        self.gridLayout_17.addWidget(self.widget_10, 0, 0, 1, 2)

        self.pushButton_20 = QPushButton(self.page_4)
        self.pushButton_20.setObjectName(u"pushButton_20")
        self.pushButton_20.setFont(font6)
        self.pushButton_20.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(224, 27, 36);")

        self.gridLayout_17.addWidget(self.pushButton_20, 1, 0, 1, 1)

        self.pushButton_18 = QPushButton(self.page_4)
        self.pushButton_18.setObjectName(u"pushButton_18")
        self.pushButton_18.setFont(font6)
        self.pushButton_18.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(26, 95, 180);")

        self.gridLayout_17.addWidget(self.pushButton_18, 1, 1, 1, 1)

        self.stackedWidget.addWidget(self.page_4)

        self.verticalLayout_18.addWidget(self.stackedWidget)


        self.horizontalLayout_2.addWidget(self.frame_pages)


        self.gridLayout.addWidget(self.Content, 0, 0, 1, 1)

        self.Top_Bar = QFrame(self.centralwidget)
        self.Top_Bar.setObjectName(u"Top_Bar")
        self.Top_Bar.setMaximumSize(QSize(16777215, 40))
        self.Top_Bar.setStyleSheet(u"background-color: rgb(35, 35, 35);")
        self.Top_Bar.setFrameShape(QFrame.NoFrame)
        self.Top_Bar.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.Top_Bar)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)

        self.gridLayout.addWidget(self.Top_Bar, 1, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"FORENSIC VOICE COMPARISON TOOL ", None))
        self.label_7.setText("")
        self.pushButton_37.setText(QCoreApplication.translate("MainWindow", u"Welcome page", None))
        self.pushButton_17.setText(QCoreApplication.translate("MainWindow", u"voice upload", None))
        self.pushButton_38.setText(QCoreApplication.translate("MainWindow", u"metadata review", None))
        self.pushButton_39.setText(QCoreApplication.translate("MainWindow", u"Authenticate page", None))
        self.pushButton_19.setText(QCoreApplication.translate("MainWindow", u"voice filter", None))
        self.pushButton_22.setText(QCoreApplication.translate("MainWindow", u"voice comparison", None))
        self.pushButton_23.setText(QCoreApplication.translate("MainWindow", u"result page", None))
        self.pushButton_36.setText(QCoreApplication.translate("MainWindow", u"view report", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"WELCOME TO FORENSIC VOICE COMPARISON TOOL", None))
        self.pushButton_24.setText(QCoreApplication.translate("MainWindow", u"SINGLE SPEAKER", None))
        self.pushButton_25.setText(QCoreApplication.translate("MainWindow", u"MULTSPEAKER", None))
        self.pushButton_26.setText(QCoreApplication.translate("MainWindow", u"UPLOAD FILE", None))
        self.pushButton_27.setText(QCoreApplication.translate("MainWindow", u"PLAY", None))
        self.pushButton_28.setText(QCoreApplication.translate("MainWindow", u"PAUSE", None))
        self.pushButton_29.setText(QCoreApplication.translate("MainWindow", u"TRIM", None))
        self.pushButton_30.setText(QCoreApplication.translate("MainWindow", u"NEXT", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"UPLOAD PAGE", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"Case Number", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Investigator 's Name", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Suspect 's Name", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"Date and Time of Case", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"Device name", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"Crime Scene Location", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"Crime Audio Name", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"Crime Audio File Formats", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u".MP4", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u".MP3", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u".FLAC", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("MainWindow", u".WAV", None))
        self.comboBox.setItemText(4, QCoreApplication.translate("MainWindow", u".PCM", None))
        self.comboBox.setItemText(5, QCoreApplication.translate("MainWindow", u".ACC", None))
        self.comboBox.setItemText(6, QCoreApplication.translate("MainWindow", u".M4a", None))
        self.comboBox.setItemText(7, QCoreApplication.translate("MainWindow", u".M4P", None))
        self.comboBox.setItemText(8, QCoreApplication.translate("MainWindow", u".WMA", None))

        self.label_29.setText(QCoreApplication.translate("MainWindow", u"Suspect Audio Name", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"Suspect Audio File Formats", None))
        self.comboBox_2.setItemText(0, QCoreApplication.translate("MainWindow", u".MP4", None))
        self.comboBox_2.setItemText(1, QCoreApplication.translate("MainWindow", u".MP3", None))
        self.comboBox_2.setItemText(2, QCoreApplication.translate("MainWindow", u".FLAC", None))
        self.comboBox_2.setItemText(3, QCoreApplication.translate("MainWindow", u".WAV", None))
        self.comboBox_2.setItemText(4, QCoreApplication.translate("MainWindow", u".PCM", None))
        self.comboBox_2.setItemText(5, QCoreApplication.translate("MainWindow", u".ACC", None))
        self.comboBox_2.setItemText(6, QCoreApplication.translate("MainWindow", u".M4a", None))
        self.comboBox_2.setItemText(7, QCoreApplication.translate("MainWindow", u".MP4", None))
        self.comboBox_2.setItemText(8, QCoreApplication.translate("MainWindow", u".M4P", None))
        self.comboBox_2.setItemText(9, QCoreApplication.translate("MainWindow", u".WMA", None))

        self.label_32.setText(QCoreApplication.translate("MainWindow", u"Date and Time of Evidence Acqusition", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Crime Voice", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"upload file", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Suspect Voice", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"upload file", None))
        self.pushButton_35.setText(QCoreApplication.translate("MainWindow", u"BACK", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"SUBMIT", None))
        self.pushButton_34.setText(QCoreApplication.translate("MainWindow", u"BACK", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"CRIME VOICE METADATA", None))
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"File Format", None))
        self.label_39.setText("")
        self.label_35.setText(QCoreApplication.translate("MainWindow", u"Hash Value", None))
        self.label_40.setText("")
        self.label_36.setText(QCoreApplication.translate("MainWindow", u"Creation date", None))
        self.label_41.setText("")
        self.label_64.setText(QCoreApplication.translate("MainWindow", u"Modification date", None))
        self.label_65.setText("")
        self.label_37.setText(QCoreApplication.translate("MainWindow", u"Bit Rate", None))
        self.label_42.setText("")
        self.label_38.setText(QCoreApplication.translate("MainWindow", u"Sample Rate", None))
        self.label_43.setText("")
        self.label_45.setText(QCoreApplication.translate("MainWindow", u"Codec Information", None))
        self.label_46.setText("")
        self.label_47.setText(QCoreApplication.translate("MainWindow", u"Clip Length In Second", None))
        self.label_59.setText("")
        self.label_68.setText(QCoreApplication.translate("MainWindow", u"Audio Channel", None))
        self.label_69.setText("")
        self.pushButton_33.setText(QCoreApplication.translate("MainWindow", u"NEXT", None))
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"SUSPECT VOICE METADATA", None))
        self.label_48.setText(QCoreApplication.translate("MainWindow", u"File Format", None))
        self.label_49.setText("")
        self.label_50.setText(QCoreApplication.translate("MainWindow", u"Hash Value", None))
        self.label_51.setText("")
        self.label_52.setText(QCoreApplication.translate("MainWindow", u"Creation date", None))
        self.label_53.setText("")
        self.label_66.setText(QCoreApplication.translate("MainWindow", u"Modification date", None))
        self.label_67.setText("")
        self.label_54.setText(QCoreApplication.translate("MainWindow", u"Bit Rate", None))
        self.label_55.setText("")
        self.label_56.setText(QCoreApplication.translate("MainWindow", u"Sample Rate", None))
        self.label_57.setText("")
        self.label_62.setText(QCoreApplication.translate("MainWindow", u"Codec Information", None))
        self.label_63.setText("")
        self.label_60.setText(QCoreApplication.translate("MainWindow", u"Clip Length In Second", None))
        self.label_61.setText("")
        self.label_70.setText(QCoreApplication.translate("MainWindow", u"Audio Channel", None))
        self.label_71.setText("")
        self.label_58.setText("")
        self.pushButton_32.setText(QCoreApplication.translate("MainWindow", u"BACK", None))
        self.pushButton_31.setText(QCoreApplication.translate("MainWindow", u"NEXT", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"PLAY", None))
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"STOP", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Suspect Audio Wave Forms", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Crime Audio Wave Forms", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"PLAY", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"STOP", None))
        self.pushButton_8.setText(QCoreApplication.translate("MainWindow", u"FILTER", None))
        self.pushButton_9.setText(QCoreApplication.translate("MainWindow", u"BACK", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Cleaned Crime Audio file", None))
        self.pushButton_10.setText(QCoreApplication.translate("MainWindow", u"PLAY", None))
        self.pushButton_11.setText(QCoreApplication.translate("MainWindow", u"STOP", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Cleaned Suspect Audio file", None))
        self.pushButton_13.setText(QCoreApplication.translate("MainWindow", u"PLAY", None))
        self.pushButton_12.setText(QCoreApplication.translate("MainWindow", u"STOP", None))
        self.pushButton_14.setText(QCoreApplication.translate("MainWindow", u"BACK", None))
        self.pushButton_15.setText(QCoreApplication.translate("MainWindow", u"COMPARE", None))
        self.pushButton_21.setText(QCoreApplication.translate("MainWindow", u"BACK", None))
        self.pushButton_16.setText(QCoreApplication.translate("MainWindow", u"VIEW REPORT", None))
        self.label_44.setText(QCoreApplication.translate("MainWindow", u"Speaker Comparison Results", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"This page presents the results of a comparison between two audio recordings to determine the likelihood that the speakers are the same person. The results are expressed in terms of likelihood ratios, ranging from 0.0 to 1.0.", None))
        self.label_74.setText(QCoreApplication.translate("MainWindow", u"Likelihood Ratio Presentation:", None))
        self.label_75.setText(QCoreApplication.translate("MainWindow", u"0.0 - 0.3: Very strong evidence the speakers are different.", None))
        self.label_76.setText(QCoreApplication.translate("MainWindow", u"0.3 - 0.7: Evidence suggests the speakers are likely different.", None))
        self.label_77.setText(QCoreApplication.translate("MainWindow", u"0.7 - 0.9: Inconclusive - more information needed.", None))
        self.label_78.setText(QCoreApplication.translate("MainWindow", u"0.9 - 1.0: Strong evidence the speakers are the same.", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Likelihood Ratios", None))
        self.label_15.setText("")
        self.label_79.setText(QCoreApplication.translate("MainWindow", u"Based on the likelihood ratio, it is [unlikely/likely] that the speakers from the two recordings are the same person.", None))
        self.pushButton_20.setText(QCoreApplication.translate("MainWindow", u"BACK", None))
        self.pushButton_18.setText(QCoreApplication.translate("MainWindow", u"SAVE", None))
    # retranslateUi

