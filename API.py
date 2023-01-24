 

import requests
import json

#link to the endpoint

response = requests.get("https://api.wazirx.com/sapi/v1/tickers/24hr")
# if okay 200
print(response.status_code)
#print the reponse as text
#print(response.text)

res =json.loads(response.text)

for data in res:
    print (data)