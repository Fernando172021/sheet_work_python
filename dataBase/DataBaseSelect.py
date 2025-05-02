from dataBase.DataBaseConfig import db_config
from logic.DataPerson import DataPerson
import pymysql


class DataBaseSelect:
    def __init__(self):
        con = pymysql.connect(
            host= db_config['host'],
            user= db_config['user'],
            password= db_config['password'],
            database= db_config['database'],
        )

        try:
            self.cursor = con.cursor()
            self.cursor.execute(self.select_data_user())
            con.commit()
            
            print(self.cursor.fetchall())
        
        except TypeError as a:
            print(f'Listas vazias. Preencha todas as informações!: {a}\n')
            con.rollback()

        except pymysql.Error as a:
            print(f'Erro ao inserir dados: {a}')
            con.rollback()

        finally:
            self.cursor.close()
            con.close()
            print('Conexão encerrada!')

    def select_data_user(self):
        try:
            personData = DataPerson()
            dataSelect = personData.get_data_for_singup()
            idCadastro = personData.get_id_cadastros()

            select_command = f'SELECT * FROM {db_config['table_user']} WHERE NOME = "{dataSelect[idCadastro[0]][0]}";'
            return select_command
        
        except IndexError as x:
            print(f'Listas vazias. Preencha todas as informações! {x}\n')