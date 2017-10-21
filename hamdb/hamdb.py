import urllib.request
import json

callsign = 'kg5key'

class hamdb:
    def __init__(self, callsign):
        self.callsign = callsign
        self.url = 'http://api.hamdb.org/v1/' + str(callsign) + '/json/hamdbpy'

        req = urllib.request.Request(self.url)
        r = urllib.request.urlopen(req).read()

        self.jsondata = json.loads(r.decode('utf-8'))

    def status_message(self):
        return self.jsondata['hamdb']['messages']['status']
    def

cl = hamdb(callsign)
print(cl.status_message())
