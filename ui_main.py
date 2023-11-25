# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'cadastro.ui'
##
## Created by: Qt User Interface Compiler version 6.5.3
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QSpacerItem, QStackedWidget,
    QTabWidget, QToolBox, QVBoxLayout, QWidget)
import icons_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(986, 645)
        MainWindow.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"*{\n"
"	border:none;\n"
"\n"
"}\n"
"\n"
"QLabel{\n"
"color: rgb(255, 255, 255);\n"
"\n"
"}")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, -1, 0, 9)
        self.left_Menu = QFrame(self.centralwidget)
        self.left_Menu.setObjectName(u"left_Menu")
        self.left_Menu.setMaximumSize(QSize(200, 16777215))
        self.left_Menu.setFrameShape(QFrame.StyledPanel)
        self.left_Menu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.left_Menu)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(-1, -1, 0, -1)
        self.frame = QFrame(self.left_Menu)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(-1, -1, 0, -1)
        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"color: rgb(255, 252, 210);")

        self.horizontalLayout_4.addWidget(self.label_3)


        self.verticalLayout_2.addWidget(self.frame)

        self.frame_2 = QFrame(self.left_Menu)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"QFrame{\n"
"background-color: rgb(45, 45, 45);\n"
"}\n"
"\n"
"QToolBox{\n"
"\n"
"	text-align:left;\n"
"	background-color: rgb(45, 45, 45);\n"
"\n"
"}\n"
"\n"
"QToolBox::tab{\n"
"	border-radius: Spx;\n"
"	\n"
"	\n"
"	background-color: rgb(81, 81, 81);\n"
"	text-align:left;\n"
"\n"
"}")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(-1, 0, 0, 0)
        self.toolBox = QToolBox(self.frame_2)
        self.toolBox.setObjectName(u"toolBox")
        self.toolBox.setMinimumSize(QSize(0, 30))
        self.toolBox.setStyleSheet(u"QPushButton:hover{\n"
"	\n"
"	background-color: rgb(85, 85, 85);\n"
"	border-top-left-radius: 15px\n"
"\n"
"}\n"
"\n"
"QPushButton{\n"
"\n"
"	\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.page.setGeometry(QRect(0, 0, 178, 502))
        self.verticalLayout_4 = QVBoxLayout(self.page)
        self.verticalLayout_4.setSpacing(6)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.btn_home = QPushButton(self.page)
        self.btn_home.setObjectName(u"btn_home")
        self.btn_home.setMinimumSize(QSize(0, 30))
        font = QFont()
        font.setPointSize(11)
        self.btn_home.setFont(font)
        self.btn_home.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_home.setStyleSheet(u"color: rgb(255, 252, 210);")

        self.verticalLayout_4.addWidget(self.btn_home)

        self.btn_menu_cadastrar = QPushButton(self.page)
        self.btn_menu_cadastrar.setObjectName(u"btn_menu_cadastrar")
        self.btn_menu_cadastrar.setMinimumSize(QSize(0, 30))
        self.btn_menu_cadastrar.setFont(font)
        self.btn_menu_cadastrar.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_menu_cadastrar.setStyleSheet(u"color: rgb(255, 252, 210);")

        self.verticalLayout_4.addWidget(self.btn_menu_cadastrar)

        self.btn_menu_contatos = QPushButton(self.page)
        self.btn_menu_contatos.setObjectName(u"btn_menu_contatos")
        self.btn_menu_contatos.setMinimumSize(QSize(0, 30))
        self.btn_menu_contatos.setFont(font)
        self.btn_menu_contatos.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_menu_contatos.setStyleSheet(u"color: rgb(255, 252, 210);")

        self.verticalLayout_4.addWidget(self.btn_menu_contatos)

        self.btn_menu_sobre = QPushButton(self.page)
        self.btn_menu_sobre.setObjectName(u"btn_menu_sobre")
        self.btn_menu_sobre.setMinimumSize(QSize(0, 30))
        self.btn_menu_sobre.setFont(font)
        self.btn_menu_sobre.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_menu_sobre.setStyleSheet(u"color: rgb(255, 252, 210);")

        self.verticalLayout_4.addWidget(self.btn_menu_sobre)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer)

        self.toolBox.addItem(self.page, u"Page 1")
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.page_2.setGeometry(QRect(0, 0, 178, 502))
        self.horizontalLayout_5 = QHBoxLayout(self.page_2)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(-1, -1, 0, -1)
        self.label_4 = QLabel(self.page_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setStyleSheet(u"color: rgb(255, 252, 210);")

        self.horizontalLayout_5.addWidget(self.label_4)

        self.toolBox.addItem(self.page_2, u"Page 2")

        self.verticalLayout_3.addWidget(self.toolBox)


        self.verticalLayout_2.addWidget(self.frame_2)


        self.horizontalLayout.addWidget(self.left_Menu)

        self.main_container = QFrame(self.centralwidget)
        self.main_container.setObjectName(u"main_container")
        self.main_container.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.main_container.setFrameShape(QFrame.StyledPanel)
        self.main_container.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.main_container)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.top_frame = QFrame(self.main_container)
        self.top_frame.setObjectName(u"top_frame")
        self.top_frame.setMaximumSize(QSize(550, 16777215))
        self.top_frame.setFrameShape(QFrame.StyledPanel)
        self.top_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.top_frame)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.btn_toggle = QPushButton(self.top_frame)
        self.btn_toggle.setObjectName(u"btn_toggle")
        self.btn_toggle.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_toggle.setStyleSheet(u"color: rgb(255, 255, 255);")
        icon = QIcon()
        icon.addFile(u":/icons/icons/menu2.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_toggle.setIcon(icon)
        self.btn_toggle.setIconSize(QSize(32, 32))

        self.horizontalLayout_3.addWidget(self.btn_toggle, 0, Qt.AlignLeft)


        self.verticalLayout.addWidget(self.top_frame)

        self.main_frame = QFrame(self.main_container)
        self.main_frame.setObjectName(u"main_frame")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.main_frame.sizePolicy().hasHeightForWidth())
        self.main_frame.setSizePolicy(sizePolicy)
        self.main_frame.setFrameShape(QFrame.StyledPanel)
        self.main_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.main_frame)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.Pages = QStackedWidget(self.main_frame)
        self.Pages.setObjectName(u"Pages")
        self.Pages.setStyleSheet(u"color: rgb(255, 252, 210);")
        self.pg_home = QWidget()
        self.pg_home.setObjectName(u"pg_home")
        self.verticalLayout_8 = QVBoxLayout(self.pg_home)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.logo = QLabel(self.pg_home)
        self.logo.setObjectName(u"logo")
        self.logo.setMinimumSize(QSize(500, 500))
        self.logo.setScaledContents(False)
        self.logo.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.logo)

        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.label_23 = QLabel(self.pg_home)
        self.label_23.setObjectName(u"label_23")

        self.horizontalLayout_16.addWidget(self.label_23)

        self.btn_pg_caduser = QPushButton(self.pg_home)
        self.btn_pg_caduser.setObjectName(u"btn_pg_caduser")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.btn_pg_caduser.sizePolicy().hasHeightForWidth())
        self.btn_pg_caduser.setSizePolicy(sizePolicy1)
        self.btn_pg_caduser.setMinimumSize(QSize(100, 30))
        self.btn_pg_caduser.setMaximumSize(QSize(300, 100))
        font1 = QFont()
        font1.setPointSize(13)
        self.btn_pg_caduser.setFont(font1)
        self.btn_pg_caduser.setStyleSheet(u"QPushButton{\n"
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

        self.horizontalLayout_16.addWidget(self.btn_pg_caduser)

        self.label_24 = QLabel(self.pg_home)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setMaximumSize(QSize(1100, 16777215))

        self.horizontalLayout_16.addWidget(self.label_24)


        self.verticalLayout_6.addLayout(self.horizontalLayout_16)


        self.verticalLayout_8.addLayout(self.verticalLayout_6)

        self.Pages.addWidget(self.pg_home)
        self.pg_cadastro = QWidget()
        self.pg_cadastro.setObjectName(u"pg_cadastro")
        self.verticalLayout_7 = QVBoxLayout(self.pg_cadastro)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.tb_cadastros = QTabWidget(self.pg_cadastro)
        self.tb_cadastros.setObjectName(u"tb_cadastros")
        self.tb_cadastros.setCursor(QCursor(Qt.ArrowCursor))
        self.tb_cadastros.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.tb_empresas = QWidget()
        self.tb_empresas.setObjectName(u"tb_empresas")
        self.label_8 = QLabel(self.tb_empresas)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(40, 10, 711, 31))
        self.label_8.setMinimumSize(QSize(0, 30))
        self.label_8.setMaximumSize(QSize(16777215, 50))
        self.label_8.setStyleSheet(u"color: rgb(255, 252, 210);\n"
"background-color: rgb(27, 27, 27);\n"
"")
        self.layoutWidget = QWidget(self.tb_empresas)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(21, 58, 731, 401))
        self.verticalLayout_10 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.frame_4 = QFrame(self.layoutWidget)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame_4)
        self.gridLayout.setObjectName(u"gridLayout")
        self.txt_cnpj = QLineEdit(self.frame_4)
        self.txt_cnpj.setObjectName(u"txt_cnpj")
        font2 = QFont()
        font2.setPointSize(12)
        self.txt_cnpj.setFont(font2)
        self.txt_cnpj.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.txt_cnpj.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.txt_cnpj, 0, 0, 1, 1)

        self.txt_nome_empresarial = QLineEdit(self.frame_4)
        self.txt_nome_empresarial.setObjectName(u"txt_nome_empresarial")
        self.txt_nome_empresarial.setFont(font2)
        self.txt_nome_empresarial.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.txt_nome_empresarial.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.txt_nome_empresarial, 0, 1, 1, 2)

        self.txt_logradouro = QLineEdit(self.frame_4)
        self.txt_logradouro.setObjectName(u"txt_logradouro")
        self.txt_logradouro.setFont(font2)
        self.txt_logradouro.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.txt_logradouro.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.txt_logradouro, 1, 0, 1, 3)

        self.txt_numero = QLineEdit(self.frame_4)
        self.txt_numero.setObjectName(u"txt_numero")
        self.txt_numero.setFont(font2)
        self.txt_numero.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.txt_numero.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.txt_numero, 2, 0, 1, 1)

        self.txt_complemento = QLineEdit(self.frame_4)
        self.txt_complemento.setObjectName(u"txt_complemento")
        self.txt_complemento.setFont(font2)
        self.txt_complemento.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.txt_complemento.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.txt_complemento, 2, 1, 1, 1)

        self.txt_bairro = QLineEdit(self.frame_4)
        self.txt_bairro.setObjectName(u"txt_bairro")
        self.txt_bairro.setFont(font2)
        self.txt_bairro.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.txt_bairro.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.txt_bairro, 2, 2, 1, 1)

        self.txt_municipio = QLineEdit(self.frame_4)
        self.txt_municipio.setObjectName(u"txt_municipio")
        self.txt_municipio.setFont(font2)
        self.txt_municipio.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.txt_municipio.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.txt_municipio, 3, 0, 1, 1)

        self.txt_uf = QLineEdit(self.frame_4)
        self.txt_uf.setObjectName(u"txt_uf")
        self.txt_uf.setFont(font2)
        self.txt_uf.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.txt_uf.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.txt_uf, 3, 1, 1, 1)

        self.txt_cep = QLineEdit(self.frame_4)
        self.txt_cep.setObjectName(u"txt_cep")
        self.txt_cep.setFont(font2)
        self.txt_cep.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.txt_cep.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.txt_cep, 3, 2, 1, 1)

        self.txt_telefone = QLineEdit(self.frame_4)
        self.txt_telefone.setObjectName(u"txt_telefone")
        self.txt_telefone.setFont(font2)
        self.txt_telefone.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.txt_telefone.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.txt_telefone, 4, 0, 1, 1)

        self.txt_email = QLineEdit(self.frame_4)
        self.txt_email.setObjectName(u"txt_email")
        self.txt_email.setFont(font2)
        self.txt_email.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.txt_email.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.txt_email, 4, 1, 1, 2)


        self.verticalLayout_10.addWidget(self.frame_4)

        self.layoutWidget1 = QWidget(self.tb_empresas)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(20, 470, 731, 27))
        self.horizontalLayout_17 = QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.label_25 = QLabel(self.layoutWidget1)
        self.label_25.setObjectName(u"label_25")

        self.horizontalLayout_17.addWidget(self.label_25)

        self.btn_cadastrar_empresa = QPushButton(self.layoutWidget1)
        self.btn_cadastrar_empresa.setObjectName(u"btn_cadastrar_empresa")
        self.btn_cadastrar_empresa.setMinimumSize(QSize(0, 25))
        self.btn_cadastrar_empresa.setFont(font2)
        self.btn_cadastrar_empresa.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_cadastrar_empresa.setStyleSheet(u"QPushButton{\n"
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

        self.horizontalLayout_17.addWidget(self.btn_cadastrar_empresa)

        self.label_26 = QLabel(self.layoutWidget1)
        self.label_26.setObjectName(u"label_26")

        self.horizontalLayout_17.addWidget(self.label_26)

        self.tb_cadastros.addTab(self.tb_empresas, "")
        self.tb_usuario = QWidget()
        self.tb_usuario.setObjectName(u"tb_usuario")
        self.frame_3 = QFrame(self.tb_usuario)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(10, 80, 731, 341))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_3)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_13 = QLabel(self.frame_3)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setMinimumSize(QSize(100, 0))
        self.label_13.setMaximumSize(QSize(100, 20))
        self.label_13.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.label_13.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_6.addWidget(self.label_13)

        self.txt_nome = QLineEdit(self.frame_3)
        self.txt_nome.setObjectName(u"txt_nome")
        font3 = QFont()
        font3.setPointSize(10)
        self.txt_nome.setFont(font3)
        self.txt_nome.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.horizontalLayout_6.addWidget(self.txt_nome)


        self.gridLayout_2.addLayout(self.horizontalLayout_6, 0, 0, 1, 1)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_14 = QLabel(self.frame_3)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setMinimumSize(QSize(100, 0))
        self.label_14.setMaximumSize(QSize(100, 20))
        self.label_14.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.label_14.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_7.addWidget(self.label_14)

        self.txt_usuario = QLineEdit(self.frame_3)
        self.txt_usuario.setObjectName(u"txt_usuario")
        self.txt_usuario.setFont(font3)
        self.txt_usuario.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.horizontalLayout_7.addWidget(self.txt_usuario)


        self.gridLayout_2.addLayout(self.horizontalLayout_7, 1, 0, 1, 1)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_15 = QLabel(self.frame_3)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setMinimumSize(QSize(100, 0))
        self.label_15.setMaximumSize(QSize(100, 20))
        self.label_15.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.label_15.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_8.addWidget(self.label_15)

        self.txt_senha = QLineEdit(self.frame_3)
        self.txt_senha.setObjectName(u"txt_senha")
        self.txt_senha.setFont(font3)
        self.txt_senha.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.txt_senha.setEchoMode(QLineEdit.Password)

        self.horizontalLayout_8.addWidget(self.txt_senha)


        self.gridLayout_2.addLayout(self.horizontalLayout_8, 2, 0, 1, 1)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_16 = QLabel(self.frame_3)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setMinimumSize(QSize(100, 0))
        self.label_16.setMaximumSize(QSize(100, 20))
        self.label_16.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.label_16.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_9.addWidget(self.label_16)

        self.txt_senha_2 = QLineEdit(self.frame_3)
        self.txt_senha_2.setObjectName(u"txt_senha_2")
        self.txt_senha_2.setFont(font3)
        self.txt_senha_2.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.txt_senha_2.setEchoMode(QLineEdit.Password)

        self.horizontalLayout_9.addWidget(self.txt_senha_2)


        self.gridLayout_2.addLayout(self.horizontalLayout_9, 3, 0, 1, 1)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_17 = QLabel(self.frame_3)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setMinimumSize(QSize(200, 0))
        self.label_17.setMaximumSize(QSize(100, 20))
        self.label_17.setFont(font3)
        self.label_17.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.label_17.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_10.addWidget(self.label_17)

        self.cb_perfil = QComboBox(self.frame_3)
        self.cb_perfil.addItem("")
        self.cb_perfil.addItem("")
        self.cb_perfil.setObjectName(u"cb_perfil")
        self.cb_perfil.setMaximumSize(QSize(200, 20))
        self.cb_perfil.setFont(font3)
        self.cb_perfil.setCursor(QCursor(Qt.PointingHandCursor))
        self.cb_perfil.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.horizontalLayout_10.addWidget(self.cb_perfil)


        self.gridLayout_2.addLayout(self.horizontalLayout_10, 4, 0, 1, 1)

        self.layoutWidget_7 = QWidget(self.tb_usuario)
        self.layoutWidget_7.setObjectName(u"layoutWidget_7")
        self.layoutWidget_7.setGeometry(QRect(20, 450, 721, 27))
        self.horizontalLayout_18 = QHBoxLayout(self.layoutWidget_7)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.label_27 = QLabel(self.layoutWidget_7)
        self.label_27.setObjectName(u"label_27")

        self.horizontalLayout_18.addWidget(self.label_27)

        self.btn_cadastre_usuario = QPushButton(self.layoutWidget_7)
        self.btn_cadastre_usuario.setObjectName(u"btn_cadastre_usuario")
        self.btn_cadastre_usuario.setMinimumSize(QSize(0, 25))
        self.btn_cadastre_usuario.setFont(font2)
        self.btn_cadastre_usuario.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_cadastre_usuario.setStyleSheet(u"QPushButton{\n"
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

        self.horizontalLayout_18.addWidget(self.btn_cadastre_usuario)

        self.label_28 = QLabel(self.layoutWidget_7)
        self.label_28.setObjectName(u"label_28")

        self.horizontalLayout_18.addWidget(self.label_28)

        self.label_6 = QLabel(self.tb_usuario)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(11, 21, 731, 30))
        self.label_6.setMinimumSize(QSize(0, 30))
        self.label_6.setStyleSheet(u"background-color: rgb(27, 27, 27);\n"
"color: rgb(255, 252, 210);")
        self.tb_cadastros.addTab(self.tb_usuario, "")

        self.verticalLayout_7.addWidget(self.tb_cadastros)

        self.Pages.addWidget(self.pg_cadastro)
        self.pg_contatos = QWidget()
        self.pg_contatos.setObjectName(u"pg_contatos")
        self.verticalLayout_11 = QVBoxLayout(self.pg_contatos)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.label_12 = QLabel(self.pg_contatos)
        self.label_12.setObjectName(u"label_12")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_12.sizePolicy().hasHeightForWidth())
        self.label_12.setSizePolicy(sizePolicy2)
        self.label_12.setMinimumSize(QSize(0, 20))
        self.label_12.setMaximumSize(QSize(16777215, 130))
        self.label_12.setStyleSheet(u"background-color: rgb(17, 17, 17);")

        self.verticalLayout_9.addWidget(self.label_12)

        self.label_5 = QLabel(self.pg_contatos)
        self.label_5.setObjectName(u"label_5")
        sizePolicy2.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy2)
        self.label_5.setMaximumSize(QSize(800, 90))
        self.label_5.setLayoutDirection(Qt.LeftToRight)

        self.verticalLayout_9.addWidget(self.label_5)

        self.label_7 = QLabel(self.pg_contatos)
        self.label_7.setObjectName(u"label_7")
        sizePolicy2.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy2)
        self.label_7.setMaximumSize(QSize(800, 90))

        self.verticalLayout_9.addWidget(self.label_7)

        self.label_9 = QLabel(self.pg_contatos)
        self.label_9.setObjectName(u"label_9")
        sizePolicy2.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy2)
        self.label_9.setMaximumSize(QSize(800, 90))

        self.verticalLayout_9.addWidget(self.label_9)


        self.verticalLayout_11.addLayout(self.verticalLayout_9)

        self.Pages.addWidget(self.pg_contatos)
        self.pg_sobre = QWidget()
        self.pg_sobre.setObjectName(u"pg_sobre")
        self.verticalLayout_12 = QVBoxLayout(self.pg_sobre)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.label_10 = QLabel(self.pg_sobre)
        self.label_10.setObjectName(u"label_10")

        self.verticalLayout_12.addWidget(self.label_10)

        self.label_11 = QLabel(self.pg_sobre)
        self.label_11.setObjectName(u"label_11")
        sizePolicy.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy)
        self.label_11.setWordWrap(True)

        self.verticalLayout_12.addWidget(self.label_11)

        self.Pages.addWidget(self.pg_sobre)

        self.verticalLayout_5.addWidget(self.Pages)


        self.verticalLayout.addWidget(self.main_frame)

        self.footer_frame = QFrame(self.main_container)
        self.footer_frame.setObjectName(u"footer_frame")
        self.footer_frame.setFrameShape(QFrame.StyledPanel)
        self.footer_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.footer_frame)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(-1, 0, 0, 0)
        self.label_2 = QLabel(self.footer_frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"color: rgb(255, 252, 210);")

        self.horizontalLayout_2.addWidget(self.label_2)


        self.verticalLayout.addWidget(self.footer_frame)


        self.horizontalLayout.addWidget(self.main_container)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.toolBox.setCurrentIndex(0)
        self.Pages.setCurrentIndex(0)
        self.tb_cadastros.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u00a9\ufe0f The Start Code", None))
        self.btn_home.setText(QCoreApplication.translate("MainWindow", u"HOME", None))
        self.btn_menu_cadastrar.setText(QCoreApplication.translate("MainWindow", u"CADASTRAR", None))
        self.btn_menu_contatos.setText(QCoreApplication.translate("MainWindow", u"CONTATOS", None))
        self.btn_menu_sobre.setText(QCoreApplication.translate("MainWindow", u"SOBRE", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page), QCoreApplication.translate("MainWindow", u"Page 1", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">Usu\u00e1rio: Brenda</p><p align=\"center\">Sistema: Cadastro</p><p align=\"center\">Status: Ativo</p><p align=\"center\">Vers\u00e3o: 2023</p></body></html>", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_2), QCoreApplication.translate("MainWindow", u"Page 2", None))
        self.btn_toggle.setText("")
        self.logo.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><img src=\":/icons/icons/logo4.png\"/></p></body></html>", None))
        self.label_23.setText("")
        self.btn_pg_caduser.setText(QCoreApplication.translate("MainWindow", u"CADASTRAR USU\u00c1RIO", None))
        self.label_24.setText("")
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; color:#ffffff;\">CADASTRAR EMPRESAS</span></p><p align=\"center\"><br/></p></body></html>", None))
        self.txt_cnpj.setPlaceholderText(QCoreApplication.translate("MainWindow", u"CNPJ", None))
        self.txt_nome_empresarial.setPlaceholderText(QCoreApplication.translate("MainWindow", u"NOME EMPRESARIAL", None))
        self.txt_logradouro.setPlaceholderText(QCoreApplication.translate("MainWindow", u"LOGRADOURO", None))
        self.txt_numero.setPlaceholderText(QCoreApplication.translate("MainWindow", u"N\u00daMERO", None))
        self.txt_complemento.setPlaceholderText(QCoreApplication.translate("MainWindow", u"COMPLEMENTO", None))
        self.txt_bairro.setPlaceholderText(QCoreApplication.translate("MainWindow", u"BAIRRO", None))
        self.txt_municipio.setPlaceholderText(QCoreApplication.translate("MainWindow", u"MUNICIPIO", None))
        self.txt_uf.setPlaceholderText(QCoreApplication.translate("MainWindow", u"UF", None))
        self.txt_cep.setPlaceholderText(QCoreApplication.translate("MainWindow", u"CEP", None))
        self.txt_telefone.setPlaceholderText(QCoreApplication.translate("MainWindow", u"TELEFONE", None))
        self.txt_email.setPlaceholderText(QCoreApplication.translate("MainWindow", u"E-MAIL", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.btn_cadastrar_empresa.setText(QCoreApplication.translate("MainWindow", u"CADASTRAR EMPRESA", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.tb_cadastros.setTabText(self.tb_cadastros.indexOf(self.tb_empresas), QCoreApplication.translate("MainWindow", u"EMPRESAS", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"NOME:", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"USU\u00c1RIO", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"SENHA", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"SENHA", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"PERFIL", None))
        self.cb_perfil.setItemText(0, QCoreApplication.translate("MainWindow", u"Usu\u00e1rio", None))
        self.cb_perfil.setItemText(1, QCoreApplication.translate("MainWindow", u"Administrador", None))

        self.label_27.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.btn_cadastre_usuario.setText(QCoreApplication.translate("MainWindow", u"CADASTRAR USU\u00c1RIO", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; color:#ffffff;\">CADASTRAR USU\u00c1RIO</span></p></body></html>", None))
        self.tb_cadastros.setTabText(self.tb_cadastros.indexOf(self.tb_usuario), QCoreApplication.translate("MainWindow", u"USU\u00c1RIO", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">CONTATOS</span></p></body></html>", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><br/></p><p align=\"center\">(79)99640-3658</p></body></html>", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><br/></p><p align=\"center\">@brends.s</p></body></html>", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><br/>brendsdev@gmail.com</p></body></html>", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">SOBRE</span></p></body></html>", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">Este sistema faz consulta do CNPJ utilizando API da receita federal e faz o cadastro em um banco de dados SQLITE3.</span></p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt;\">\u00a9\ufe0f The Start Code 2023</span></p></body></html>", None))
    # retranslateUi

