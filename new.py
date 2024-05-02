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
        MainWindow.setStyleSheet(u"background-color: rgb(43, 43, 43);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
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
        self.pushButton_17 = QPushButton(self.layoutWidget)
        self.pushButton_17.setObjectName(u"pushButton_17")
        self.pushButton_17.setStyleSheet(u"background-color: rgb(99, 69, 44);\n"
"color: rgb(255, 255, 255);")

        self.verticalLayout.addWidget(self.pushButton_17)

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


        self.horizontalLayout_2.addWidget(self.frame_left_menu)

        self.frame_pages = QFrame(self.Content)
        self.frame_pages.setObjectName(u"frame_pages")
        self.frame_pages.setFrameShape(QFrame.StyledPanel)
        self.frame_pages.setFrameShadow(QFrame.Raised)
        self.gridLayout_19 = QGridLayout(self.frame_pages)
        self.gridLayout_19.setObjectName(u"gridLayout_19")
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
        self.verticalLayout_9 = QVBoxLayout(self.page_1)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_9.addItem(self.verticalSpacer_2)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_8 = QLabel(self.page_1)
        self.label_8.setObjectName(u"label_8")
        font2 = QFont()
        font2.setPointSize(25)
        font2.setBold(True)
        font2.setWeight(75)
        self.label_8.setFont(font2)
        self.label_8.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_8.setAlignment(Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.label_8)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacer_3)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_9 = QLabel(self.page_1)
        self.label_9.setObjectName(u"label_9")
        font3 = QFont()
        font3.setPointSize(12)
        self.label_9.setFont(font3)
        self.label_9.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_3.addWidget(self.label_9)

        self.pushButton = QPushButton(self.page_1)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(38, 162, 105);")

        self.horizontalLayout_3.addWidget(self.pushButton)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_5)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_10 = QLabel(self.page_1)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font3)
        self.label_10.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_4.addWidget(self.label_10)

        self.pushButton_2 = QPushButton(self.page_1)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(165, 29, 45);")

        self.horizontalLayout_4.addWidget(self.pushButton_2)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)


        self.verticalLayout_3.addLayout(self.verticalLayout_2)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_4)

        self.pushButton_3 = QPushButton(self.page_1)
        self.pushButton_3.setObjectName(u"pushButton_3")
        font4 = QFont()
        font4.setPointSize(15)
        font4.setBold(True)
        font4.setWeight(75)
        self.pushButton_3.setFont(font4)
        self.pushButton_3.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(26, 95, 180);")

        self.verticalLayout_3.addWidget(self.pushButton_3)


        self.verticalLayout_7.addLayout(self.verticalLayout_3)


        self.verticalLayout_9.addLayout(self.verticalLayout_7)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_9.addItem(self.verticalSpacer)

        self.stackedWidget.addWidget(self.page_1)
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
        self.gridLayout_15 = QGridLayout(self.widget_9)
        self.gridLayout_15.setObjectName(u"gridLayout_15")
        self.frame_6 = QFrame(self.widget_9)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setStyleSheet(u"border: 1px solid;\n"
"border-radius:5px;\n"
"padding: 10px;\n"
"background-image: url(./images/voiceAnalysis.png);\n"
"background-position:center;\n"
"background-repeate:no-repeate;\n"
"")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.gridLayout_14 = QGridLayout(self.frame_6)
        self.gridLayout_14.setObjectName(u"gridLayout_14")

        self.gridLayout_15.addWidget(self.frame_6, 0, 0, 1, 1)

        self.frame_5 = QFrame(self.widget_9)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setStyleSheet(u"border: 1px solid;\n"
"border-radius:20px;\n"
"padding: 10px;\n"
"box-shadow: 10px 10px 28px 0px #888888;\n"
"background-color: rgb(0, 0, 0);")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.gridLayout_16 = QGridLayout(self.frame_5)
        self.gridLayout_16.setObjectName(u"gridLayout_16")
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_13 = QLabel(self.frame_5)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setFont(font2)
        self.label_13.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"")
        self.label_13.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.label_13)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_14 = QLabel(self.frame_5)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setFont(font4)
        self.label_14.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout.addWidget(self.label_14)

        self.label_15 = QLabel(self.frame_5)
        self.label_15.setObjectName(u"label_15")
        font5 = QFont()
        font5.setPointSize(50)
        font5.setBold(True)
        font5.setWeight(75)
        self.label_15.setFont(font5)
        self.label_15.setStyleSheet(u"color: rgb(26, 95, 180);\n"
"border-color: rgb(38, 162, 105);")
        self.label_15.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.label_15)


        self.verticalLayout_5.addLayout(self.horizontalLayout)


        self.gridLayout_16.addLayout(self.verticalLayout_5, 0, 0, 1, 1)


        self.gridLayout_15.addWidget(self.frame_5, 1, 0, 1, 1)


        self.gridLayout_13.addWidget(self.widget_9, 0, 0, 1, 2)

        self.stackedWidget.addWidget(self.page)
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.gridLayout_17 = QGridLayout(self.page_4)
        self.gridLayout_17.setObjectName(u"gridLayout_17")
        self.widget_10 = QWidget(self.page_4)
        self.widget_10.setObjectName(u"widget_10")
        self.gridLayout_18 = QGridLayout(self.widget_10)
        self.gridLayout_18.setObjectName(u"gridLayout_18")
        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_16 = QLabel(self.widget_10)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setFont(font1)
        self.label_16.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_6.addWidget(self.label_16)

        self.label_17 = QLabel(self.widget_10)
        self.label_17.setObjectName(u"label_17")
        font6 = QFont()
        font6.setPointSize(9)
        font6.setBold(False)
        font6.setWeight(50)
        self.label_17.setFont(font6)
        self.label_17.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_6.addWidget(self.label_17)

        self.verticalSpacer_9 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer_9)


        self.verticalLayout_8.addLayout(self.verticalLayout_6)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_18 = QLabel(self.widget_10)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_6.addWidget(self.label_18)

        self.lineEdit = QLineEdit(self.widget_10)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.horizontalLayout_6.addWidget(self.lineEdit)


        self.verticalLayout_8.addLayout(self.horizontalLayout_6)

        self.verticalSpacer_8 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_8.addItem(self.verticalSpacer_8)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_19 = QLabel(self.widget_10)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_7.addWidget(self.label_19)

        self.textEdit_3 = QTextEdit(self.widget_10)
        self.textEdit_3.setObjectName(u"textEdit_3")
        self.textEdit_3.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.horizontalLayout_7.addWidget(self.textEdit_3)


        self.verticalLayout_8.addLayout(self.horizontalLayout_7)

        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_8.addItem(self.verticalSpacer_7)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_24 = QLabel(self.widget_10)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_8.addWidget(self.label_24)

        self.textEdit_4 = QTextEdit(self.widget_10)
        self.textEdit_4.setObjectName(u"textEdit_4")
        self.textEdit_4.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.horizontalLayout_8.addWidget(self.textEdit_4)


        self.verticalLayout_8.addLayout(self.horizontalLayout_8)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_8.addItem(self.verticalSpacer_6)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_25 = QLabel(self.widget_10)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_9.addWidget(self.label_25)

        self.textEdit_5 = QTextEdit(self.widget_10)
        self.textEdit_5.setObjectName(u"textEdit_5")
        self.textEdit_5.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.horizontalLayout_9.addWidget(self.textEdit_5)


        self.verticalLayout_8.addLayout(self.horizontalLayout_9)

        self.verticalSpacer_11 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_8.addItem(self.verticalSpacer_11)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_21 = QLabel(self.widget_10)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_10.addWidget(self.label_21)

        self.label_23 = QLabel(self.widget_10)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setFont(font)
        self.label_23.setStyleSheet(u"color: rgb(26, 95, 180);")

        self.horizontalLayout_10.addWidget(self.label_23)


        self.verticalLayout_8.addLayout(self.horizontalLayout_10)

        self.verticalSpacer_12 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_8.addItem(self.verticalSpacer_12)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.pushButton_20 = QPushButton(self.widget_10)
        self.pushButton_20.setObjectName(u"pushButton_20")
        font7 = QFont()
        font7.setBold(True)
        font7.setWeight(75)
        self.pushButton_20.setFont(font7)
        self.pushButton_20.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(224, 27, 36);")

        self.horizontalLayout_5.addWidget(self.pushButton_20)

        self.pushButton_18 = QPushButton(self.widget_10)
        self.pushButton_18.setObjectName(u"pushButton_18")
        self.pushButton_18.setFont(font7)
        self.pushButton_18.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(26, 95, 180);")

        self.horizontalLayout_5.addWidget(self.pushButton_18)


        self.verticalLayout_8.addLayout(self.horizontalLayout_5)


        self.gridLayout_18.addLayout(self.verticalLayout_8, 0, 0, 1, 1)

        self.verticalSpacer_13 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_18.addItem(self.verticalSpacer_13, 1, 0, 1, 1)


        self.gridLayout_17.addWidget(self.widget_10, 1, 0, 1, 1)

        self.verticalSpacer_10 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_17.addItem(self.verticalSpacer_10, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.page_4)

        self.gridLayout_19.addWidget(self.stackedWidget, 1, 0, 1, 1)


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

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"FORENSIC VOICE COMPARISON TOOL ", None))
        self.label_7.setText("")
        self.pushButton_17.setText(QCoreApplication.translate("MainWindow", u"voice upload", None))
        self.pushButton_19.setText(QCoreApplication.translate("MainWindow", u"voice filter", None))
        self.pushButton_22.setText(QCoreApplication.translate("MainWindow", u"voice comparison", None))
        self.pushButton_23.setText(QCoreApplication.translate("MainWindow", u"genarate report", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"WELCOME TO FORENSIC VOICE COMPARISON TOOL", None))
        self.pushButton_24.setText(QCoreApplication.translate("MainWindow", u"SINGLE SPEAKER", None))
        self.pushButton_25.setText(QCoreApplication.translate("MainWindow", u"MULTSPEAKER", None))
        self.pushButton_26.setText(QCoreApplication.translate("MainWindow", u"UPLOAD FILE", None))
        self.pushButton_27.setText(QCoreApplication.translate("MainWindow", u"PLAY", None))
        self.pushButton_28.setText(QCoreApplication.translate("MainWindow", u"PAUSE", None))
        self.pushButton_29.setText(QCoreApplication.translate("MainWindow", u"TRIM", None))
        self.pushButton_30.setText(QCoreApplication.translate("MainWindow", u"NEXT", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"UPLOAD VOICE CLIPS", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Crime Voice", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"upload file", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Suspect Voice", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"upload file", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"SUBMIT", None))
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
        self.pushButton_16.setText(QCoreApplication.translate("MainWindow", u"GENARATE REPORT", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"VOICE COMPARISON RESULTS", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Likelihood Ratios", None))
        self.label_15.setText("")
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Fill the form below to genarate a full Report about the Voice Analysis", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"The information inserted in the form below will be submitted to the Court for further decisions", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Supect name", None))
        self.lineEdit.setText("")
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"About the case", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"Forensic Investigator Comment", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"Provide a short summary about result", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"Results", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"0.98", None))
        self.pushButton_20.setText(QCoreApplication.translate("MainWindow", u"BACK", None))
        self.pushButton_18.setText(QCoreApplication.translate("MainWindow", u"SAVE", None))
    # retranslateUi

