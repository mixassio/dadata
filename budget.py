import requests
import json
import sqlite3

page = 1547
payload = {'pageNum': page}
#url = 'http://www.budget.gov.ru/epbs/registry/ubpandnubp/data'
#url = 'http://budget.gov.ru/epbs/registry/ubpandnubp/data?filterkbk=187'
url = 'http://budget.gov.ru/epbs/registry/rubp/data?blocks=info'
response = requests.get(url, params=payload)
users = response.json()
count_page = users['pageCount']
print(count_page)
print(users)
"""
for page in range(1, count_page - 1):
    payload = {'pageNum': page}
    response = requests.get(url, params=payload)
    users = response.json()
    my_list = []
    for i in users['data']:
        print('-------------------------------------')
        my_list_val = list(i['info'].values())
        my_list_key = list(i['info'].keys())
        print(i['id'])
        print('-------------------------------------')
        my_list.append(my_list_val)
    #my_list.append(my_list_key)
    conn = sqlite3.connect('./KA.db')
    c = conn.cursor()
    for row in my_list:
        print(row)
        c.execute("insert into ubp_neubp values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", row)
    conn.commit()
    print(page)"""