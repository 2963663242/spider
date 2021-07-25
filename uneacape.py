import urllib.parse
import json
with open("f.json", "r") as fp:
    t = fp.read()
t = json.loads(t)
print(t)