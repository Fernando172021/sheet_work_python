from tkinter import *
from style import *

class singIn:
    def __init__(self):
        
        self.window = Tk()
        self.window.title('Cadastro')
        self.window.iconbitmap(iconImage)
        self.window.resizable(False, False)
        self.window.configure(bg = colorWindowStandart)
        register_window(self.window)



        self.window.mainloop()
