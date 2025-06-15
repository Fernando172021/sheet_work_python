from logic.AppCore import AppCore
from app.SingIn import Sing_in
from style.Style import StyleWindows
from tkinter import messagebox, Tk, Label, Button
from app.DriverSchedule import DriverSchedule

class Main:
    def __init__(self):
        core = AppCore()
        styleWindows = StyleWindows()
        register_window = core.setRegisteredWindow
        register_winget = core.setRegisteredWinget

        iconImage = styleWindows.getIconImage()
        colorWindowStandart = styleWindows.getColorWindowStandart()
        fgColor = styleWindows.getFgWingetStandart()
        styleConfig = styleWindows.getStyleConfig()
        styleWindows.modeWinget(colorWindowStandart)

        checkColorWhite = styleWindows.checkColorWhite
        checkColorDark = styleWindows.checkColorDark
        
        self.Window = Tk()
        self.Window.title('Gerador de Planilhas')
        self.Window.iconbitmap(iconImage)
        self.Window.resizable(False, False)
        self.Window.config(bg = colorWindowStandart)
        register_window('Main', self.Window)

        self.titleH1 = Label(self.Window, text='GERADOR DE PLANILHAS')
        self.titleH1.config(bg = colorWindowStandart)
        self.titleH1.config(fg = fgColor)
        self.titleH1['font'] = styleConfig[styleWindows.getFontText()], styleConfig[styleWindows.getFontSize()], styleConfig[styleWindows.getFontBold()]
        self.titleH1.grid(column= 10, row= 0, columnspan= 30, padx= 5, pady= 5)
        register_winget('Main', self.titleH1)

        self.button1 = Button(text='HORARIO MOTORISTA', width= styleConfig[styleWindows.getButtonsWidth()], height= styleConfig[styleWindows.getButtonsHeight()], bd= styleConfig[styleWindows.getBorder()], command= DriverSchedule)
        self.button1['font'] = styleConfig[styleWindows.getFontText()], styleConfig[styleWindows.getFontSize()], styleConfig[styleWindows.getFontBold()]
        self.button1.grid(column= 10, row= 1, padx= styleConfig[styleWindows.getButtonPadX()], pady= styleConfig[styleWindows.getButtonPadY()])

        self.button2 = Button(text='CADASTRO', width= styleConfig[styleWindows.getButtonsWidth()], height= styleConfig[styleWindows.getButtonsHeight()], bd= styleConfig[styleWindows.getBorder()], command= Sing_in)
        self.button2['font'] = styleConfig[styleWindows.getFontText()], styleConfig[styleWindows.getFontSize()], styleConfig[styleWindows.getFontBold()]
        self.button2.grid(column= 20, row= 1, padx= styleConfig[styleWindows.getButtonPadX()], pady= styleConfig[styleWindows.getButtonPadY()])

        self.button3 = Button(text='BUTTON_3', width= styleConfig[styleWindows.getButtonsWidth()], height= styleConfig[styleWindows.getButtonsHeight()], bd= styleConfig[styleWindows.getBorder()])
        self.button3['font'] = styleConfig[styleWindows.getFontText()], styleConfig[styleWindows.getFontSize()], styleConfig[styleWindows.getFontBold()]
        self.button3.grid(column= 10, row= 2, padx= styleConfig[styleWindows.getButtonPadX()], pady= styleConfig[styleWindows.getButtonPadY()])

        self.button4 = Button(text='BUTTON_4', width= styleConfig[styleWindows.getButtonsWidth()], height= styleConfig[styleWindows.getButtonsHeight()],bd= styleConfig[styleWindows.getBorder()])
        self.button4['font'] = styleConfig[styleWindows.getFontText()], styleConfig[styleWindows.getFontSize()], styleConfig[styleWindows.getFontBold()]
        self.button4.grid(column= 20, row= 2, padx= styleConfig[styleWindows.getButtonPadX()], pady= styleConfig[styleWindows.getButtonPadY()])

        self.buttonW = Button(text='Claro', width= styleConfig[styleWindows.getButtonsWidth()], height= 2, bd= styleConfig[styleWindows.getBorder()], command= checkColorWhite)
        self.buttonW['font'] = styleConfig[styleWindows.getFontText()], styleConfig[styleWindows.getFontSize()], styleConfig[styleWindows.getFontBold()]
        self.buttonW.grid(column= 10, row= 3, padx= styleConfig[styleWindows.getButtonPadX()], pady= styleConfig[styleWindows.getButtonPadY()])

        self.buttonD = Button(text='Escuro', width= styleConfig[styleWindows.getButtonsWidth()], height= 2, bd= styleConfig[styleWindows.getBorder()], command= checkColorDark)
        self.buttonD['font'] = styleConfig[styleWindows.getFontText()], styleConfig[styleWindows.getFontSize()], styleConfig[styleWindows.getFontBold()]
        self.buttonD.grid(column= 20, row= 3, padx= styleConfig[styleWindows.getButtonPadX()], pady= styleConfig[styleWindows.getButtonPadY()])

        self.Window.protocol("WM_DELETE_WINDOW", self.close)

        self.Window.mainloop()
    
    def close(self):
        core = AppCore()
        if messagebox.askokcancel('Sair', 'Você Quer Sair?'):
            core.unsubscribeWindow('Main')
            core.unsubscribeWinget('Main')

            self.Window.destroy()
