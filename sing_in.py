from tkinter import *
from instances import PessoaDados, ConsoleRedirect, AppCore
from DataBaseConnection import DataBaseInsert, DataBaseDelete, DataBaseSelect
from style import *
import sys

class Sing_in:
    def __init__(self):

        person = PessoaDados()
        core = AppCore()
        dataBaseInsert = DataBaseInsert
        dataBaseDelete = DataBaseDelete
        dataBaseSelect = DataBaseSelect
        register_inputs = core.setRegisteredInput
        register_window = core.setRegisteredWindow
        register_winget = core.setRegisteredWinget
        id_cadastros = person.get_id_cadastros()
        
        self.window = Tk()
        self.window.title('Cadastro')
        self.window.iconbitmap(iconImage)
        self.window.resizable(False, False)
        self.window.configure(bg = colorWindowStandart)
        register_window('Sing_in_window', self.window)

        self.label0 = Label(self.window, text= 'INSIRA OS SEUS DADOS A BAIXO', width= 40)
        self.label0['font'] = fontText
        self.label0.grid(row= 0, column= 1, padx= padX, pady= padY)
        register_winget('Sing_in_label0', self.label0)

        self.label1 = Label(self.window, text= id_cadastros[0], width= 40)
        self.label1['font'] = fontText
        self.label1.grid(row= 1, column= 0, padx= padX, pady= padY)
        register_winget('Sing_in_label1', self.label1)

        self.input1 = Entry(self.window, bd= border, bg= backgroundcolorWidget, width= 30)
        self.input1['font'] = fontText
        self.input1.grid(row= 2, column= 0, padx= padX, pady= padY)
        register_inputs('Sing_in_input1', self.input1)

        self.label2 = Label(self.window, text= id_cadastros[1], width= 40)
        self.label2['font'] = fontText
        self.label2.grid(row= 1, column= 1, padx= padX, pady= padY)
        register_winget('Sing_in_label2', self.label2)

        self.input2 = Entry(self.window, bd= border, bg= backgroundcolorWidget, width= 30)
        self.input2['font'] = fontText
        self.input2.grid(row= 2, column= 1, padx= padX, pady= padY)
        register_inputs('Sing_in_input2', self.input2)

        self.label3 = Label(self.window, text= id_cadastros[2], width= 40)
        self.label3['font'] = fontText
        self.label3.grid(row= 1, column= 2, padx= padX, pady= padY)
        register_winget('Sing_in_label3', self.label3)

        self.input3 = Entry(self.window, bd= border, bg= backgroundcolorWidget, width= 30)
        self.input3['font'] = fontText
        self.input3.grid(row= 2, column= 2, padx= padX, pady= padY)
        register_inputs('Sing_in_input3', self.input3)

        self.label4 = Label(self.window, text= id_cadastros[3], width= 40)
        self.label4['font'] = fontText
        self.label4.grid(row= 3, column= 0, padx= padX, pady= padY)
        register_winget('Sing_in_label4', self.label4)

        self.input4 = Entry(self.window, bd= border, bg= backgroundcolorWidget, width= 30)
        self.input4['font'] = fontText
        self.input4.grid(row= 4, column= 0, padx= padX, pady= padY)
        register_inputs('Sing_in_input4', self.input4)

        self.label5 = Label(self.window, text= id_cadastros[4], width= 40)
        self.label5['font'] = fontText
        self.label5.grid(row= 3, column= 1, padx= padX, pady= padY)
        register_winget('Sing_in_label5', self.label5)

        self.input5 = Entry(self.window, bd= border, bg= backgroundcolorWidget, width= 30)
        self.input5['font'] = fontText
        self.input5.grid(row= 4, column= 1, padx= padX, pady= padY)
        register_inputs('Sing_in_input5', self.input5)

        self.label6 = Label(self.window, text= id_cadastros[5], width= 40)
        self.label6['font'] = fontText
        self.label6.grid(row= 3, column= 2, padx= padX, pady= padY)
        register_winget('Sing_in_label6', self.label6)

        self.input6 = Entry(self.window, bd= border, bg= backgroundcolorWidget, width= 30)
        self.input6['font'] = fontText
        self.input6.grid(row= 4, column= 2, padx= padX, pady= padY)
        register_inputs('Sing_in_input6', self.input6)

        self.label7 = Label(self.window, text= id_cadastros[6], width= 40)
        self.label7['font'] = fontText
        self.label7.grid(row= 5, column= 0, padx= padX, pady= padY)
        register_winget('Sing_in_label7', self.label7)

        self.input7 = Entry(self.window, bd= border, bg= backgroundcolorWidget, width= 30)
        self.input7['font'] = fontText
        self.input7.grid(row= 6, column= 0, padx= padX, pady= padY)
        register_inputs('Sing_in_input7', self.input7)

        self.label8 = Label(self.window, text= id_cadastros[7], width= 40)
        self.label8['font'] = fontText
        self.label8.grid(row= 5, column= 1, padx= padX, pady= padY)
        register_winget('Sing_in_label8', self.label8)

        self.input8 = Entry(self.window, bd= border, bg= backgroundcolorWidget, width= 30)
        self.input8['font'] = fontText
        self.input8.grid(row= 6, column= 1, padx= padX, pady= padY)
        register_inputs('Sing_in_input8', self.input8)

        self.label9 = Label(self.window, text= id_cadastros[8], width= 40)
        self.label9['font'] = fontText
        self.label9.grid(row= 5, column= 2, padx= padX, pady= padY)
        register_winget('Sing_in_label9', self.label9)

        self.input9 = Entry(self.window, bd= border, bg= backgroundcolorWidget, width= 30)
        self.input9['font'] = fontText
        self.input9.grid(row= 6, column= 2, padx= padX, pady= padY)
        register_inputs('Sing_in_input9', self.input9)

        self.label10 = Label(self.window, text= id_cadastros[9], width= 40)
        self.label10['font'] = fontText
        self.label10.grid(row= 7, column= 0, padx= padX, pady= padY)
        register_winget('Sing_in_label10', self.label10)

        self.input10 = Entry(self.window, bd= border, bg= backgroundcolorWidget, width= 30)
        self.input10['font'] = fontText
        self.input10.grid(row= 8, column= 0, padx= padX, pady= padY)
        register_inputs('Sing_in_input10', self.input10)

        self.label11 = Label(self.window, text= id_cadastros[10], width= 40)
        self.label11['font'] = fontText
        self.label11.grid(row= 7, column= 1, padx= padX, pady= padY)
        register_winget('Sing_in_label11', self.label11)

        self.input11 = Entry(self.window, bd= border, bg= backgroundcolorWidget, width= 30)
        self.input11['font'] = fontText
        self.input11.grid(row= 8, column= 1, padx= padX, pady= padY)
        register_inputs('Sing_in_input11', self.input11)

        self.label12 = Label(self.window, text= id_cadastros[11], width= 40)
        self.label12['font'] = fontText
        self.label12.grid(row= 7, column= 2, padx= padX, pady= padY)
        register_winget('Sing_in_label12', self.label12)

        self.input12 = Entry(self.window, bd= border, bg= backgroundcolorWidget, width= 30)
        self.input12['font'] = fontText
        self.input12.grid(row= 8, column= 2, padx= padX, pady= padY)
        register_inputs('Sing_in_input12', self.input12)

        self.labelText = Label(self.window, text= 'Para PESQUISAR / DELETAR digite o email aperte CADASTRAR e em seguida as opções anteriores.')
        self.labelText['font'] = fontText
        self.labelText.grid(row= 9, column= 1, padx= padX, pady= padY)

        self.buttonClear = Button(self.window, text= 'LIMPAR', width= buttonsWidth, height= 2, bd= border, command= person.clearData)
        self.buttonClear['font'] = fontText
        self.buttonClear.grid(row= 10, column= 0, padx= buttonPadx, pady= buttonPady)

        self.buttonUp = Button(self.window, text= 'CADASTRAR', width= buttonsWidth, height= 2, bd= border, command= person.insert)
        self.buttonUp['font'] = fontText
        self.buttonUp.grid(row= 10, column= 1, padx= buttonPadx, pady= buttonPady)

        self.buttonSingIn = Button(self.window, text= 'APLICAR', width= buttonsWidth, height= 2, bd= border, command= dataBaseInsert)
        self.buttonSingIn['font'] = fontText
        self.buttonSingIn.grid(row= 10, column= 2, padx= buttonPadx, pady= buttonPady)

        self.buttonSearch = Button(self.window, text= 'PESQUISA', width= buttonsWidth, height= 2, bd= border, command= dataBaseSelect)
        self.buttonSearch['font'] = fontText
        self.buttonSearch.grid(row= 11, column= 0, padx= buttonPadx, pady= buttonPady)

        self.buttonDelete = Button(self.window, text= 'DELETAR', width= buttonsWidth, height= 2, bd= border, command= dataBaseDelete)
        self.buttonDelete['font'] = fontText
        self.buttonDelete.grid(row= 11, column= 2, padx= buttonPadx, pady= buttonPady)

        self.console_output = Text(self.window, height= 10, width= 70, state= NORMAL, fg= fontColorConsole, bg= '#f7f7f7')
        self.console_output['font'] = fontFamilyConsole
        self.console_output.grid(row= 11, column= 1)

        sys.stdout = ConsoleRedirect(self.console_output)

        self.window.mainloop()
