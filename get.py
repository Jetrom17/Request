import requests
req = requests.get("http://ip-api.com/json/")
print(req)
print(req.json())
