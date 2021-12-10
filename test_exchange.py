import main
import pytest
import requests
import json


@pytest.mark.prod
def testProd():
    currency_names = [] #create empty list
    response = requests.get('http://api.exchangeratesapi.io/v1/latest?access_key=36d4d7b23910dc84442f4bc147637fab').json() #save the api response into variable
    dic = response["rates"] #create dictionary with the rates value from the api
    for k, v in dic.items(): #run on api and search for bigger then 10 element
        if v > 10:
            currency_names.append(k) #append all the rates that are bigger then 10
    list = main.prodExchenage() #create a list with the real live data from prod function
    assert currency_names not in list #if currency_names not in the >10 list (which will return true) pass the test , else , fail the test

@pytest.mark.dev
def testDev():
    currency_names = []
    parsed = json.load(open("moc_data.json", "r")) # same like before , just with our mock_data file we generated
    for k, v in parsed.items():
        if v > 10:
            currency_names.append(k)
    list = main.prodExchenage()
    assert currency_names not in list

