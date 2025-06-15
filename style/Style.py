from logic.AppCore import AppCore

class StyleWindows:
    core = AppCore()

    __iconImage = 'midia/favicon.ico'
    __configStyleJson = 'json\\configStyle.json'
    __white = 'colorWhite'
    __black = 'colorBlack'
    __colorDefault = 'colorDefault'
    __fg_default = 'fg_default'
    __border = "border"
    __buttonsWidth = "buttonsWidth"
    __entryWidth = "entryWidth"
    __padY = "padY"
    __padX = "padX" 
    __buttonsHeight = "buttonsHeight"
    __buttonPadx    = "buttonPadx"
    __buttonPady    = "buttonPady"
    __backgroundcolorWidget = "backgroundcolorWidget"
    __backgroundcolorFont   = "backgroundcolorFont"
    __fontColorConsole = "fontColorConsole" 
    __fontText = "fontText"
    __fontSize = "fontSize"
    __fontBold = "fontBold"
    __fontTextConsole = "fontTextConsole"
    __fontSizeConsole = "fontSizeConsole"
    __fontBoldConsole = "fontBoldConsole"

    def getIconImage(self):
        return self.__iconImage

    def getBackGroundColorWidget(self):
        return self.__backgroundcolorWidget
    
    def getBackGroundColorFont(self):
        return self.__backgroundcolorFont
    
    def getFontColorConsole(self):
        return self.__fontColorConsole
    
    def getFontText(self):
        return self.__fontText
    
    def getButtonsHeight(self):
        return self.__buttonsHeight
    
    def getButtonWidth(self):
        return self.__buttonsWidth
    
    def getButtonPadX(self):
        return self.__buttonPadx
    
    def getButtonPadY(self):
        return self.__buttonPady 
    
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
    
    def getWhite(self):
        return self.__white
    
    def getBlack(self):
        return self.__black
    
    def getConfigJson(self):
        return self.__configStyleJson
    
    def getColorDefault(self):
        return self.__colorDefault
    
    def getFgDefault(self):
        return self.__fg_default
    
    def getFontSize(self):
        return self.__fontSize
    
    def getFontBold(self):
        return self.__fontBold
    
    def getFontTextConsole(self):
        return self.__fontTextConsole
    
    def getFontSizeConsole(self):
        return self.__fontSizeConsole
    
    def getFontBoldConsole(self):
        return self.__fontBoldConsole
    
    #-------------------------------------------------------------------

    def updateColorWindow(self, color):
        self.__styleConfig[self.getColorDefault()] = self.__styleConfig[color]

    def updateFgWinget(self, color):
        if color == self.getWhite():
            self.__styleConfig[self.getFgDefault()] = self.__styleConfig[self.getBlack()]
        elif color == self.getBlack():
            self.__styleConfig[self.getFgDefault()] = self.__styleConfig[self.getWhite()]

    __styleConfig = {
        __colorDefault:          f"{core.getJsonRegistered(__colorDefault, __configStyleJson)}",
        __fg_default:            f"{core.getJsonRegistered(__fg_default, __configStyleJson)}",
        __white:                 f"{core.getJsonRegistered(__white, __configStyleJson)}",
        __black:                 f"{core.getJsonRegistered(__black, __configStyleJson)}",
        __border:                f"{core.getJsonRegistered(__border, __configStyleJson)}",
        __buttonsWidth:          f"{core.getJsonRegistered(__buttonsWidth, __configStyleJson)}",
        __buttonsHeight:         f"{core.getJsonRegistered(__buttonsHeight, __configStyleJson)}",
        __buttonPadx:            f"{core.getJsonRegistered(__buttonPadx, __configStyleJson)}",
        __buttonPady:            f"{core.getJsonRegistered(__buttonPady, __configStyleJson)}",
        __entryWidth:            f"{core.getJsonRegistered(__entryWidth, __configStyleJson)}",
        __padY:                  f"{core.getJsonRegistered(__padY, __configStyleJson)}",
        __padX:                  f"{core.getJsonRegistered(__padX, __configStyleJson)}",
        __backgroundcolorWidget: f"{core.getJsonRegistered(__backgroundcolorWidget, __configStyleJson)}",
        __backgroundcolorFont:   f"{core.getJsonRegistered(__backgroundcolorFont, __configStyleJson)}",
        __fontColorConsole:      f"{core.getJsonRegistered(__fontColorConsole, __configStyleJson)}",
        __fontText:              f"{core.getJsonRegistered(__fontText, __configStyleJson)}",
        __fontSize:              f"{core.getJsonRegistered(__fontSize, __configStyleJson)}",
        __fontBold:              f"{core.getJsonRegistered(__fontBold, __configStyleJson)}",
        __fontTextConsole:       f"{core.getJsonRegistered(__fontTextConsole, __configStyleJson)}",
        __fontSizeConsole:       f"{core.getJsonRegistered(__fontSizeConsole, __configStyleJson)}",
        __fontBoldConsole:       f"{core.getJsonRegistered(__fontBoldConsole, __configStyleJson)}",
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
