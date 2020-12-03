class Graph():
    def __init__(self, graphChannel):
        self.graphId = 3213122
        self.graphChannel = graphChannel
    
    def takeScreenshot(self):
        return None

class Channel(Graph):
    def __init__(self):
        self.horScale = 21
        self.verScale = 32
        self.gridScale = 2
        self.xMarker = 1
        self.yMarker = 2
        self.backColor = "White"
        self.gridColor = "Gray"
        self.xMarkerColor = "Red"
        self.yMarkerColor = "Green"
        self.traceColor = "Black"
    
    def setHorScale(self, scale):
        return None
    
    def setVerScale(self, scale):
        return None

    def setGridScale(self, scale):
        return None

    def addXMarker(self):
        return None

    def addYMarker(self):
        return None

    def setBackColor(self, color):
        return None

    def setGridColor(self, color):
        return None

    def setTraceColor(self, color):
        return None