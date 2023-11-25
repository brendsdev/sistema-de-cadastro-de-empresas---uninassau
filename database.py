import sqlite3
class DataBase():
    def __init__(self, name = "system.db") -> None:
        self.name = name
    def conecta(self):
        self.connection = sqlite3.connect(self.name)

    def close_connection(self):
        try:
            self.connection.close()
        except:
            pass
    def create_table_users(self):
        try:
            cursor = self.connection.cursor()
            cursor.execute("""

                CREATE TABLE IF NOT EXISTS users(

                    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    user TEXT UNIQUE NOT NULL,
                    password TEXT NOT NULL,
                    access TEXT NOT NULL

                );

            """)
        except AttributeError:
            print("faça a conexão")
    def insert_user(self, name, user, password, access):

        try:

            cursor = self.connection.cursor()
            cursor.execute("""
    
                INSERT INTO users(name, user, password, access) VALUES(?,?,?,?)
    
            """, (name, user, password, access))
            self.connection.commit()

        except AttributeError:
            print("faça a conexão")
    def check_user(self, user, password):

        try:
            cursor = self.connection.cursor()
            cursor.execute("""

                SELECT * FROM users;

            """)

            for linha in cursor.fetchall():
                if linha[2].upper() == user.upper() and linha[3] == password and linha[4] == "Administrador":
                    return "Administrador"


                elif linha[2].upper() == user.upper() and linha[3] == password and linha[4] == "Usuário":
                    return "user"

                else:
                    continue
            return "sem acesso"
        except:
            pass

    def register_company(self, fullDataSet):

        campos_tabela = ('CNPJ','NOME','LOGRADOURO','NUMERO','COMPLEMENTO','BAIRRO','MUNICIPIO',
        'UF','CEP','TELEFONE','EMAIL')

        qntd = ("?,?,?,?,?,?,?,?,?,?,?")
        cursor = self.connection.cursor()

        try:
            cursor.execute(f"""INSERT INTO Empresas {campos_tabela}
            VALUES({qntd})""", fullDataSet)
            self.connection.commit()
            return("OK")

        except:
            return "Erro"

    def create_table_company(self):
        cursor = self.connection.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Empresas(

            CNPJ TEXT,
            NOME TEXT,
            LOGRADOURO TEXT,
            NUMERO TEXT,
            COMPLEMENTO TEXT,
            BAIRRO TEXT,
            MUNICIPIO TEXT,
            UF TEXT,
            CEP TEXT,
            TELEFONE TEXT,
            EMAIL TEXT,

            PRIMARY KEY(CNPJ)
            );




        """)





if __name__ == "__main__":

    db = DataBase()
    db.conecta()
    db.create_table_users()
    db.close_connection()