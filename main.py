import requests
import json


def proExchenage():
    currency_names = []
    response = requests.get('http://api.exchangeratesapi.io/v1/latest?access_key=36d4d7b23910dc84442f4bc147637fab').json()
    dic = response["rates"]
    for k,v in dic.items():
        if v<10:
            currency_names.append(k)
    return(currency_names)


print(proExchenage())

currency_names = []
response = requests.get('http://api.exchangeratesapi.io/v1/latest?access_key=36d4d7b23910dc84442f4bc147637fab').json()
dic = response["rates"]
for k,v in dic.items():
    if v<10:
        currency_names.append(k)
print(currency_names)

with open('moc_data.json', 'w') as outfile:
    json.dump(response["rates"], outfile)