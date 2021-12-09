import requests
import json


def prodExchenage():
    currency_names = []
    response = requests.get('http://api.exchangeratesapi.io/v1/latest?access_key=36d4d7b23910dc84442f4bc147637fab').json()
    dic = response["rates"]
    for k,v in dic.items():
        if v<10:
            currency_names.append(k)
    return(currency_names)

#print(prodExchenage())




def devExchange():
    parsed = json.load(open("moc_data.json", "r"))
    currency_names = []
    for k, v in parsed.items():
        if v < 10:
            currency_names.append(k)
    return(currency_names)

#print(devExchange())
