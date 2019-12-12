import requests
import io
import tarfile
import json

url = "https://www.virustotal.com/vtapi/v2/url/feed"

querystring = {"apikey":"<APIKEY>",
               "package":"<PACKAGE>"}

response = requests.request("GET", url, params=querystring)

with io.BytesIO(response.content) as f:
  with tarfile.open(fileobj=f, mode="r:bz2") as t:
    url_infos = [[json.loads(line) for line in t.extractfile(compressed_file)] for compressed_file in t]
