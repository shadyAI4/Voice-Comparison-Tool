# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'loader_dialog.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(427, 359)
        self.circularProgressBarBase = QFrame(Dialog)
        self.circularProgressBarBase.setObjectName(u"circularProgressBarBase")
        self.circularProgressBarBase.setGeometry(QRect(60, 20, 320, 320))
        self.circularProgressBarBase.setFrameShape(QFrame.NoFrame)
        self.circularProgressBarBase.setFrameShadow(QFrame.Raised)
        self.circularProgress_2 = QFrame(self.circularProgressBarBase)
        self.circularProgress_2.setObjectName(u"circularProgress_2")
        self.circularProgress_2.setGeometry(QRect(10, 10, 300, 300))
        self.circularProgress_2.setStyleSheet(u"QFrame{\n"
"	border-radius: 150px;\n"
"	background-color: qconicalgradient(cx:0.5, cy:0.5, angle:90, stop:0.749 rgba(255, 0, 127, 0), stop:0.750 rgba(85, 170, 255, 255));\n"
"}")
        self.circularProgress_2.setFrameShape(QFrame.NoFrame)
        self.circularProgress_2.setFrameShadow(QFrame.Raised)
        self.circularBg_2 = QFrame(self.circularProgressBarBase)
        self.circularBg_2.setObjectName(u"circularBg_2")
        self.circularBg_2.setGeometry(QRect(10, 10, 300, 300))
        self.circularBg_2.setStyleSheet(u"QFrame{\n"
"	border-radius: 150px;\n"
"	background-color: rgba(77, 77, 127, 120);\n"
"}")
        self.circularBg_2.setFrameShape(QFrame.NoFrame)
        self.circularBg_2.setFrameShadow(QFrame.Raised)
        self.container_2 = QFrame(self.circularProgressBarBase)
        self.container_2.setObjectName(u"container_2")
        self.container_2.setGeometry(QRect(25, 25, 270, 270))
        self.container_2.setStyleSheet(u"QFrame{\n"
"	border-radius: 135px;\n"
"	background-color: rgb(77, 77, 127);\n"
"}")
        self.container_2.setFrameShape(QFrame.NoFrame)
        self.container_2.setFrameShadow(QFrame.Raised)
        self.layoutWidget_2 = QWidget(self.container_2)
        self.layoutWidget_2.setObjectName(u"layoutWidget_2")
        self.layoutWidget_2.setGeometry(QRect(40, 50, 213, 191))
        self.gridLayout_2 = QGridLayout(self.layoutWidget_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.labelLoadingInfo_2 = QLabel(self.layoutWidget_2)
        self.labelLoadingInfo_2.setObjectName(u"labelLoadingInfo_2")
        self.labelLoadingInfo_2.setMinimumSize(QSize(0, 20))
        self.labelLoadingInfo_2.setMaximumSize(QSize(16777215, 20))
        font = QFont()
        font.setFamily(u"Segoe UI")
        font.setPointSize(9)
        self.labelLoadingInfo_2.setFont(font)
        self.labelLoadingInfo_2.setStyleSheet(u"QLabel{\n"
"	border-radius: 10px;	\n"
"	background-color: rgb(93, 93, 154);\n"
"	color: #FFFFFF;\n"
"	margin-left: 40px;\n"
"	margin-right: 40px;\n"
"}")
        self.labelLoadingInfo_2.setFrameShape(QFrame.NoFrame)
        self.labelLoadingInfo_2.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.labelLoadingInfo_2, 1, 0, 1, 1)

        self.labelPercentage_2 = QLabel(self.layoutWidget_2)
        self.labelPercentage_2.setObjectName(u"labelPercentage_2")
        font1 = QFont()
        font1.setFamily(u"Roboto Thin")
        font1.setPointSize(68)
        self.labelPercentage_2.setFont(font1)
        self.labelPercentage_2.setStyleSheet(u"background-color: none;\n"
"color: #FFFFFF")
        self.labelPercentage_2.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.labelPercentage_2, 0, 0, 1, 1)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.labelLoadingInfo_2.setText(QCoreApplication.translate("Dialog", u"please wait...", None))
        self.labelPercentage_2.setText(QCoreApplication.translate("Dialog", u"<p><span style=\" font-size:68pt;\">0</span><span style=\" font-size:58pt; vertical-align:super;\">%</span></p>", None))
    # retranslateUi

