from instasces import *
from tkinter import *
from horario_motorista import horario_motorista

class mainApplication:
    def __init__(self):
        
        self.mainWindow = Tk()
        self.mainWindow.title('Gerador de Planilhas')
        self.mainWindow.iconbitmap(iconImage)
        self.mainWindow.resizable(False, False)

        self.titleH1 = Label(self.mainWindow, text='GERADOR DE PLANILHAS', bg= backgroundcolorFont)
        self.titleH1['font'] = fontText
        self.titleH1.grid(column= 10, row= 0, columnspan= 30, padx= 5, pady= 5)

        self.button1 = Button(text='HORARIO MOTORISTA', width= buttonsWidth, height= buttonsHeight, bd= border, command= horario_motorista)
        self.button1['font'] = fontText
        self.button1.grid(column= 10, row= 1, padx= buttonPadx, pady= buttonPady)

        self.button2 = Button(text='CADASTRO', width= buttonsWidth, height= buttonsHeight, bd= border)
        self.button2['font'] = fontText
        self.button2.grid(column= 20, row= 1, padx= buttonPadx, pady= buttonPady)

        self.button3 = Button(text='BUTTON_3', width= buttonsWidth, height= buttonsHeight, bd= border)
        self.button3['font'] = fontText
        self.button3.grid(column= 10, row= 2, padx= buttonPadx, pady= buttonPady)

        self.button4 = Button(text='BUTTON_4', width= buttonsWidth, height= buttonsHeight,bd= border)
        self.button4['font'] = fontText
        self.button4.grid(column= 20, row= 2, padx= buttonPadx, pady= buttonPady)

        self.mainWindow.mainloop()

ia = mainApplication()
