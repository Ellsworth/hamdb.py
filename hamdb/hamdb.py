import urllib.request
import json

class dblookup:
    def __init__(self, callsign):
        callsign = callsign
        url = 'http://api.hamdb.org/v1/' + str(callsign) + '/json/hamdbpy'

        req = urllib.request.Request(url)
        r = urllib.request.urlopen(req).read()

        jsondata = json.loads(r.decode('utf-8'))

        self.info = jsondata['hamdb']['callsign']
        self.url = url
        self.jsondata = jsondata

# There should be a better way to do this, need to work on it some more.
    def get_data(self):
        return {'url': self.url,
                'api_version': self.jsondata['hamdb']['version'],
                'api_status': self.jsondata['hamdb']['messages']['status'],
                'callsign': self.info['call'],
                'license_class': self.info['class'],
                'expires': self.info['expires'],
                'status': self.info['status'],
                'grid': self.info['grid'],
                'lat': self.info['lat'],
                'lon': self.info['lon'],
                'first_name': self.info['fname'],
                'middle_name': self.info['mi'],
                'last_name': self.info['name'],
                'suffix_name': self.info['suffix'],
                'address': self.info['addr1'],
                'city': self.info['addr2'],
                'state': self.info['state'],
                'zip': self.info['zip'],
                'country': self.info['country']}
