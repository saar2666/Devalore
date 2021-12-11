import main
import pytest
import requests
import json


@pytest.mark.prod
def testProd():
    currency_names = []
    response = requests.get('http://api.exchangeratesapi.io/v1/latest?access_key=36d4d7b23910dc84442f4bc147637fab').json()
    dic = response["rates"]
    for k, v in dic.items():
        if v > 10:
            currency_names.append(k)
    list = main.prodExchenage()
    assert currency_names not in list

@pytest.mark.dev
def testDev():
    currency_names = []
    parsed = json.load(open("moc_data.json", "r"))
    for k, v in parsed.items():
        if v > 10:
            currency_names.append(k)
    list = main.prodExchenage()
    assert currency_names not in list
