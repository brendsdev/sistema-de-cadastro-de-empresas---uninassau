from os import access
from PySide6.QtWidgets import(QApplication,QMainWindow, QMessageBox, QWidget)
from PySide6.QtCore import Qt, QSize
from ui_login import Ui_Login
from ui_main import Ui_MainWindow
import sys
from database import DataBase
from ui_funtions import consulta_cnpj


class Login(QWidget, Ui_Login):
    def __init__(self) -> None:
        super(Login, self).__init__()
        self.tentativas = 0
        self.setupUi(self)
        self.setWindowTitle("Login do Sistema")

        self.btn_login.clicked.connect(self.checkLogin)

    def checkLogin(self):

        self.users = DataBase()
        self.users.conecta()
        autenticado = self.users.check_user(self.txt_user.text().upper(), self.txT_password.text())

        if autenticado.lower() == "administrador" or autenticado.lower() == "user":

            self.w = MainWindow(self.txt_user.text(), autenticado.lower())
            self.w.show()
            self.close()
        else:

            if self.tentativas < 3:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Warning)
                msg.setWindowTitle("Erro ao acessar")
                msg.setText(f'Login ou senha incorreto \n \n Tentativa: {self.tentativas + 1} de 3')
                msg.exec()
                self.tentativas += 1
            if self.tentativas == 3:
                # bloquear o usuário
                self.users.close_connection()
                sys.exit(0)



class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, user_text, autenticado_lower):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Sistema de Gerenciamento")

        self.setFixedSize(QSize(1000,650))


#     ******************PAGINAS DO SISTEMA***********************************************
        self.btn_home.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pg_home))
        self.btn_menu_cadastrar.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pg_cadastro))
        self.btn_pg_caduser.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pg_cadastro))
        self.btn_menu_sobre.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pg_sobre))
        self.btn_menu_contatos.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pg_contatos))

        self.btn_cadastre_usuario.clicked.connect(self.subscribe_user)

        # PREENCHER AUTOMATICAMENTE OS DADOS DO CNPJ
        self.txt_cnpj.editingFinished.connect(self.consult_api)
        ###############################################################################################

        self.btn_cadastrar_empresa.clicked.connect(self.cadastrar_empresas)
    def subscribe_user(self):

        if self.txt_senha.text() != self.txt_senha_2.text():
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setWindowTitle("Senhas divirgentes")
            msg.setText("A senha não é igual!")
            msg.exec_()
            return None

        nome = self.txt_nome.text()
        user = self.txt_usuario.text()
        password = self.txt_senha.text()
        access = self.cb_perfil.currentText()

        db = DataBase()
        db.conecta()
        db.insert_user(nome, user, password, access)
        db.close_connection()

        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("Cadastro de usuário")
        msg.setText("Cadastro realizado com sucesso!")
        msg.exec()

        self.txt_nome.setText("")
        self.txt_usuario.setText("")
        self.txt_senha.setText("")
        self.txt_senha_2.setText("")

    def consult_api(self):
        campos = consulta_cnpj(self.txt_cnpj.text())

        self.txt_nome_empresarial.setText(campos[0])
        self.txt_logradouro.setText(campos[1])
        self.txt_numero.setText(campos[2])
        self.txt_complemento.setText(campos[3])
        self.txt_bairro.setText(campos[4])
        self.txt_municipio.setText(campos[5])
        self.txt_uf.setText(campos[6])
        self.txt_cep.setText(campos[7].replace('.', '').replace('-',''))
        self.txt_telefone.setText(campos[8].replace('(','').replace('-','').replace(')',''))
        self.txt_email.setText(campos[9])

    def cadastrar_empresas(self):
        db = DataBase()
        db.conecta()

        fullDataSet = (

            self.txt_cnpj.text(), self.txt_nome_empresarial.text(), self.txt_logradouro.text(), self.txt_numero.text(),
            self.txt_complemento.text(), self.txt_bairro.text(), self.txt_municipio.text(), self.txt_uf.text(),
            self.txt_cep.text(), self.txt_telefone.text().strip(), self.txt_email.text()
        )

        #CADASTRAR NO BANCO DE DADOS
        resp = db.register_company(fullDataSet)

        if resp == "OK":
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setWindowTitle("Casdastro Realizado")
            msg.setText("Cadastro Realizado com sucesso")
            msg.exec()
            db.close_connection()
            return
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setWindowTitle("Erro")
            msg.setText("Erro ao cadastrar, verifique se as informações foram preenchidadas corretamente!")
            msg.exec()
            db.close_connection()
            return

if __name__ == "__main__":


    db = DataBase()
    db.conecta()
    db.create_table_company()
    db.close_connection()

    app = QApplication(sys.argv)
    window = Login()
    window.show()
    app.exec()