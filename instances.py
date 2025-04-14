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

class pessoa_dados:
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
        if reg_input[0].get() != '':
            self.data_for_signup[self.id_cadastro_nome].append(reg_input[0].get())
            reg_input[0].delete(0, 'end')
        else:
            self.clearData()
        
        if reg_input[1].get() != '':
            self.data_for_signup[self.id_cadastro_sobrenome].append(reg_input[1].get())
            reg_input[1].delete(0, 'end')
        else:
            self.clearData()

        if reg_input[2].get() != '':
            self.data_for_signup[self.id_cadastro_data_nascimento].append(reg_input[2].get())
            reg_input[2].delete(0, 'end')
        else:
            self.clearData()

        if reg_input[3].get() != '':
            self.data_for_signup[self.id_cadastro_numero_telefone].append(reg_input[3].get())
            reg_input[3].delete(0, 'end')
        else:
            self.clearData()

        if reg_input[4].get() != '':
            self.data_for_signup[self.id_cadastro_email].append(reg_input[4].get())
            reg_input[4].delete(0, 'end')
        else:
            self.clearData()

        if reg_input[5].get() != '':
            self.data_for_signup[self.id_cadastro_logradouro].append(reg_input[5].get())
            reg_input[5].delete(0, 'end')
        else:
            self.clearData()

        if reg_input[6].get() != '':
            self.data_for_signup[self.id_cadastro_numero_casa].append(reg_input[6].get())
            reg_input[6].delete(0, 'end')
        else:
            self.clearData()

        if reg_input[7].get() != '':
            self.data_for_signup[self.id_cadastro_complemento].append(reg_input[7].get())
            reg_input[7].delete(0, 'end')
        else:
            self.clearData()

        if reg_input[8].get() != '':
            self.data_for_signup[self.id_cadastro_bairro].append(reg_input[8].get())
            reg_input[8].delete(0, 'end')
        else:
            self.clearData()

        if reg_input[9].get() != '':
            self.data_for_signup[self.id_cadastro_cidade].append(reg_input[9].get())
            reg_input[9].delete(0, 'end')
        else:
            self.clearData()

        if reg_input[10].get() != '':
            self.data_for_signup[self.id_cadastro_cep].append(reg_input[10].get())
            reg_input[10].delete(0, 'end')
        else:
            self.clearData()

        if reg_input[11].get() != '':
            self.data_for_signup[self.id_cadastro_estado].append(reg_input[11].get())
            reg_input[11].delete(0, 'end')
        else:
            self.clearData()

    def clearData(self):
        cd1 = list(self.data_for_signup[self.id_cadastro_nome])
        cd2 = list(self.data_for_signup[self.id_cadastro_sobrenome])
        cd3 = list(self.data_for_signup[self.id_cadastro_data_nascimento])
        cd4 = list(self.data_for_signup[self.id_cadastro_numero_telefone])
        cd5 = list(self.data_for_signup[self.id_cadastro_email])
        cd6 = list(self.data_for_signup[self.id_cadastro_logradouro])
        cd7 = list(self.data_for_signup[self.id_cadastro_numero_casa])
        cd8 = list(self.data_for_signup[self.id_cadastro_complemento])
        cd9 = list(self.data_for_signup[self.id_cadastro_bairro])
        cd10 = list(self.data_for_signup[self.id_cadastro_cidade])
        cd11 = list(self.data_for_signup[self.id_cadastro_cep])
        cd12 = list(self.data_for_signup[self.id_cadastro_estado])

        if len(self.data_for_signup[self.id_cadastro_nome]) != 0:
            for self.numberFrame in cd1:
                self.data_for_signup[self.id_cadastro_nome].pop()

        if len(self.data_for_signup[self.id_cadastro_sobrenome]) != 0:
            for self.numberFrame in cd2:
                self.data_for_signup[self.id_cadastro_sobrenome].pop()

        if len(self.data_for_signup[self.id_cadastro_data_nascimento]) != 0:
            for self.numberFrame in cd3:
                self.data_for_signup[self.id_cadastro_data_nascimento].pop()

        if len(self.data_for_signup[self.id_cadastro_numero_telefone]) != 0:
            for self.numberFrame in cd4:
                self.data_for_signup[self.id_cadastro_numero_telefone].pop()

        if len(self.data_for_signup[self.id_cadastro_email]) != 0:
            for self.numberFrame in cd5:
                self.data_for_signup[self.id_cadastro_email].pop()
        
        if len(self.data_for_signup[self.id_cadastro_logradouro]) != 0:
            for self.numberFrame in cd6:
                self.data_for_signup[self.id_cadastro_logradouro].pop()
        
        if len(self.data_for_signup[self.id_cadastro_numero_casa]) != 0:
            for self.numberFrame in cd7:
                self.data_for_signup[self.id_cadastro_numero_casa].pop()

        if len(self.data_for_signup[self.id_cadastro_complemento]) != 0:
            for self.numberFrame in cd8:
                self.data_for_signup[self.id_cadastro_complemento].pop()

        if len(self.data_for_signup[self.id_cadastro_bairro]) != 0:
            for self.numberFrame in cd9:
                self.data_for_signup[self.id_cadastro_bairro].pop()

        if len(self.data_for_signup[self.id_cadastro_cidade]) != 0:
            for self.numberFrame in cd10:
                self.data_for_signup[self.id_cadastro_cidade].pop()

        if len(self.data_for_signup[self.id_cadastro_cep]) != 0:
            for self.numberFrame in cd11:
                self.data_for_signup[self.id_cadastro_cep].pop()

        if len(self.data_for_signup[self.id_cadastro_estado]) != 0:
            for self.numberFrame in cd12:
                self.data_for_signup[self.id_cadastro_estado].pop()

