from logic.AppCore import AppCore

class ConsoleRedirect:
    core = AppCore()
    windowR = core.getRegisteredWindow()
    key = core.getMain()

    def __init__(self, text_widget):
        self.text_widget = text_widget

    def write(self, message):
        self.text_widget.insert('end', message)   
        self.text_widget.see('end')  

    def flush(self):
        pass
