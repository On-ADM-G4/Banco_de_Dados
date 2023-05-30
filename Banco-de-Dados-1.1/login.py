class User():

    def __init__(self):
        
        import mysql.connector as conector

        try:

            conexao = conector.connect(
                host= 'localhost',
                database= 'db_property',
                user= 'root',
                password= 'root'
            )  

            if conexao.is_connected:

                print('\n# CONECTADO AO BANCO #')
                self.cursor = conexao.cursor()
                self.logar()

        except:
            print('\n# OCORREU UM ERRO AO SE CONECTAR COM O BANCO DE DADOS #')

    def logar(self):

        try:
            rec_user = str(input('\nDIGITE SEU LOGIN: '))
            rec_pass = int(input('\nDIGITE SUA SENHA: '))
            
            rec_senha = f'''SELECT SENHA FROM db_property.tb_login WHERE USUARIO = '{rec_user}';'''
            self.cursor.execute(rec_senha)
            resul = self.cursor.fetchall()

            if resul[0][0] == rec_pass:
                print('\n# LOGIN EFETUADO COM SUCESSO #')
            if resul[0][0] != rec_pass:
                print('\n# USUÁRIO OU SENHA NÃO EXISTE #')
                self.logar()
        except:
            print('\n# [ERROR] TENTE NOVAMENTE #')
            self.logar()