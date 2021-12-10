import requests
import json


def prodExchenage():
    currency_names = [] #create empty list
    response = requests.get('http://api.exchangeratesapi.io/v1/latest?access_key=36d4d7b23910dc84442f4bc147637fab').json() #save the api response into variable
    dic = response["rates"] #create dictionary with the rates value from the api
    for k, v in dic.items(): ##run on api and search for bigger then 10 element
        if v < 10:
            currency_names.append(k) #append all the rates that are smaller then 10 as requested
    return (currency_names)


print(prodExchenage()) #just for self testing


def devExchange():
    parsed = json.load(open("moc_data.json", "r")) #load the json file with the mock data we created earlier using the function below
    currency_names = []
    for k, v in parsed.items():
        if v < 10:
            currency_names.append(k)
    return (currency_names)

print(devExchange())  #just for self testing




currency_names = []
response = requests.get('http://api.exchangeratesapi.io/v1/latest?access_key=36d4d7b23910dc84442f4bc147637fab').json()
dic = response["rates"]
for k,v in dic.items():
    if v<10:
        currency_names.append(k)
print(currency_names)

json_string = json.dumps(response, indent=3)
with open('moc_data.json', 'w') as outfile: #create json file name mock_data.json , write permissions
    outfile.write(json_string) #using dump to convert object into string

