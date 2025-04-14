from DataBaseConfig import *
from instances import Pessoa_Dados
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

        finally:
            self.cursor.close()
            con.close()
            print('Conexão encerrada!')

    def insert_data_user(self):
        personData = Pessoa_Dados
        dataSingUp = Pessoa_Dados.data_for_signup

        insert_command = f'INSERT INTO {db_config['table_user']} () VALUES ("{dataSingUp[personData.id_cadastro_nome][0]}","{dataSingUp[personData.id_cadastro_sobrenome][0]}","{dataSingUp[personData.id_cadastro_data_nascimento][0]}","{dataSingUp[personData.id_cadastro_numero_telefone][0]}","{dataSingUp[personData.id_cadastro_email][0]}","{dataSingUp[personData.id_cadastro_logradouro][0]}","{dataSingUp[personData.id_cadastro_numero_casa][0]}","{dataSingUp[personData.id_cadastro_complemento][0]}","{dataSingUp[personData.id_cadastro_bairro][0]}","{dataSingUp[personData.id_cadastro_cidade][0]}","{dataSingUp[personData.id_cadastro_cep][0]}","{dataSingUp[personData.id_cadastro_estado][0]}");' 

        return insert_command

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

        finally:
            self.cursor.close()
            con.close()
            print('Conexão encerrada!')
    
    def delete_data_user(self):
        personData = Pessoa_Dados
        dataDelete = Pessoa_Dados.data_for_signup

        self.delete_command = f'DELETE FROM {db_config['table_user']} WHERE EMAIL = "{dataDelete[personData.id_cadastro_email][0]}";'

        return self.delete_command