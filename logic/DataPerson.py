from logic.AppCore import AppCore

class DataPerson:
    processList = []

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
        __id_cadastros = []
        __dataSignup = self.get_data_for_singup()

        for i in __dataSignup.keys():
            __id_cadastros.append(i)

        return __id_cadastros
    
    def set_data_for_singup(self, name, key, num):
        core = AppCore()
        registerInput = core.getRegisteredInput()

        listDataUser = self.__data_for_signup

        listDataUser[name].append(registerInput[key][num].get())

    # Acima metodos Get n' Set
    
    def insert(self):
        core = AppCore()
        registerInput = core.getRegisteredInput()
        key = core.getSingIn()
        __listDataUser = self.get_data_for_singup()

        for id in __listDataUser:
            self.processList.append(id)
        
        for i, id in enumerate(registerInput[key]):
            if registerInput[key][i].get() != '':
                self.set_data_for_singup(self.processList[i], key, i)
                print(f'{__listDataUser[self.processList[i]][0]} --> Pré Carregado\n')
                #print(self.processList[i], key)
            else:
                print('PRENENCHA OS CAMPOS!')


    def clearData(self):
        core = AppCore()
        registerInput = core.getRegisteredInput()
        key = core.getSingIn()
        __listDataUser = self.get_data_for_singup()

        for id in __listDataUser:
            for num, x in enumerate(__listDataUser[id]): # retirar laço for
                x == None
                __listDataUser[id].pop(0)

        self.processList.clear()
        
        for num, x in enumerate(registerInput[key]):
            registerInput[key][num].delete(0, 'end')
        
        print('INSIRA TODAS AS INSFORMAÇÕES\nINTERFACE LIMPA\n')