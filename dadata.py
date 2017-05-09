import json
import requests
import time


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
    print(json.dumps(l, indent=2, ensure_ascii=False))
    End_list = []
    for a,b in enumerate(l['suggestions']):
        my_dict = {}
        for key,val in b.items():
            if isinstance(val, dict):
                for k1,v1 in val.items():
                    if isinstance(v1, dict):
                        for k2, v2 in v1.items():
                            print('------------------')
                            k3 = k1 + '-' + k2
                            my_dict[k3] = v2
                    else:
                        my_dict[k1] = v1
            else:
                my_dict[key] = val
        End_list.append(my_dict)
    return End_list


if __name__ == '__main__':

    l = suggest('5262308874', 'party')
    print(json.dumps(l, indent=2, ensure_ascii=False))
    tek = time.localtime(1415232000)
    print('{}.{}.{}'.format(tek.tm_mday, tek.tm_mon, tek.tm_year))



