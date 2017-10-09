import csv
import requests
import json
import re
import sqlite3


API_KEY = '90cc7f7cb74adc7e34bc3328e3a2e93813c4f662'
BASE_URL = 'https://suggestions.dadata.ru/suggestions/api/4_1/rs/suggest/%s'


def suggest_kladr_house(query, resource):
    url = BASE_URL % resource
    headers = {
        'Authorization': 'Token %s' % API_KEY,
        'Content-Type': 'application/json',
    }
    data = {
        'query': query
    }
    r = requests.post(url, data=json.dumps(data), headers=headers)
    print(r.json())
    try:
        kladr = r.json()['suggestions'][0]['data']['kladr_id']
        house = str(r.json()['suggestions'][0]['data']['house'])
        print(kladr)
        #print(type(kladr), type(house))
        return kladr + house
    except IndexError:
        return ''


def get_index(text):
    try:
        return re.findall('\w*(\d\d\d\d\d\d)', text)[0]
    except IndexError:
        return ''

def true_id(a, b):
    if len(a) + len(b) > 4:
        return a + b
    if len(a) == 1:
        sym = '0' * (4 - len(a) - len(b))
    elif len(a) == 2:
        sym = '0' * (5 - len(a) - len(b))
    return a + sym + b


raw_csv = requests.get('http://opendata.fssprus.ru/7709576929-osp/data-20170926-structure-20160226.csv')
#raw_csv.content.decode('utf-8')
raw_csv.encoding = 'utf-8'

with open("test.csv", "wb") as code:
    code.write(raw_csv.content)


with open('test.csv', 'rt') as f:
    reader = csv.reader(f)
    m = map(lambda x: [x[0], true_id(x[0], x[1]), x[2], get_index(x[3]), suggest_kladr_house(x[3], 'address'), x[3], x[5]], list(reader)[1:])
#print(list(m))


conn = sqlite3.connect('./KA.db')
c = conn.cursor()

c.execute("DROP TABLE  fssp_address1")
c.execute("CREATE TABLE fssp_address1 (region CHAR, id CHAR, short_name CHAR, address CHAR, post_index CHAR, kladr_house CHAR, telephone CHAR)")


for row in m:
    print(row)
    c.execute("insert into fssp_address1 values ( ?, ?, ?, ?, ?, ?, ?)", row)

conn.commit()
"""
print(get_index('С. ЧАРЫШСКОЕ, УЛ. ПАРТИЗАНСКАЯ, 53, 658170'))
print(get_index('Россия, Алтайский край, , , с. Усть-Чарышская Пристань, ул. 1 Мая, 13, , '))
print(suggest_kladr_house('453580 С. СТ. СУБХАНГУЛОВО, УЛ. САЛАВАТА, 30', 'address'))
"""
