import requests
import json
url = 'https://www.reddit.com/r/earthporn/hot.json?limit=1'
r = requests.get(url)
data = json.loads(r.text)
target = "sticked"
for target in data:
    print('Found it')
