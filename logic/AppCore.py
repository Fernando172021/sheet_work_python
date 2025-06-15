import orjson

class AppCore:
    __DriverSchedule = 'DriverSchedule'
    __SingIn = 'SingIn' 
    __Main = 'Main'

    def getDriverSchedule(self):
        return self.__DriverSchedule
    
    def getSingIn(self):
        return self.__SingIn
    
    def getMain(self):
        return self.__Main

    __registered_input = {
        __DriverSchedule: [],
        __SingIn:         []
    }
    __registered_windows  = {
        __DriverSchedule: [],
        __SingIn:         [],
        __Main:           []
    }
    __registered_winget = {
        __DriverSchedule: [],
        __SingIn:         [],
        __Main:           []
    }

    def getRegisteredInput(self):
        return self.__registered_input
    
    def getRegisteredWindow(self):
        return self.__registered_windows
    
    def getRegisteredWinget(self):
        return self.__registered_winget
    
    def setRegisteredInput(self, id, input):
        self.__registered_input[id].append(input)

    def setRegisteredWindow(self, id, window):
        self.__registered_windows[id].append(window)

    def setRegisteredWinget(self, id, winget):
        self.__registered_winget[id].append(winget)
    
    def unsubscribeInput(self, id):
        for key in self.__registered_input[id]:
            key = None
            self.__registered_input[id].clear()

    def unsubscribeWindow(self, id):
        for key in self.__registered_windows[id]:
            key = None
            self.__registered_windows[id].clear()
    
    def unsubscribeWinget(self, id):
        for key in self.__registered_winget[id]:
            key = None
            self.__registered_winget[id].clear()

    def jsonRegistered(self, dictInput, jsonFile):
        with open(jsonFile, "wb") as file:
            jsonDump = orjson.dumps(dictInput)
            file.write(jsonDump)

    def getJsonRegistered(self, key, jsonFile):
        try:
            with open(jsonFile, "rb") as file:
                data = orjson.loads(file.read())
                return data[f"{key}"]
            
        except KeyError:
            print(f"Key '{key}' not found in JSON file.")
            return None
        
        except FileNotFoundError:
            print("JSON file not found.")
            return None
        
        except Exception as e:
            print(f"An error occurred: {e}")
            return None
