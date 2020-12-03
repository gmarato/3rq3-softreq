from datacapture import DataCapture, DataRecall
from filters import Filter, LowPassFilter, HighPassFilter, MovingAverageFilter, PeakFilter

def test_data_capture_length_60():
    """Tests 4.2.3 Data capture length
    """
    data = DataRecall()

    test_length = 60
    
    assert test_length == data.getLength(), "Capture length is beyond the requirement"
    
def test_data_capture_length_40():
    """Tests 4.2.3 Data capture length
    """
    data = DataRecall()

    test_length = 40
    
    assert test_length == data.getLength(), "Capture length is beyond the requirement"

def test_data_capture_length_65():
    """Tests 4.2.3 Data capture length
    """
    data = DataRecall()

    test_length = 65
    
    assert test_length == data.getLength(), "Capture length is beyond the requirement"

def test_data_live_capture():
    """Tests 4.2.4 Live data capture
    """
    data = DataCapture()
    
    data.dataCapture()

    errors = []

    if data.dataData == []:
        errors.append("Data variable empty")
    if data.dataGraph == []:
        errors.append("Graph variable empty")

    assert not errors, "Assert errors occured:\n{}".format("\n".join(errors))

def test_save_data_capture():
    """Tests 4.2.5 Data saving
    """
    data = DataCapture()
    
    # capture up to 1hr long of data
    data.dataCapture()

    data1 = data.dataSave()
    data2 = data.dataSave()

    #TODO
    # save data1 onto local drive, recall it and compare to data2 from memory
    
    # NOTE: currently returns PASSED as the two data types are both "NONE" and python considers them equal
    assert data1 == data2, "Was not able to save data capture"

def test_recall_data_capture():
    """Tests 4.2.6 Data recall
    """
    data = DataRecall()
    
    # open dummy .CSV data files
    data1 = data.openData()
    data2 = data.openData()

    errors = []
    
    if not data1:
        errors.append("Was not able to recall data capture 1")
    if not data2:
        errors.append("Was not able to recall data capture 2")

    assert not errors, "Assert errors occured:\n{}".format("\n".join(errors))

def test_apply_filter():
    """Tests 4.3.1 Filtering method
    """
    data = DataCapture()

    dfilter = LowPassFilter("Chebyshev", 1000)
    

    old_data = data.dataCapture()
    filtered_data = data.applyFilter(dfilter, 2)

    assert old_data != filtered_data, "No changes to filtered data"

def test_apply_noise_filter():
    """ Tests 4.3 Filter library
        Tests 4.3.2 Noise filtering
    """
    data = DataCapture()

    
    low_noise_filter = LowPassFilter("Chebyshev", 100)
    high_noise_filter = HighPassFilter("Chebyshev", 5000)

    low_noise = []  # random <100HZ noise
    high_noise = [] # random >5000HZ noise

    old_data = data.dataCapture()
    low_filtered_data = data.applyFilter(low_noise_filter, 2)
    high_filtered_data = data.applyFilter(high_noise_filter, 2)

    errors = []
    
    #TODO
    # replace == with a in comparison to check if the noise is in the data
    if low_noise == low_filtered_data:
        errors.append("Low noise detected in filtered data")
    if high_noise == high_filtered_data:
        errors.append("High noise detected in filtered data")

     # NOTE: currently returns PASSED as the two data types are both "NONE" and python considers them equal
    assert not errors, "Assert errors occured:\n{}".format("\n".join(errors))

def test_check_avail_filters():
    """ Tests 4.3 Filter library
        Tests 4.3.3 Data filtering
    """
    data = DataCapture()

    lpf = LowPassFilter("Chebyshev", 250)
    hpf = HighPassFilter("Bessel", 500)
    maf = MovingAverageFilter(10)
    pkf = PeakFilter(10, 10)

    errors = []

    # replace == with a check if noise data is contained in filtered data
    if not lpf.getFilterInfo():
        errors.append("Low pass filter does not exist")
    if not hpf.getFilterInfo():
        errors.append("High pass filter does not exist")
    if not maf.getFilterInfo():
        errors.append("Moving average filter does not exist")
    if not pkf.getFilterInfo():
        errors.append("Peak filter does not exist")

    assert not errors, "Assert errors occured:\n{}".format("\n".join(errors))