# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
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
        MainWindow.resize(1027, 599)
        MainWindow.setMinimumSize(QSize(1000, 500))
        MainWindow.setStyleSheet(u"background-color: rgb(45, 45, 45);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.Top_Bar = QFrame(self.centralwidget)
        self.Top_Bar.setObjectName(u"Top_Bar")
        self.Top_Bar.setMaximumSize(QSize(16777215, 40))
        self.Top_Bar.setStyleSheet(u"background-color: rgb(35, 35, 35);")
        self.Top_Bar.setFrameShape(QFrame.NoFrame)
        self.Top_Bar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.Top_Bar)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_toggle = QFrame(self.Top_Bar)
        self.frame_toggle.setObjectName(u"frame_toggle")
        self.frame_toggle.setMaximumSize(QSize(70, 40))
        self.frame_toggle.setStyleSheet(u"background-color: rgb(85, 170, 255);")
        self.frame_toggle.setFrameShape(QFrame.StyledPanel)
        self.frame_toggle.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_toggle)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout.addWidget(self.frame_toggle)

        self.frame_top = QFrame(self.Top_Bar)
        self.frame_top.setObjectName(u"frame_top")
        self.frame_top.setFrameShape(QFrame.StyledPanel)
        self.frame_top.setFrameShadow(QFrame.Raised)

        self.horizontalLayout.addWidget(self.frame_top)


        self.verticalLayout.addWidget(self.Top_Bar)

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
        self.frame_left_menu.setMinimumSize(QSize(250, 0))
        self.frame_left_menu.setMaximumSize(QSize(100, 16777215))
        self.frame_left_menu.setStyleSheet(u"background-color: rgb(35, 35, 35);")
        self.frame_left_menu.setFrameShape(QFrame.StyledPanel)
        self.frame_left_menu.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_left_menu)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_5 = QLabel(self.frame_left_menu)
        self.label_5.setObjectName(u"label_5")
        font = QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_4.addWidget(self.label_5)

        self.progressBar_2 = QProgressBar(self.frame_left_menu)
        self.progressBar_2.setObjectName(u"progressBar_2")
        self.progressBar_2.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.progressBar_2.setValue(24)

        self.horizontalLayout_4.addWidget(self.progressBar_2)


        self.gridLayout_2.addLayout(self.horizontalLayout_4, 4, 0, 1, 1)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_6 = QLabel(self.frame_left_menu)
        self.label_6.setObjectName(u"label_6")
        font1 = QFont()
        font1.setBold(True)
        font1.setWeight(75)
        self.label_6.setFont(font1)
        self.label_6.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_5.addWidget(self.label_6)

        self.progressBar_3 = QProgressBar(self.frame_left_menu)
        self.progressBar_3.setObjectName(u"progressBar_3")
        self.progressBar_3.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.progressBar_3.setValue(24)

        self.horizontalLayout_5.addWidget(self.progressBar_3)


        self.gridLayout_2.addLayout(self.horizontalLayout_5, 6, 0, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_2, 7, 0, 1, 1)

        self.frame_top_menus = QFrame(self.frame_left_menu)
        self.frame_top_menus.setObjectName(u"frame_top_menus")
        self.frame_top_menus.setFrameShape(QFrame.NoFrame)
        self.frame_top_menus.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_top_menus)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)

        self.gridLayout_2.addWidget(self.frame_top_menus, 10, 0, 1, 1)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_7 = QLabel(self.frame_left_menu)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font1)
        self.label_7.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_6.addWidget(self.label_7)

        self.progressBar_4 = QProgressBar(self.frame_left_menu)
        self.progressBar_4.setObjectName(u"progressBar_4")
        self.progressBar_4.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.progressBar_4.setValue(24)

        self.horizontalLayout_6.addWidget(self.progressBar_4)


        self.gridLayout_2.addLayout(self.horizontalLayout_6, 8, 0, 1, 1)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_4 = QLabel(self.frame_left_menu)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font)
        self.label_4.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_3.addWidget(self.label_4)

        self.progressBar = QProgressBar(self.frame_left_menu)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.progressBar.setValue(24)

        self.horizontalLayout_3.addWidget(self.progressBar)


        self.gridLayout_2.addLayout(self.horizontalLayout_3, 2, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer, 9, 0, 1, 1)

        self.label_3 = QLabel(self.frame_left_menu)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setPixmap(QPixmap(u":/images/emblem1.png"))

        self.gridLayout_2.addWidget(self.label_3, 0, 0, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_3, 5, 0, 1, 1)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_4, 3, 0, 1, 1)


        self.horizontalLayout_2.addWidget(self.frame_left_menu)

        self.frame_pages = QFrame(self.Content)
        self.frame_pages.setObjectName(u"frame_pages")
        self.frame_pages.setFrameShape(QFrame.StyledPanel)
        self.frame_pages.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame_pages)
        self.gridLayout.setObjectName(u"gridLayout")
        self.stackedWidget = QStackedWidget(self.frame_pages)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page_1 = QWidget()
        self.page_1.setObjectName(u"page_1")
        self.gridLayout_3 = QGridLayout(self.page_1)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.verticalSpacer_6 = QSpacerItem(20, 135, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer_6, 0, 2, 1, 2)

        self.horizontalSpacer_6 = QSpacerItem(209, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_6, 1, 0, 2, 2)

        self.label_8 = QLabel(self.page_1)
        self.label_8.setObjectName(u"label_8")
        font2 = QFont()
        font2.setPointSize(20)
        font2.setBold(True)
        font2.setWeight(75)
        self.label_8.setFont(font2)
        self.label_8.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout_3.addWidget(self.label_8, 1, 2, 2, 3)

        self.horizontalSpacer_7 = QSpacerItem(231, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_7, 1, 5, 2, 4)

        self.verticalSpacer_5 = QSpacerItem(20, 135, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer_5, 2, 3, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(203, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_2, 3, 0, 1, 1)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_9 = QLabel(self.page_1)
        self.label_9.setObjectName(u"label_9")
        font3 = QFont()
        font3.setPointSize(15)
        self.label_9.setFont(font3)
        self.label_9.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_7.addWidget(self.label_9)

        self.pushButton = QPushButton(self.page_1)
        self.pushButton.setObjectName(u"pushButton")
        font4 = QFont()
        font4.setPointSize(13)
        font4.setBold(True)
        font4.setWeight(75)
        self.pushButton.setFont(font4)
        self.pushButton.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(26, 95, 180);")

        self.horizontalLayout_7.addWidget(self.pushButton)


        self.gridLayout_3.addLayout(self.horizontalLayout_7, 3, 1, 1, 6)

        self.horizontalSpacer_4 = QSpacerItem(182, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_4, 3, 7, 1, 2)

        self.verticalSpacer_9 = QSpacerItem(20, 16, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer_9, 4, 4, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(203, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_3, 5, 0, 1, 1)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_10 = QLabel(self.page_1)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font3)
        self.label_10.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_8.addWidget(self.label_10)

        self.pushButton_2 = QPushButton(self.page_1)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setFont(font4)
        self.pushButton_2.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(26, 95, 180);")

        self.horizontalLayout_8.addWidget(self.pushButton_2)


        self.gridLayout_3.addLayout(self.horizontalLayout_8, 5, 1, 1, 6)

        self.horizontalSpacer_5 = QSpacerItem(182, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_5, 5, 7, 1, 2)

        self.verticalSpacer_7 = QSpacerItem(20, 105, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer_7, 6, 6, 1, 1)

        self.horizontalSpacer = QSpacerItem(502, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer, 7, 0, 1, 6)

        self.pushButton_3 = QPushButton(self.page_1)
        self.pushButton_3.setObjectName(u"pushButton_3")
        font5 = QFont()
        font5.setPointSize(15)
        font5.setBold(True)
        font5.setWeight(75)
        self.pushButton_3.setFont(font5)
        self.pushButton_3.setStyleSheet(u"color: rgb(246, 245, 244);")

        self.gridLayout_3.addWidget(self.pushButton_3, 7, 6, 1, 2)

        self.horizontalSpacer_8 = QSpacerItem(139, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_8, 7, 8, 1, 1)

        self.verticalSpacer_8 = QSpacerItem(20, 14, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer_8, 8, 7, 1, 1)

        self.stackedWidget.addWidget(self.page_1)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.verticalLayout_6 = QVBoxLayout(self.page_2)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_2 = QLabel(self.page_2)
        self.label_2.setObjectName(u"label_2")
        font6 = QFont()
        font6.setPointSize(40)
        self.label_2.setFont(font6)
        self.label_2.setStyleSheet(u"color: #FFF;")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.label_2)

        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.verticalLayout_8 = QVBoxLayout(self.page_3)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label = QLabel(self.page_3)
        self.label.setObjectName(u"label")
        self.label.setFont(font6)
        self.label.setStyleSheet(u"color: #FFF;")
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.label)

        self.stackedWidget.addWidget(self.page_3)

        self.gridLayout.addWidget(self.stackedWidget, 0, 0, 1, 1)


        self.horizontalLayout_2.addWidget(self.frame_pages)


        self.verticalLayout.addWidget(self.Content)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Voice Filter", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Voice Comparison", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Genate report", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Voice Upload", None))
        self.label_3.setText("")
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"UPLOAD VOICE CLIPS", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Suspect Voice : ", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"upload file", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Crime Voice : ", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"upload file", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"FILTER", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"PAGE 2", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"PAGE 3", None))
    # retranslateUi

