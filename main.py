from instances import *
from singIn import singIn
from style import *
from tkinter import *
from driver_schedule import driver_schedule

class mainApplication:
    def __init__(self):
        
        self.Window = Tk()
        self.Window.title('Gerador de Planilhas')
        self.Window.iconbitmap(iconImage)
        self.Window.resizable(False, False)
        self.Window.config(bg = colorWindowStandart)
        register_window(self.Window)

        self.titleH1 = Label(self.Window, text='GERADOR DE PLANILHAS')
        self.titleH1['font'] = fontText
        self.titleH1.grid(column= 10, row= 0, columnspan= 30, padx= 5, pady= 5)
        register_winget(self.titleH1)

        self.button1 = Button(text='HORARIO MOTORISTA', width= buttonsWidth, height= buttonsHeight, bd= border, command= driver_schedule)
        self.button1['font'] = fontText
        self.button1.grid(column= 10, row= 1, padx= buttonPadx, pady= buttonPady)

        self.button2 = Button(text='CADASTRO', width= buttonsWidth, height= buttonsHeight, bd= border, command= singIn)
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

        self.Window.mainloop()

mainApplication = mainApplication()
