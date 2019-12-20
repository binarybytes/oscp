# curl https://api.hackertarget.com/geoip/?q=64.137.135.53

#!/bin/python3

import requests


url = 'https://api.hackertarget.com/geoip/?q=1.1.1.1'
params = {'apikey':'APIKEYZ', 'url':'badguy.xom'}
response = requests.post(url, data=params)

print(response.json())

#url of a gcp'Maps Static API' image
#http://maps.googleapis.com/maps/api/staticmap?center=38.000000,-97.000000&zoom=5&size=400x400&sensor=false&markers=color:blue|38.000000,-97.000000&key=API_KEY



