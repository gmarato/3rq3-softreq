class Device:
    def __init__(self):
        self.devId = 123872183
        self.devMfg = "Laborie"
        self.devSN = 123123
        self.devHWver = 2.11
        self.devFWver = 1.2
        self.devTime = 12312312
        self.devBatStatus = 100
        self.connectionType = "Wireless"
    
    def setTime(self, time):
        self.devTime = time
    
    def getTime(self):
        return None
    
    def getInfo(self):
        return None
    
    def setConnection(self, connType):
        self.connectionType = connType

    def getConnection(self):
        return None
