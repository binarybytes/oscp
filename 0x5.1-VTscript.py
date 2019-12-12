


import requests

url = "https://www.virustotal.com/vtapi/v2/url/scan"

params = {"apikey" : <apikey>, "resource", : <resource>}

response = requests.get(url, params = params)

print(response.json)

#resource; MD5, SHA-1 or SHA-256
#scan_id; endpoint
#allinfo; true = metadata(PDFiD, ExifTool, sigcheck, TrID,)
#vtapi/v2- file,network-traffic,domain/report,ip-address/report,
#'ip':'<ip>'
#'query': '<query>'
#'url':'<url>'
