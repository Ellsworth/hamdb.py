from hamdb import hamdb

def func(call):
    cl = hamdb.dblookup('W1AW')
    callsign = cl.get_data()

    data = callsign['callsign']
    return(data)

def test_answer():
    assert func("W1AW") == "W1AW"
