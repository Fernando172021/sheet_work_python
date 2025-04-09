from instasces import *
from tkinter import *

class mainApplication:
    def __init__(self):

        self.window = Tk()
        self.window.title('Cadastros')
        self.window.resizable(False, False)

        self.titleH1 = Label(self.window, text= 'Cadastros Pessoais', bg= backgroundcolorFont)
        self.titleH1['font'] = fontText
        self.titleH1.grid(column= 0, row= 0, columnspan= 10, padx= 5, pady= 5)

        self.titleEntry1 = Label(self.window, text='Nome')
        self.titleEntry1.grid(column= 0, row= 1)
        self.inputLabel = Entry(self.window)
        self.inputLabel.grid(column= 0, row= 2,)

        self.titleEntry2 = Label(self.window, text='Sobrenome')
        self.titleEntry2.grid(column= 3, row= 1)
        self.inputLabel2 = Entry(self.window)
        self.inputLabel2.grid(column= 3, row= 2)

        self.titleEntry3 = Label(self.window, text= 'Data de Nascimento')
        self.titleEntry3.grid(column= 4, row= 1)
        self.inputLabel3 = Entry(self.window)
        self.inputLabel3.grid(column= 4, row= 2)

        self.titleEntry4 = Label(self.window, text= 'Telefone')
        self.titleEntry4.grid(column= 0, row= 3)
        self.inputLabel4 = Entry(self.window)
        self.inputLabel4.grid(column= 0, row= 4)

        self.titleEntry5 = Label(self.window, text= 'Profissão')
        self.titleEntry5.grid(column= 3, row= 3)
        self.inputLabel5 = Entry(self.window)
        self.inputLabel5.grid(column= 3, row= 4)

        self.titleEntry6 = Label(self.window, text= 'Logradouro')
        self.titleEntry6.grid(column= 4, row= 3)
        self.inputLabel6 = Entry(self.window)
        self.inputLabel6.grid(column= 4, row= 4)

        self.titleEntry7 = Label(self.window, text= 'Número Da Casa')
        self.titleEntry7.grid(column= 0, row= 5)
        self.inputLabel7 = Entry(self.window)
        self.inputLabel7.grid(column= 0, row= 6)

        self.titleEntry8 = Label(self.window, text= 'Bairro')
        self.titleEntry8.grid(column= 3, row= 5)
        self.inputLabel8 = Entry(self.window)
        self.inputLabel8.grid(column= 3, row= 6)

        self.titleEntry9 = Label(self.window, text= 'Cidade')
        self.titleEntry9.grid(column= 4, row= 5)
        self.inputLabel9 = Entry(self.window)
        self.inputLabel9.grid(column= 4, row= 6)

        self.titleEntry10 = Label(self.window, text= 'Estado')
        self.titleEntry10.grid(column= 0, row= 7)
        self.inputLabel10 = Entry(self.window)
        self.inputLabel10.grid(column= 0, row= 8)

        self.titleEntry12 = Label(self.window, text= 'CEP')
        self.titleEntry12.grid(column= 3, row= 7)
        self.inputLabel12 = Entry(self.window)
        self.inputLabel12.grid(column= 3, row= 8)

        self.button = Button(self.window, text= 'Enviar', command= self.extraction)
        self.button.grid(column= 3, row= 9)

        self.window.mainloop()

    def extraction(self):

        if self.inputLabel.get() != '':
            self.nome_db = self.inputLabel.get()
        else:
            print('Sem informações!')

        if self.inputLabel2.get() != '':
            self.sobrenome_db = self.inputLabel2.get()
        else:
            print('Sem informações!')

        if self.inputLabel3.get() != '':
            self.data_nascimento_db = self.inputLabel3.get()
        else:
            print('Sem informações!')

        if self.inputLabel4.get != '':
            self.telefone_db = self.inputLabel4.get()
        else:
            print('Sem informações!')

        if self.inputLabel5.get() != '':
            self.profissao_db = self.inputLabel5.get()
        else:
            print('Sem informações!')

        if self.inputLabel6.get() != '':
            self.logradouro_db = self.inputLabel6.get()
        else:
            print('Sem informações!')

        if self.inputLabel7.get() != '':
            self.numero_casa_db = self.inputLabel7.get()
        else:
            print('Sem informações!')

        if self.inputLabel8.get() != '':
            self.bairro_db = self.inputLabel8.get()
        else:
            print('Sem informações!')

        if self.inputLabel9.get() != '':
            self.cidade_db = self.inputLabel9.get()
        else:
            print('Sem informações!')

        if self.inputLabel10.get() != '':
            self.estado_db = self.inputLabel10.get()
        else:
            print('Sem informações!')

        if self.inputLabel12.get() != '':
            self.cep_db = self.inputLabel12.get()
        else:
            print('Sem informações!')

ia = mainApplication()
