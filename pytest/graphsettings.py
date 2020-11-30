class Graph():
    def __init__(self, graphChannel):
        self.graphId = 3213122
        self.graphChannel = graphChannel

class Settings(Graph):
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

