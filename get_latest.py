import json
import requests
import sys
from operator import itemgetter

headers = {'Content-Type': 'application/json'}

api_url = "https://api.github.com/repos/graalvm/graalvm-ce-dev-builds/releases"

response = requests.get(api_url, headers=headers)

GRAAL_VERSION = sys.argv[1]

if response.status_code == 200:
  releases = response.json()
  releases = sorted(releases, key = lambda i: i['tag_name'].replace("-", "").replace("_", ""), reverse=True) 
  releases = filter(lambda i: GRAAL_VERSION in i['tag_name'], releases)
  print releases[0]['tag_name'].replace(GRAAL_VERSION + "-", "")
else:
  print response

