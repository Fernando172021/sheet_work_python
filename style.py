iconImage = 'midia/favicon.ico'

buttonsHeight = 5
buttonsWidth  = 30
buttonPadx    = 30
buttonPady    = 15

backgroundcolorWidget = '#f0f8ff'
backgroundcolorFont   = '#ffffff'
fontColorConsole = '#00FF00'
fontFamilyConsole = 'Consolas'
fontText = ('Arial', '10', 'bold')
border = 3
buttonsWidth = 18
entryWidth = 25
padY = 10
padX = 5   

color_window = {
    'White': ['#ffffff'],
    'Dark':  ['#000000'],
}

colorWindowStandart = color_window['White']

registered_windows  = []

registered_winget = []

def register_window(window):
    registered_windows.append(window)

def register_winget(winget):
    registered_winget.append(winget)

def update_window_colors(color):
    global colorWindowStandart

    for mode in color_window.keys():
        if mode and color == 'White':
            colorWindowStandart = color_window['White']
        elif mode and color == 'Dark':
            colorWindowStandart = color_window['Dark']
        
        for window in registered_windows:
            window.configure(bg = colorWindowStandart)

    for winget in registered_winget:
                winget.configure(bg = colorWindowStandart)
                if color == 'White':
                    winget.configure(fg = '#000000')
                if color == 'Dark':
                    winget.configure(fg = '#ffffff')

def checkColorWhite():
    update_window_colors('White')

def checkColorDark():
    update_window_colors('Dark')
