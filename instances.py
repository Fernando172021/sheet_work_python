#Instacias que definem os estilos das janelas

reg_input = []

id_name = "NOME MOTORISTA"
id_start_load = "CHEGADA CARREGAMENTO"
id_end_load = "SAIDA CARREGAMENTO"
id_start_unload = "CHEGADA DESCARGA"
id_end_unload = "SAIDA DESCARGA"


data = {
        id_name:         [],
        id_start_load:   [],
        id_end_load:     [],
        id_start_unload: [],
        id_end_unload:   []
    }

class Pessoa_Dados:
    __id_cadastro_nome = "NOME"
    __id_cadastro_sobrenome = "SOBRENOME"
    __id_cadastro_data_nascimento = "DATA NASCIMENTO"
    __id_cadastro_numero_telefone = "NUMERO TELEFONE" 
    __id_cadastro_email = "E-MAIL"
    __id_cadastro_logradouro = "LOGRADOURO"
    __id_cadastro_numero_casa = "NÚMERO DA CASA"
    __id_cadastro_complemento = "COMPLEMENTO"
    __id_cadastro_bairro = "BAIRRO" 
    __id_cadastro_cidade = "CIDADE"
    __id_cadastro_cep = "CEP"
    __id_cadastro_estado = "ESTADO"

    __data_for_signup = {
        __id_cadastro_nome:            [],
        __id_cadastro_sobrenome:       [],
        __id_cadastro_data_nascimento: [],
        __id_cadastro_numero_telefone: [],
        __id_cadastro_email:           [],
        __id_cadastro_logradouro:      [],
        __id_cadastro_numero_casa:     [],
        __id_cadastro_complemento:     [],
        __id_cadastro_bairro:          [],
        __id_cadastro_cidade:          [],
        __id_cadastro_cep:             [],
        __id_cadastro_estado:          []
    }

    def get_data_for_singup(self):
        return self.__data_for_signup
    
    def get_id_cadastros(self):
        self.__id_cadastros = []
        for i in self.get_data_for_singup().keys():
            self.__id_cadastros.append(i)

        return self.__id_cadastros

    
    def set_data_for_singup(self, key, registeredEntry):
        self.__data_for_signup[key].append(registeredEntry.get())

    def register_inputs(self, valueInput):
        reg_input.append(valueInput)
    
    def insert(self):
        __listDataUser = self.get_data_for_singup()

        for i, key in enumerate(__listDataUser.keys()):
            if reg_input[i].get() != '':
                self.set_data_for_singup(key, reg_input[i])
                reg_input[i].delete(0, 'end')
                print(f'Pré Carregado --> {__listDataUser[key][0]}')
            else:
                print('clear data insert')
                self.clearData

    def clearData(self):
        __listDataUser = self.get_data_for_singup()

        for key in __listDataUser.keys():
            if len(__listDataUser[key]) != 0:
                __listDataUser[key].clear()
                print(f'{key} --> LIMPO')
        
        for i in reg_input:
            i.delete(0, 'end')
        
        print('INSIRA TODAS AS INSFORMAÇÕES\nINTERFACE LIMPA')

class ConsoleRedirect:

    def __init__(self, text_widget):
        self.text_widget = text_widget

    def write(self, message):
        self.text_widget.insert('end', message)  
        self.text_widget.see('end')  

    def flush(self):
        pass
