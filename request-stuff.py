import requests
import json
url = 'https://www.reddit.com/r/earthporn/hot.json?limit=1'
headers = {"User-Agent" : "jimmyboi"}
r = requests.get(url, headers = headers)
x = r.text
print(x)
#data = json.loads(r.text)
target = '"stickied": false, "url": "'
print(x.find(target))
#this returns the index where I first find the target!! Use this!
