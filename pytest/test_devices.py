from devices import Device

def test_connection_type():
    """Tests 4.2.1 Device connection methods
       Tests 5.1.1 Connection type 
    """
    dev = Device()

    set_conn_type = "Wired"
    dev.setConnection(set_conn_type)
    get_conn_type = dev.getConnection() 
    
    assert get_conn_type == set_conn_type, "Wired device connection was not set"

def test_device_info():
    """Tests 5.1.2 Retrieving device information
    """
    dev = Device()
    dev_info = dev.getInfo()

    assert dev_info == ["Roam NXT", 12345, 2.11, 1.2, 423434343, 100], "Incorrect device information"

def test_set_time():
    """Tests 5.1.4 Data synchronization
    """
    dev = Device()

    set_time = 342342343
    dev.setTime(set_time)
    get_time = dev.getTime()

    assert get_time == set_time, "Time was not set correctly"
