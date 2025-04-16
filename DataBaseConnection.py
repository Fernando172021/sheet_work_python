from DataBaseConfig import *
from instances import PessoaDados
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
            personData = PessoaDados()
            dataSingUp = personData.get_data_for_singup()
            getDataId = personData.get_id_cadastros()
        
            insert_command = f'INSERT INTO {db_config['table_user']} () VALUES ("{dataSingUp[getDataId[0]][0]}","{dataSingUp[getDataId[1]][0]}","   {dataSingUp[getDataId[2]][0]}","{dataSingUp[getDataId[3]][0]}","{dataSingUp[getDataId[4]][0]}","{dataSingUp[getDataId[5]][0]}","   {dataSingUp[getDataId[6]][0]}","{dataSingUp[getDataId[7]][0]}","{dataSingUp[getDataId[8]][0]}","{dataSingUp[getDataId[9]][0]}","   {dataSingUp[getDataId[10]][0]}","{dataSingUp[getDataId[11]][0]}");' 

            return insert_command
        
        except IndexError as x:
            print(f'Para inserir informações  no BD cadastre as mesmas antes! {x}\n')

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

            # Implementar adição de dados as id_cadastro para poder excluir os dados no banco de dados apartir do email
            # Posteriormente deletar os dados pré cadastrados.

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
            personData = PessoaDados()
            dataDelete = personData.get_data_for_singup()
            idCadastro = personData.get_id_cadastros()

            self.delete_command = f'DELETE FROM {db_config['table_user']} WHERE EMAIL = "{dataDelete[idCadastro[4]][0]}";'

            return self.delete_command
        
        except IndexError as x:
            print(f'Para deletar cadastre as informações do registro! {x}\n')

    
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
            personData = PessoaDados()
            dataSelect = personData.get_data_for_singup()
            idCadastro = personData.get_id_cadastros()

            select_command = f'SELECT * FROM {db_config['table_user']} WHERE EMAIL = "{dataSelect[idCadastro[4]][0]}";'
            return select_command
        
        except IndexError as x:
            print(f'Listas vazias. Preencha todas as informações! {x}\n')

