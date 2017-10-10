import requests
import json
page = 8500
payload = {'pageNum': page}
url = 'http://www.budget.gov.ru/epbs/registry/ubpandnubp/data'

response = requests.get(url, params=payload)
users = response.json()

print(json.dumps(users, indent=2, ensure_ascii=False))
for i, j in users.items():
    print(i)
for i in users['data']:
    print(json.dumps(i, indent=2, ensure_ascii=False))
    print('-------------------------------------')

print(type(users['data']), len(users['data']))