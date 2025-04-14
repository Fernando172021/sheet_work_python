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
    id_cadastro_nome = "NOME"
    id_cadastro_sobrenome = "SOBRENOME"
    id_cadastro_data_nascimento = "DATA NASCIMENTO"
    id_cadastro_numero_telefone = "NUMERO TELEFONE" 
    id_cadastro_email = "E-MAIL"
    id_cadastro_logradouro = "LOGRADOURO"
    id_cadastro_numero_casa = "NÚMERO DA CASA"
    id_cadastro_complemento = "COMPLEMENTO"
    id_cadastro_bairro = "BAIRRO" 
    id_cadastro_cidade = "CIDADE"
    id_cadastro_cep = "CEP"
    id_cadastro_estado = "ESTADO"

    data_for_signup = {
        id_cadastro_nome:            [],
        id_cadastro_sobrenome:       [],
        id_cadastro_data_nascimento: [],
        id_cadastro_numero_telefone: [],
        id_cadastro_email:           [],
        id_cadastro_logradouro:      [],
        id_cadastro_numero_casa:     [],
        id_cadastro_complemento:     [],
        id_cadastro_bairro:          [],
        id_cadastro_cidade:          [],
        id_cadastro_cep:             [],
        id_cadastro_estado:          []
    }

    def register_inputs(self, valueInput):
        reg_input.append(valueInput)

    def insert(self):
        for i, key in enumerate(self.data_for_signup.keys()):
            if reg_input[i].get() != '':
                self.data_for_signup[key].append(reg_input[i].get())
                reg_input[i].delete(0, 'end')
                print(f'Pré Carregado --> {self.data_for_signup[key]}')
            else:
                self.clearData()

    def clearData(self):
        for key in self.data_for_signup.keys():
            if len(self.data_for_signup[key]) != 0:
                self.data_for_signup[key].clear()
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
