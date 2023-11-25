# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QWidget)
import icons

class Ui_Login(object):
    def setupUi(self, Login):
        if not Login.objectName():
            Login.setObjectName(u"Login")
        Login.resize(457, 564)
        Login.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.frame = QFrame(Login)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(50, 210, 361, 331))
        self.frame.setStyleSheet(u"background-color: rgba(29, 29, 29, 0.7);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.txt_user = QLineEdit(self.frame)
        self.txt_user.setObjectName(u"txt_user")
        self.txt_user.setGeometry(QRect(70, 70, 211, 31))
        font = QFont()
        font.setPointSize(10)
        self.txt_user.setFont(font)
        self.txt_user.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.txt_user.setAlignment(Qt.AlignCenter)
        self.txT_password = QLineEdit(self.frame)
        self.txT_password.setObjectName(u"txT_password")
        self.txT_password.setGeometry(QRect(70, 170, 211, 31))
        self.txT_password.setFont(font)
        self.txT_password.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.txT_password.setEchoMode(QLineEdit.Password)
        self.txT_password.setAlignment(Qt.AlignCenter)
        self.btn_login = QPushButton(self.frame)
        self.btn_login.setObjectName(u"btn_login")
        self.btn_login.setGeometry(QRect(110, 240, 141, 31))
        font1 = QFont()
        font1.setPointSize(11)
        self.btn_login.setFont(font1)
        self.btn_login.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_login.setStyleSheet(u"QPushButton{\n"
"\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(220, 112, 11);\n"
"	border-radius:10Px\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"\n"
"	color: rgb(0, 0, 0);\n"
"	background-color: rgb(255, 255, 255);\n"
"\n"
"}")
        self.label = QLabel(Login)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(110, 20, 221, 191))
        self.label.setPixmap(QPixmap(u"icons/logo4.png"))
        self.label.setScaledContents(True)
        self.label.raise_()
        self.frame.raise_()

        self.retranslateUi(Login)

        QMetaObject.connectSlotsByName(Login)
    # setupUi

    def retranslateUi(self, Login):
        Login.setWindowTitle(QCoreApplication.translate("Login", u"Form", None))
        self.txt_user.setPlaceholderText(QCoreApplication.translate("Login", u"USU\u00c1RIO", None))
        self.txT_password.setPlaceholderText(QCoreApplication.translate("Login", u"SENHA", None))
        self.btn_login.setText(QCoreApplication.translate("Login", u"LOGIN", None))
        self.label.setText("")
    # retranslateUi

