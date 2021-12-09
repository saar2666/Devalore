import main
import pytest
import requests

@pytest.mark.prod
def testProd():
    response = requests.get('http://api.exchangeratesapi.io/v1/latest?access_key=36d4d7b23910dc84442f4bc147637fab').json()
    dic = response["rates"]
    for k, v in dic.items():
        if v > 10:
            currency_names.append(k)
    list = main.exchangeProd()

@pytest.mark.dev
def testDev():
    list =  main.devExchange()

