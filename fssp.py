import xml.etree.ElementTree as etree
import requests
import json

# r = requests.get('http://fssprus.ru/export/payment_receiver.xml')
tree = etree.parse('./payment_receiver.xml')
root = tree.getroot()
my_dict = []
for i in range(0, len(root)):
    my_dict_local = {}
    for j in range(0, len(root[i])):
        #print(root[i][j].tag, root[i][j].text)
        my_dict_local[root[i][j].tag] = root[i][j].text
        #print(my_dict_local)
    my_dict.append(my_dict_local)

#for a in my_dict:
    #print(a)

#print(json.dumps(my_dict, indent=2, ensure_ascii=False))

f = open('./text1.txt', 'w')
f.write(str(my_dict))
f.close()
