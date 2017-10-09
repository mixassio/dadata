import re
import requests
import datetime
import lxml.etree as etree
import sqlite3

DATE_TODAY = datetime.date.today()
# get data FSSP
raw_xml = requests.get('http://fssprus.ru/export/payment_receiver.xml').content
parser_xml = etree.XMLParser(remove_blank_text=True)
root_xml = etree.fromstring(raw_xml, parser_xml)
#get list from FSSP
my_list1 = []
my_list2 = []
for index, course in enumerate(root_xml):
    for line in course:
        my_list1.append(line.text)
    my_list1.append(DATE_TODAY)
    my_list2.append(my_list1)
    my_list1 = []

conn = sqlite3.connect('./KA.db')
c = conn.cursor()
#get replace and make my_name
list_reduce = c.execute('select * from Reduce').fetchall()
for id, line in enumerate(my_list2):
    line.insert(3,line[2])
    for red in list_reduce:
        f = re.sub(red[0], red[1], line[3])
        g = re.sub(r'(?<!\d\.\s)УФССП.*', '', f)
        if g != '':
            line[3] = g
        else:
            line[3] = f
#get my_full_name
for id, line in enumerate(my_list2):
    list_UFK = c.execute('select * from regUFK where regions={}'.format(line[0])).fetchall()
    my_full_name = '{}({} {}, л/с {})'.format(list_UFK[0][2], line[3], list_UFK[0][1], line[12])
    line[4] = my_full_name
"""
for line in my_list2:
    print(line)

print(len(my_list2))
"""
c.execute("DROP TABLE  fssp")
c.execute("CREATE TABLE fssp (region CHAR, id CHAR, short_name CHAR, my_name CHAR, full_name CHAR, RKC CHAR, RS CHAR, BIK CHAR, INN CHAR, KPP CHAR, OKATO CHAR, OKTMO CHAR, LS CHAR, date_download)")
for line in my_list2:
    c.execute("insert into fssp values ( ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", line)
conn.commit()