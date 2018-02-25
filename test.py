from hamdb import hamdb

cl = hamdb.dblookup('W1AW')
callsign = cl.get_data()

print(callsign)
