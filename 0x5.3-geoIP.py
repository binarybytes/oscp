#!/bin/python3


#curl https://api.hackertarget.com/geoip/?q=1.1.1.1


#pip install geoip2

import geoip2.webservice
#replcae 42 with account id+license key with legit l-key)
client = geoip2.webserver.Client(62, 'license key')
#replcae insights with method e.g, 'country', 'city'
response = client.insights('1.2.3.4')
response.country.iso_code
response.country.name
response.country.names['zh-CN']
response.subdivisions.most_specific.name
response.subdivisions.most_specific.iso_code
response.city.name
response.postal.code
response.location.latitude
response.location.longitude



#OR


import requests




url = 'http://api.ipstack.com/'
params = {'access_key' : 'key...', 'ip' : '8.8.8.8'} 
r = requests.post(url, data=params)
print(r)
