from Instances import AppCore

class StyleWindows:
    __iconImage = 'midia/favicon.ico'

    def getIconImage(self):
        return self.__iconImage
    
    #-------------------------------------------------------------------

    __buttonsHeight = 5
    __buttonsWidth  = 30
    __buttonPadx    = 30
    __buttonPady    = 15

    def getButtonHeight(self):
        return self.__buttonsHeight
    
    def getButtonWidth(self):
        return self.__buttonsWidth
    
    def getButtonPadX(self):
        return self.__buttonPadx
    
    def getButtonPadY(self):
        return self.__buttonPady 
    
    #-------------------------------------------------------------------
    
    __entryWidth = 30

    def getEntryWidth(self):
        return self.__entryWidth
    
    #-------------------------------------------------------------------

    __backgroundcolorWidget = '#f0f8ff'
    __backgroundcolorFont   = '#ffffff'
    __fontColorConsole = '#000000'
    __fontFamilyConsole = ('Consolas', '12', 'bold')  
    __fontText = ('Arial', '10', 'bold')

    def getBackGroundColorWidget(self):
        return self.__backgroundcolorWidget
    
    def getBackGroundColorFont(self):
        return self.__backgroundcolorFont
    
    def getFontColorConsole(self):
        return self.__fontColorConsole
    
    def getFontFamilyConsole(self):
        return self.__fontFamilyConsole
    
    def getFontText(self):
        return self.__fontText
    
    #-------------------------------------------------------------------

    __border = 3
    __buttonsWidth = 18
    __entryWidth = 25
    __padY = 10
    __padX = 5  

    def getBorder(self):
        return self.__border
    
    def getButtonsWidth(self):
        return self.__buttonsWidth
    
    def getEntryWidth(self):
        return self.__entryWidth
    
    def getPadY(self):
        return self.__padY
    
    def getPadX(self):
        return self.__padX
    
    #-------------------------------------------------------------------

    __color_window = {
        'White': ['#ffffff'],
        'Dark':  ['#000000'],
    }

    def getColorWindow(self):
        return self.__color_window

    def getColorWindowStandart(self):
        colorWindowStandart = self.getColorWindow()['White']
        return colorWindowStandart
    
    #-------------------------------------------------------------------

    def update_window_colors(self, color):
        core = AppCore()
        registered_windows = core.getRegisteredWindow()
        registered_winget = core.getRegisteredWinget()
        colorWindow = self.getColorWindow()
    
        global colorWindowStandart

        for mode in colorWindow.keys():
            if mode and color == 'White':
                colorWindowStandart = colorWindow['White']
            elif mode and color == 'Dark':
                colorWindowStandart = colorWindow['Dark']
        
            for key in registered_windows:
                for window in registered_windows[key]:
                    window.configure(bg = colorWindowStandart)

        for key in registered_winget:
                for winget in registered_windows[key]:
                    winget.configure(bg = colorWindowStandart)
                    if color == 'White': 
                        winget.configure(fg = '#000000')
                    if color == 'Dark':
                        winget.configure(fg = '#ffffff')

    def checkColorWhite(self):
        self.update_window_colors('White')

    def checkColorDark(self):
        self.update_window_colors('Dark')
