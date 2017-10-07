import json
import requests
import time, os
from datetime import datetime

import sqlite3

API_KEY = '90cc7f7cb74adc7e34bc3328e3a2e93813c4f662'
BASE_URL = 'https://suggestions.dadata.ru/suggestions/api/4_1/rs/suggest/%s'


def suggest(query, resource):
    url = BASE_URL % resource
    headers = {
        'Authorization': 'Token %s' % API_KEY,
        'Content-Type': 'application/json',
    }
    data = {
        'query': query
    }
    r = requests.post(url, data=json.dumps(data), headers=headers)
    l = r.json()

    list_ka = []
    for i in l["suggestions"]:
        ka = {}
        ka['name'] = i["value"]
        try:
            ka['branch_type'] = i["data"]["branch_type"]
        except KeyError:
            ka['branch_type'] = None
        try:
            ka['branch_count'] = i["data"]["branch_count"]
        except KeyError:
            ka['branch_count'] = None
        ka['inn'] = i["data"]["inn"]
        try:
            ka['kpp'] = i["data"]["kpp"]
        except KeyError:
            ka['kpp'] = None
        ka['ogrn'] = i["data"]["ogrn"]
        ka['actuality_date'] = datetime.fromtimestamp(int(i["data"]["state"]["actuality_date"])/1000).strftime('%d.%m.%Y')
        if i["data"]["state"]["registration_date"]:
            ka['registration_date'] = datetime.fromtimestamp(int(i["data"]["state"]["registration_date"])/1000).strftime('%d.%m.%Y')
        else:
            ka['registration_date'] = None
        if i["data"]["state"]["liquidation_date"]:
            ka['liquidation_date'] = datetime.fromtimestamp(int(i["data"]["state"]["liquidation_date"])/1000).strftime('%d.%m.%Y')
        else:
            ka['liquidation_date'] = None
        if i["data"]["opf"]:
            ka['opf'] = i["data"]["opf"]["code"]
        else:
            ka['opf'] = None
        ka['status'] = i["data"]["state"]["status"]
        ka['type'] = i["data"]["type"]
        ka['address'] = i["data"]["address"]["value"]
        if i["data"]["address"]["data"]:
            ka['street_kladr_id'] = i["data"]["address"]["data"]["street_kladr_id"]
        else:
            ka['street_kladr_id'] = None
        list_ka.append(ka)
    return list_ka


if __name__ == '__main__':

    #list_ka = suggest('7714704125', 'party') #121505503564
    conn = sqlite3.connect('./megafon.db')
    c = conn.cursor()
    list_inn = c.execute("select kunnr, stcd1 from kna1 where stcd1 != '' limit 500").fetchall()

    c.execute("DROP TABLE dadata")
    c.execute("CREATE TABLE dadata (kunnr char, name char, branch_type CHAR, branch_count CHAR, inn CHAR, kpp CHAR, ogrn CHAR, actuality_date CHAR, registration_date CHAR, liquidation_date CHAR, opf CHAR, status CHAR, type CHAR, address CHAR, street_kladr_id CHAR)")
    for i in list_inn:
        print(i[1])
        list_ka = suggest(i[1], 'party')
        for l in list_ka:
            c.execute("insert into dadata values ('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')".format(i[0], l['name'], l['branch_type'], l['branch_count'], l['inn'], l['kpp'], l['ogrn'], l['actuality_date'], l['registration_date'], l['liquidation_date'], l['opf'], l['status'], l['type'], l['address'], l['street_kladr_id']))
    conn.commit()

"""
time.strftime(“%a, %d %b %Y %H:%M:%S +0000”, time.gmtime(t/1000.0))
‘Thu, 19 Jul 2007 00:00:00 +0000’
my_time = datetime.fromtimestamp(t/1000.0)
my_time.strftime(‘%Y.%m.%d %H:%M’)
‘2007.07.19 04:00’
"""