from instances import MotoristasDados, AppCore
from style import *
from tkinter import *
from tkinter import messagebox


class DriverSchedule:
        def __init__(self):
            core = AppCore()
            driver = MotoristasDados()
            register_window = core.setRegisteredWindow
            register_winget = core.setRegisteredWinget
            register_input = core.setRegisteredInput
            listName = driver.get_id_state()
            insert = driver.insert
            creatSheet = driver.creatSheet

            self.window = Tk()
            self.window.title('HR - Motorista') 
            self.window.iconbitmap(iconImage)
            self.window.resizable(False, False)
            self.window.configure(bg = colorWindowStandart)
            register_window('DriverSchedule', self.window) # Registro da da pagina

            self.word_init = Label(self.window, text= 'Insira os dados da operação abaixo', width= 40)
            self.word_init['font'] = fontText
            self.word_init.grid(column = 0, columnspan= 1, row = 0, padx= padX, pady= padY)
            register_winget('DriverSchedule', self.word_init)

            self.inputLabel = Label(self.window, text= listName[0], bg= backgroundcolorFont)
            self.inputLabel['font'] = fontText
            self.inputLabel.grid(column= 0, row= 3)
            register_winget('DriverSchedule', self.inputLabel)

            self.inputValue = Entry(self.window, bd= border, bg= backgroundcolorWidget, width= entryWidth)
            self.inputValue.grid(column= 0, row= 4)
            register_input('DriverSchedule', self.inputValue)

            self.inputLabel2 = Label(self.window, text= listName[1],  bg= backgroundcolorFont)
            self.inputLabel2['font'] = fontText
            self.inputLabel2.grid(column= 0, row= 5)
            register_winget('DriverSchedule', self.inputLabel2)

            self.inputValue2 = Entry(self.window, bd= border, bg= backgroundcolorWidget, width= entryWidth)
            self.inputValue2.grid(column= 0, row= 6)
            register_input('DriverSchedule', self.inputValue2)

            self.inputLabel3 = Label(self.window, text= listName[2], bg= backgroundcolorFont)
            self.inputLabel3['font'] = fontText
            self.inputLabel3.grid(column= 0, row= 7)
            register_winget('DriverSchedule', self.inputLabel3)

            self.inputValue3 = Entry(self.window, bd= border, bg= backgroundcolorWidget, width= entryWidth)
            self.inputValue3.grid(column= 0, row= 8)
            register_input('DriverSchedule', self.inputValue3)

            self.inputLabel4 = Label(self.window, text= listName[3], bg= backgroundcolorFont)
            self.inputLabel4['font'] = fontText
            self.inputLabel4.grid(column= 0, row= 9)
            register_winget('DriverSchedule', self.inputLabel4)

            self.inputValue4 = Entry(self.window, bd= border, bg= backgroundcolorWidget,  width= entryWidth)
            self.inputValue4.grid(column= 0, row= 10)
            register_input('DriverSchedule', self.inputValue4)

            self.inputLabel5 = Label(self.window, text= listName[4], bg= backgroundcolorFont)
            self.inputLabel5['font'] = fontText
            self.inputLabel5.grid(column= 0, row= 11)
            register_winget('DriverSchedule', self.inputLabel5)

            self.inputValue5 = Entry(self.window, bd= border, bg= backgroundcolorWidget,  width= entryWidth)
            self.inputValue5.grid(column= 0, row= 12)
            register_input('DriverSchedule', self.inputValue5)

            self.button1 = Button(self.window, text='Inserir Dados', bd= border, width= buttonsWidth, command= insert)
            self.button1.grid(column= 0, row= 13, pady= padY)
            self.button1['bg'] = backgroundcolorWidget
            self.button1['font'] = fontText

            self.button2 = Button(self.window, text='Gerar Planilha', bd= border, width= buttonsWidth, command= creatSheet)
            self.button2.grid(column= 0, row= 14, pady= padY)
            self.button2['bg'] = backgroundcolorWidget
            self.button2['font'] = fontText

            self.end_word = Label(self.window, text='', bg= backgroundcolorFont)
            self.end_word['font'] = fontText
            self.end_word.grid(column= 0, row= 15, pady= padY)
            register_winget('DriverSchedule', self.end_word)

            self.window.protocol("WM_DELETE_WINDOW", self.close)

            self.window.mainloop()
        
        def close(self):
            core = AppCore()
            if messagebox.askokcancel('Sair', 'Você Quer Sair?'):
                core.unsubscribeInput('DriverSchedule')
                core.unsubscribeWindow('DriverSchedule')
                core.unsubscribeWinget('DriverSchedule')

                self.window.destroy()
