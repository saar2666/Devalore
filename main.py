#prod
import requests
import json

def exchangeProd():
    url = 'http://api.exchangeratesapi.io/v1/latest?access_key=36d4d7b23910dc84442f4bc147637fab'
    response = requests.get(url).json()
    dic = response["rates"]
    d = dict((k, v) for k, v in dic.items() if v <= 10)

    return(d)

print(exchangeProd())



#dev

#def exchangeDev():
