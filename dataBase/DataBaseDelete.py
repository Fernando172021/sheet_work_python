from dataBase.DataBaseConfig import *
from logic.DataPerson import DataPerson
import pymysql


class DataBaseDelete:
    def __init__(self):
        con = pymysql.connect(
            host= db_config['host'],
            user= db_config['user'],
            password= db_config['password'],
            database= db_config['database'],
        )

        try:
            self.cursor = con.cursor()
            self.cursor.execute(self.delete_data_user())
            con.commit()

            print('Dados Excluidos com sucesso!')

        except pymysql.Error as a:
            print(f'Erro ao inserir dados: {a}')
            con.rollback()

        except TypeError as a:
            print(f'Listas vazias. Preencha todas as informações!: {a}\n')

        finally:
            self.cursor.close()
            con.close()
            print('Conexão encerrada!')
    
    def delete_data_user(self):
        try:
            personData = DataPerson()
            dataDelete = personData.get_data_for_singup()
            idCadastro = personData.get_id_cadastros()

            self.delete_command = f'DELETE FROM {db_config['table_user']} WHERE NOME = "{dataDelete[idCadastro[0]][0]}";'

            return self.delete_command
        
        except IndexError as x:
            print(f'Para deletar cadastre as informações do registro! {x}\n')