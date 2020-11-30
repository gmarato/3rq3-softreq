class DataCapture():
    def __init__(self):
        self.dataSessionId = 372183617
        self.dataData = []
        self.dataFilter = []
        self.dataGraph = []
        self.dataDevice = "NXT Roam"
    
    def dataCapture(self):
        """Method for capturing data and filling in dataData and dataGraph
        """
        return None
    
    def applyFilter(self, filterType, filterOrder):
        """Method for applying filter onto data
        """
        return None

class DataRecall(DataCapture):
    def __init__(self):
        self.dataLength = 60
        self.dataDate = 372178361

    def getLength(self):
        return None
