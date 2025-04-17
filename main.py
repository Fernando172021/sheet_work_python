from instances import AppCore
from sing_in import Sing_in
from style import *
from tkinter import *
from tkinter import messagebox
from DriverSchedule import DriverSchedule

class MainApplication:
    def __init__(self):
        core = AppCore()
        register_window = core.setRegisteredWindow
        register_winget = core.setRegisteredWinget
        
        self.Window = Tk()
        self.Window.title('Gerador de Planilhas')
        self.Window.iconbitmap(iconImage)
        self.Window.resizable(False, False)
        self.Window.config(bg = colorWindowStandart)
        register_window('Main', self.Window)

        self.titleH1 = Label(self.Window, text='GERADOR DE PLANILHAS')
        self.titleH1['font'] = fontText
        self.titleH1.grid(column= 10, row= 0, columnspan= 30, padx= 5, pady= 5)
        register_winget('Main', self.titleH1)

        self.button1 = Button(text='HORARIO MOTORISTA', width= buttonsWidth, height= buttonsHeight, bd= border, command= DriverSchedule)
        self.button1['font'] = fontText
        self.button1.grid(column= 10, row= 1, padx= buttonPadx, pady= buttonPady)

        self.button2 = Button(text='CADASTRO', width= buttonsWidth, height= buttonsHeight, bd= border, command= Sing_in)
        self.button2['font'] = fontText
        self.button2.grid(column= 20, row= 1, padx= buttonPadx, pady= buttonPady)

        self.button3 = Button(text='BUTTON_3', width= buttonsWidth, height= buttonsHeight, bd= border)
        self.button3['font'] = fontText
        self.button3.grid(column= 10, row= 2, padx= buttonPadx, pady= buttonPady)

        self.button4 = Button(text='BUTTON_4', width= buttonsWidth, height= buttonsHeight,bd= border)
        self.button4['font'] = fontText
        self.button4.grid(column= 20, row= 2, padx= buttonPadx, pady= buttonPady)

        self.buttonW = Button(text='Claro', width= buttonsWidth, height= 2, bd= border, command= checkColorWhite)
        self.buttonW['font'] = fontText
        self.buttonW.grid(column= 10, row= 3, padx= buttonPadx, pady= buttonPady)

        self.buttonD = Button(text='Escuro', width= buttonsWidth, height= 2, bd= border, command= checkColorDark)
        self.buttonD['font'] = fontText
        self.buttonD.grid(column= 20, row= 3, padx= buttonPadx, pady= buttonPady)

        self.Window.protocol("WM_DELETE_WINDOW", self.close)

        self.Window.mainloop()
    
    def close(self):
        core = AppCore()
        if messagebox.askokcancel('Sair', 'Você Quer Sair?'):
            core.unsubscribeWindow('Main')
            core.unsubscribeWinget('Main')

            self.Window.destroy()

mainApplication = MainApplication()
