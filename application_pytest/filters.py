class Filter():
    def __init__(self):
        self.filterType = "Some Filter"
        self.filterOrder = 1

    def getFilterInfo(self):
        """Method for returning the information of the filter
        """
        return None  

class LowPassFilter(Filter):
    def __init__(self, lpfSubType, lpfCutoff):
        self.filterType = "Low Pass Filter"
        self.lpfSubType = lpfSubType
        self.lpfCutoff = lpfCutoff

class HighPassFilter(LowPassFilter):
    def __init__(self, hpfSubType, lpfCutoff):
        self.filterType = "High Pass Filter"

class MovingAverageFilter(Filter):
    def __init__(self, mafWeight):
        self.filterType = "Moving Average Filter"
        self.mafWeight = mafWeight

class PeakFilter(Filter):
    def __init__(self, pkfPeakAmp, pkfBWfreq):
        self.filterType = "Peak Filter"
        self.pkfPeakAmp = pkfPeakAmp
        self.pkfBWfreq = pkfBWfreq
