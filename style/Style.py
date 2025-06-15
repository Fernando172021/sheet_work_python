from logic.AppCore import AppCore

class StyleWindows:
    core = AppCore()

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

    __white = 'White'
    __dark = 'Dark'

    def getStandartWhite(self):
        return self.__white
    
    def getStandartDark(self):
        return self.__dark
    
    __color = {
        __white: ['#ffffff'],
        __dark:  ['#000000'],
    }

    def getColorWindow(self):
        return self.__color
    
    #-------------------------------------------------------------------

    def updateColorWindow(self, color):
        self.__color_window["colorDefault"] = self.__color[color][0]

    def updateFgWinget(self, color):
        if color == 'White':
            self.__color_window["fg_default"] = self.__color["Dark"][0]
        elif color == 'Dark':
            self.__color_window["fg_default"] = self.__color["White"][0]

    __color_window = {
        "colorDefault": f"{core.getJsonRegistered('colorDefault')}",
        "fg_default": f"{core.getJsonRegistered('fg_default')}"
    }

    def getColorWindowStandart(self):
        colorWindowStandart = self.__color_window["colorDefault"]
        return colorWindowStandart
    
    def getFgWingetStandart(self):
        fgWingetStandart = self.__color_window["fg_default"]
        return fgWingetStandart
    
    def modeColor(self, color):
        core = AppCore()
        registered_windows = core.getRegisteredWindow()
        colorWindow = self.getColorWindow()
        colorWindowStandart = []

        for mode in colorWindow.keys():
            if mode and color == 'White':  
                colorWindowStandart.append(colorWindow['White'])
                core.jsonRegistered('colorDefault', self.__color_window)
            
            elif mode and color == 'Dark':
                colorWindowStandart.append(colorWindow['Dark'])
                core.jsonRegistered('colorDefault', self.__color_window)
            
            for key in registered_windows:
                for window in registered_windows[key]:
                    window.configure(bg = colorWindowStandart[0])
    
    def modeWinget(self, color):
        core = AppCore()
        registered_winget = core.getRegisteredWinget()
        colorWindow = self.getColorWindow()
        self.updateFgWinget(color)
        colorWindowStandart = []
        colorFgWingetStandart = []

        for mode in colorWindow.keys():
            if mode and color == 'White': 
                        colorWindowStandart.append(colorWindow['White'])
                        colorFgWingetStandart.append(colorWindow['Dark'])
                        core.jsonRegistered('fg_default', self.__color_window)
            
            if mode and color == 'Dark':
                        colorWindowStandart.append(colorWindow['Dark'])
                        colorFgWingetStandart.append(colorWindow['White'])
                        core.jsonRegistered('fg_default', self.__color_window)
                        
        for key in registered_winget:
                for winget in registered_winget[key]:
                    winget.config(fg = colorFgWingetStandart[0])
                    winget.configure(bg = colorWindowStandart[0])

                
    def update_window_colors(self, color):
        
        self.updateColorWindow(color)
        self.modeColor(color)
        self.modeWinget(color)

    def checkColorWhite(self):
        self.update_window_colors('White')
        
        #self.getColorWindowStandart('White')

    def checkColorDark(self):
        self.update_window_colors('Dark')
        #self.getColorWindowStandart('Dark')
