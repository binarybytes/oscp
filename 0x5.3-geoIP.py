# curl https://api.hackertarget.com/geoip/?q=64.137.135.53

#!/bin/python3

import requests


url = 'https://api.hackertarget.com/geoip/?q=1.1.1.1'
params = {'apikey':'APIKEYZ', 'url':'badguy.xom'}
response = requests.post(url, data=params)

print(response.json())

http://maps.googleapis.com/maps/api/staticmap?center=38.000000,-97.000000&zoom=5&size=400x400&sensor=false&markers=color:blue|38.000000,-97.000000


#resource; MD5, SHA-1 or SHA-256
#scan_id; endpoint
#allinfo; true = metadata(PDFiD, ExifTool, sigcheck, TrID,)
#vtapi/v2- file,network-traffic,domain/report,ip-address/report,
#'ip':'<ip>'
#'query': '<query>'
#'url':'<url>'
