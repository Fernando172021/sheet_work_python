from logic.DataDrivers import DataDriver
from logic.AppCore import AppCore
from style.Style import StyleWindows
from tkinter import messagebox, Tk, Label, Entry, Button

class DriverSchedule:
        def __init__(self):
            core = AppCore()
            driver = DataDriver()
            styleWindows = StyleWindows()
            register_window = core.setRegisteredWindow
            register_winget = core.setRegisteredWinget
            register_input = core.setRegisteredInput
            listName = driver.get_id_state()
            insert = driver.insert
            creatSheet = driver.creatSheet

            iconImage = styleWindows.getIconImage()
            colorWindowStandart = styleWindows.getColorWindowStandart()
            styleConfig = styleWindows.getStyleConfig()
            fgColor = styleWindows.getFgWingetStandart()

            self.window = Tk()
            self.window.title('HR - Motorista') 
            self.window.iconbitmap(iconImage)
            self.window.resizable(False, False)
            self.window.configure(bg = colorWindowStandart)
            register_window('DriverSchedule', self.window) # Registro da da pagina

            self.word_init = Label(self.window, text= 'Insira os dados da operação abaixo', width= 40)
            self.word_init.config(bg = colorWindowStandart)
            self.word_init.config(fg = fgColor)
            self.word_init['font'] = styleConfig[styleWindows.getFontText()], styleConfig[styleWindows.getFontSize()], styleConfig[styleWindows.getFontBold()]
            self.word_init.grid(column = 0, columnspan= 1, row = 0, padx= styleConfig[styleWindows.getPadX()], pady= styleConfig[styleWindows.getPadY()])
            register_winget('DriverSchedule', self.word_init)

            self.inputLabel = Label(self.window, text= listName[0], bg= styleConfig[styleWindows.getBackGroundColorFont()])
            self.inputLabel.config(bg = colorWindowStandart)
            self.inputLabel.config(fg = fgColor)
            self.inputLabel['font'] = styleConfig[styleWindows.getFontText()], styleConfig[styleWindows.getFontSize()], styleConfig[styleWindows.getFontBold()]
            self.inputLabel.grid(column= 0, row= 3)
            register_winget('DriverSchedule', self.inputLabel)

            self.inputValue = Entry(self.window, bd= styleConfig[styleWindows.getBorder()], bg= styleConfig[styleWindows.getBackGroundColorWidget()], width= styleConfig[styleWindows.getEntryWidth()])
            self.inputValue.grid(column= 0, row= 4)
            register_input('DriverSchedule', self.inputValue)

            self.inputLabel2 = Label(self.window, text= listName[1],  bg= styleConfig[styleWindows.getBackGroundColorFont()])
            self.inputLabel2.config(bg = colorWindowStandart)
            self.inputLabel2.config(fg = fgColor)
            self.inputLabel2['font'] = styleConfig[styleWindows.getFontText()], styleConfig[styleWindows.getFontSize()], styleConfig[styleWindows.getFontBold()]
            self.inputLabel2.grid(column= 0, row= 5)
            register_winget('DriverSchedule', self.inputLabel2)

            self.inputValue2 = Entry(self.window, bd= styleConfig[styleWindows.getBorder()], bg= styleConfig[styleWindows.getBackGroundColorWidget()], width= styleConfig[styleWindows.getEntryWidth()])
            self.inputValue2.grid(column= 0, row= 6)
            register_input('DriverSchedule', self.inputValue2)

            self.inputLabel3 = Label(self.window, text= listName[2], bg= styleConfig[styleWindows.getBackGroundColorFont()])
            self.inputLabel3.config(bg = colorWindowStandart)
            self.inputLabel3.config(fg = fgColor)
            self.inputLabel3['font'] = styleConfig[styleWindows.getFontText()], styleConfig[styleWindows.getFontSize()], styleConfig[styleWindows.getFontBold()]
            self.inputLabel3.grid(column= 0, row= 7)
            register_winget('DriverSchedule', self.inputLabel3)

            self.inputValue3 = Entry(self.window, bd= styleConfig[styleWindows.getBorder()], bg= styleConfig[styleWindows.getBackGroundColorWidget()], width= styleConfig[styleWindows.getEntryWidth()])
            self.inputValue3.grid(column= 0, row= 8)
            register_input('DriverSchedule', self.inputValue3)

            self.inputLabel4 = Label(self.window, text= listName[3], bg= styleConfig[styleWindows.getBackGroundColorFont()])
            self.inputLabel4.config(bg = colorWindowStandart)
            self.inputLabel4.config(fg = fgColor)
            self.inputLabel4['font'] = styleConfig[styleWindows.getFontText()], styleConfig[styleWindows.getFontSize()], styleConfig[styleWindows.getFontBold()]
            self.inputLabel4.grid(column= 0, row= 9)
            register_winget('DriverSchedule', self.inputLabel4)

            self.inputValue4 = Entry(self.window, bd= styleConfig[styleWindows.getBorder()], bg= styleConfig[styleWindows.getBackGroundColorWidget()],  width= styleConfig[styleWindows.getEntryWidth()])
            self.inputValue4.grid(column= 0, row= 10)
            register_input('DriverSchedule', self.inputValue4)

            self.inputLabel5 = Label(self.window, text= listName[4], bg= styleConfig[styleWindows.getBackGroundColorFont()])
            self.inputLabel5.config(bg = colorWindowStandart)
            self.inputLabel5.config(fg = fgColor)
            self.inputLabel5['font'] = styleConfig[styleWindows.getFontText()], styleConfig[styleWindows.getFontSize()], styleConfig[styleWindows.getFontBold()]
            self.inputLabel5.grid(column= 0, row= 11)
            register_winget('DriverSchedule', self.inputLabel5)

            self.inputValue5 = Entry(self.window, bd= styleConfig[styleWindows.getBorder()], bg= styleConfig[styleWindows.getBackGroundColorWidget()],  width= styleConfig[styleWindows.getEntryWidth()])
            self.inputValue5.grid(column= 0, row= 12)
            register_input('DriverSchedule', self.inputValue5)

            self.button1 = Button(self.window, text='Inserir Dados', bd= styleConfig[styleWindows.getBorder()], width= styleConfig[styleWindows.getButtonsWidth()], command= insert)
            self.button1.grid(column= 0, row= 13, pady= styleConfig[styleWindows.getPadY()])
            self.button1['bg'] = styleConfig[styleWindows.getBackGroundColorWidget()]
            self.button1['font'] = styleConfig[styleWindows.getFontText()], styleConfig[styleWindows.getFontSize()], styleConfig[styleWindows.getFontBold()]

            self.button2 = Button(self.window, text='Gerar Planilha', bd= styleConfig[styleWindows.getBorder()], width= styleConfig[styleWindows.getButtonsWidth()], command= creatSheet)
            self.button2.grid(column= 0, row= 14, pady= styleConfig[styleWindows.getPadY()])
            self.button2['bg'] = styleConfig[styleWindows.getBackGroundColorWidget()]
            self.button2['font'] = styleConfig[styleWindows.getFontText()], styleConfig[styleWindows.getFontSize()], styleConfig[styleWindows.getFontBold()]

            self.end_word = Label(self.window, text='', bg= styleConfig[styleWindows.getBackGroundColorFont()])
            self.end_word.config(bg = colorWindowStandart)
            self.end_word.config(fg = fgColor)
            self.end_word['font'] = styleConfig[styleWindows.getFontText()], styleConfig[styleWindows.getFontSize()], styleConfig[styleWindows.getFontBold()]
            self.end_word.grid(column= 0, row= 15, pady= styleConfig[styleWindows.getPadY()])
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
