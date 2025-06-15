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

    __configJson = 'config.json'
    __white = 'colorWhite'
    __black = 'colorBlack'
    __colorDefault = 'colorDefault'
    __fg_default = 'fg_default'

    def getWhite(self):
        return self.__white
    
    def getBlack(self):
        return self.__black
    
    def getConfigJson(self):
        return self.__configJson
    
    def getColorDefault(self):
        return self.__colorDefault
    
    def getFgDefault(self):
        return self.__fg_default
    
    #-------------------------------------------------------------------

    def updateColorWindow(self, color):
        self.__styleConfig[self.getColorDefault()] = self.__styleConfig[color]

    def updateFgWinget(self, color):
        if color == self.getWhite():
            self.__styleConfig[self.getFgDefault()] = self.__styleConfig[self.getBlack()]
        elif color == self.getBlack():
            self.__styleConfig[self.getFgDefault()] = self.__styleConfig[self.getWhite()]

    __styleConfig = {
        __colorDefault: f"{core.getJsonRegistered(__colorDefault, __configJson)}",
        __fg_default: f"{core.getJsonRegistered(__fg_default, __configJson)}",
        __white: f"{core.getJsonRegistered(__white, __configJson)}",
        __black: f"{core.getJsonRegistered(__black, __configJson)}",
    }

    def getColorWindowStandart(self):
        colorWindowStandart = self.__styleConfig[self.getColorDefault()]
        return colorWindowStandart
    
    def getFgWingetStandart(self):
        fgWingetStandart = self.__styleConfig[self.getFgDefault()]
        return fgWingetStandart
    
    def getStyleConfig(self):
        return self.__styleConfig
    
    def modeColor(self, color):
        core = AppCore()
        registered_windows = core.getRegisteredWindow()
        colorWindow = self.getStyleConfig()
        colorWindowStandart = []

        for mode in colorWindow.keys():
            if mode and color == self.getWhite():  
                colorWindowStandart.append(colorWindow[self.getWhite()])
                core.jsonRegistered(self.__styleConfig, self.getConfigJson())
            
            elif mode and color == self.getBlack():
                colorWindowStandart.append(colorWindow[self.getBlack()])
                core.jsonRegistered(self.__styleConfig, self.getConfigJson())
            
        for key in registered_windows:
            for window in registered_windows[key]:
                window.configure(bg = colorWindowStandart[0])
    
    def modeWinget(self, color):
        core = AppCore()
        registered_winget = core.getRegisteredWinget()
        colorWindow = self.getStyleConfig()
        self.updateFgWinget(color)
        colorWindowStandart = []
        colorFgWingetStandart = []

        for mode in colorWindow.keys():
            if mode and color == self.getWhite(): 
                colorWindowStandart.append(colorWindow[self.getWhite()])
                colorFgWingetStandart.append(colorWindow[self.getBlack()])
                core.jsonRegistered(self.__styleConfig,self.getConfigJson())
            
            if mode and color == self.getBlack():
                colorWindowStandart.append(colorWindow[self.getBlack()])
                colorFgWingetStandart.append(colorWindow[self.getWhite()])
                core.jsonRegistered(self.__styleConfig, self.getConfigJson())
                        
            for key in registered_winget:
                for winget in registered_winget[key]:
                    winget.config(fg = colorFgWingetStandart[0])
                    winget.configure(bg = colorWindowStandart[0])
                
    def update_window_colors(self, color):
        
        self.updateColorWindow(color)
        self.modeColor(color)
        self.modeWinget(color)

    def checkColorWhite(self):
        self.update_window_colors(self.getWhite())
        #self.getColorWindowStandart('White')

    def checkColorDark(self):
        self.update_window_colors(self.getBlack())
        #self.getColorWindowStandart('Dark')
