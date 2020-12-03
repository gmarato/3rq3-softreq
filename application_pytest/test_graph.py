from graph import Graph, Channel

def test_take_screenshot_graph():
    """Tests 4.4.2 Graph screenshot
    """
    graph = Channel()

    image1 = graph.takeScreenshot()
    image2 = graph.takeScreenshot()

    #TODO
    # save image1 onto local drive, recall it and compare to image2 from memory
    # using OpenCV or other library

    # NOTE: currently returns PASSED as the two data types are both "NONE" and python considers them equal
    assert image1 == image2, "Was not able to take acreenshot"


def test_horizontal_scale():
    """Tests 4.4 Graph settings
    """
    graph = Channel()

    # takes screenshot before setting applied and after for comparison
    # compare the two images if any change has happened
    image1 = graph.takeScreenshot()
    graph.setHorScale(5)
    image2 = graph.takeScreenshot()

    #TODO
    #upload the screenshots to website for a person to compare and approve

    assert image1 != image2, "Horizontal scale did not apply"

def test_vertical_scale():
    """Tests 4.4 Graph settings
    """
    graph = Channel()

    # takes screenshot before setting applied and after for comparison
    # compare the two images if any change has happened
    image1 = graph.takeScreenshot()
    graph.setVerScale(5)
    image2 = graph.takeScreenshot()

    #TODO
    #upload the screenshots to website for a person to compare and approve

    assert image1 != image2, "Vertical scale did not apply"

def test_grid_scale():
    """Tests 4.4 Graph settings
    """
    graph = Channel()

    # takes screenshot before setting applied and after for comparison
    # compare the two images if any change has happened
    image1 = graph.takeScreenshot()
    graph.setGridScale(2)
    image2 = graph.takeScreenshot()

    #TODO
    #upload the screenshots to website for a person to compare and approve

    assert image1 != image2, "Grid scale did not apply"
