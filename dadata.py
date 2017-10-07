import json
import requests
import time, os


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
    End_list = []
    for a,b in enumerate(l['suggestions']):
        my_dict = {}
        for key,val in b.items():
            if isinstance(val, dict):
                for k1,v1 in val.items():
                    if isinstance(v1, dict):
                        for k2, v2 in v1.items():
                            k3 = k1 + '-' + k2
                            my_dict[k3] = v2
                    else:
                        my_dict[k1] = v1
            else:
                my_dict[key] = val
        End_list.append(my_dict)
    #print(json.dumps(End_list, indent=2, ensure_ascii=False))
    return l


# Функция по загрузке списка значений из файла в список
def load_list_into_file(filepath):
    if os.path.exists(filepath):
        with open(filepath, 'r') as file_text:
            list_ka = [line.strip('') for line in file_text]
    my_dict = {}
    my_list = []
    for KA in list_ka:
        a = KA[0:-1].split(';')
        my_dict['id_sap'] = a[0]
        my_dict['name_sap'] = a[1]
        my_dict['date_sap'] = a[2]
        my_dict['creater_sap'] = a[3]
        my_dict['group_sap'] = a[4]
        my_dict['inn_sap'] = a[5]
        my_dict['kpp_sap'] = a[6]
        my_list.append(my_dict.copy())
    return my_list


def data_mining(KA):
    for i in KA:
        l = suggest(i['inn_sap'], 'party')
        i['ogrn'] = l[0]['ogrn']
        i['postal_code'] = l[0]['value']
        i['new_name'] = 'helllo'
        print(i['inn_sap'], l[0]['ogrn'])
    print(json.dumps(KA, indent=2, ensure_ascii=False))


if __name__ == '__main__':

    l = suggest('Алтайский край Барнаул, "пр.Красноармейский, 61А"', 'address') #121505503564
    #f = load_list_into_file('./test_60.csv')
    #data_mining(f)
    print(json.dumps(l, indent=2, ensure_ascii=False))
    tek = time.localtime(1488326400)
    print('{}.{}.{}'.format(tek.tm_mday, tek.tm_mon, tek.tm_year))




