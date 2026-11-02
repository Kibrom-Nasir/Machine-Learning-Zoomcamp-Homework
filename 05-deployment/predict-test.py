import requests


url = ' http://127.0.0.1:9696/predict'



customer = {
    "customerid":"8879-zkjof",
    "gender": "female",
    "seniorcitizen": 0,
    "partner": "no",
    "dependents": "no",
    "tenure": 1,
    "phoneservice": "yes",
    "multiplelines": "no",
    "internetservice": "dsl",
    "onlinesecurity": "yes",
    "onlinebackup": "no",
    "deviceprotection": "yes",
    "techsupport": "yes",
    "streamingtv": "yes",
    "streamingmovies": "yes",
    "contract": "one_year",
    "paperlessbilling": "yes",
    "paymentmethod": "bank_transfer_(automatic)",
    "monthlycharges": 29.85,
    "totalcharges": 4100.75
}


customer_id = '8879-zkjof'



response = requests.post(url, json=customer).json()
response


if response['churn'] == True:
    print('sending promo email to %s' %(customer_id))
else:
    print('Not sending promo email to %s' %(customer_id))





