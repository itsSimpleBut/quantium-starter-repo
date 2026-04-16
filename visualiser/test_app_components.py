import app

def test_header(dash_duo):
    dash_duo.start_server(app.app)
    dash_duo.wait_for_element("#header", timeout=5)
    assert dash_duo.find_element("#header").text == "Pink Morsel Sales"

def test_visualiser(dash_duo):

    dash_duo.start_server(app.app)
    dash_duo.wait_for_element("#visualiser", timeout=5)
    assert dash_duo.find_element("#visualiser").get_attribute("figure") is not None

def test_region_picker(dash_duo):

    dash_duo.start_server(app.app)
    dash_duo.wait_for_element("#regionInput", timeout=5)
    assert dash_duo.find_element("#regionInput").get_attribute("options") is not None