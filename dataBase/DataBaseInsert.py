from dataBase.DataBaseConfig import *
from logic.DataPerson import DataPerson
import pymysql


class DataBaseInsert:
    def __init__(self):   
        con = pymysql.connect(
            host= db_config['host'],
            user= db_config['user'],
            password= db_config['password'],
            database= db_config['database'],
        )

        try:
            self.cursor = con.cursor()
            self.cursor.execute(self.insert_data_user())
            con.commit()

            print('Dados Inseridos com sucesso!')

        except pymysql.Error as a:
            print(f'Erro ao inserir dados: {a}')
            con.rollback()
        
        except TypeError as a:
            print(f'Listas vazias. Preencha todas as informações!: {a}\n')

        finally:
            self.cursor.close()
            con.close()
            print('Conexão encerrada!')

    def insert_data_user(self):
        try:
            personData = DataPerson()
            dataSingUp = personData.get_data_for_singup()
            getDataId = personData.get_id_cadastros()
        
            insert_command = f'INSERT INTO {db_config['table_user']} () VALUES ("{dataSingUp[getDataId[0]][0]}","{dataSingUp[getDataId[1]][0]}","{dataSingUp[getDataId[2]][0]}","{dataSingUp[getDataId[3]][0]}","{dataSingUp[getDataId[4]][0]}","{dataSingUp[getDataId[5]][0]}","{dataSingUp[getDataId[6]][0]}","{dataSingUp[getDataId[7]][0]}","{dataSingUp[getDataId[8]][0]}","{dataSingUp[getDataId[9]][0]}","{dataSingUp[getDataId[10]][0]}","{dataSingUp[getDataId[11]][0]}");' 

            return insert_command
        
        except IndexError as x:
            print(f'Para inserir informações  no BD cadastre as mesmas antes! {x}\n')