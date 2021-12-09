import secrets
import requests
import json

parsed = json.load(open("secrets.json", "r"))
currency_names = []
response = requests.get('http://api.exchangeratesapi.io/v1/latest?access_key='+parsed["API_KEY"]).json()
dic = response["rates"]
for k,v in dic.items():
    if v<10:
        currency_names.append(k)
print(currency_names)