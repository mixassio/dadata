import os, re
import chardet
import codecs

import sqlite3

if os.path.exists('./LFA1.txt'):
    with open('./LFA1.txt', 'rb') as file_text:
        char_type = chardet.detect(file_text.read())['encoding']
    with codecs.open('./LFA1.txt', 'rb', encoding=char_type) as file_text:
        #print(file_text.read(351))
        list_ka = [line.strip('')  for line in file_text]

my_list = []
my_list2 = []
my_set = set()
for line in list_ka:
    #[number * number for number in numbers]
    my_list.append(line.split('\t')[1:-1])
for line in my_list:
    list2 = [c for c in line]
    #my_set.add(len(list2))
    my_list2.append(list2)

#print(my_list2[8606])
#print(len(my_list2[8606]))


for i, line in enumerate(my_list2):
    if len(line) < 16:
        list_dop = [';' for i in range(0,16 - len(line))]
        #print(len(line), line, len(list_dop), list_dop)
        my_list2[i].extend(list_dop)
        #print(len(my_list2[i]), my_list2[i])
    elif len(line) > 16:
        #print(len(line), line)
        for j in range(0, len(line) - 16):
            my_list2[i].pop()
        #print(len(my_list2[i]), my_list2[i])

#print(len(my_list2[350]), my_list2[350])
#print(len(my_list2[351]), my_list2[351])
#rint(len(my_list2[352]), my_list2[352])

for line in my_list2:
    for i, st in enumerate(line):
        line[i] = re.sub('""', '"', st)

for line in my_list2:
    for i, st in enumerate(line):
        line[i] = re.sub('""', '"', st)

for line in my_list2:
    for i, st in enumerate(line):
        line[i] = re.sub('""', '"', st)

for line in my_list2:
    for i, st in enumerate(line):
        line[i] = re.sub('""', '"', st)

for line in my_list2:
    for i in line:
        if bool(re.findall('""', i)): print(line)

for line in my_list2:
    if line[0] == '15.03.2010':
        print(line)

"""conn = sqlite3.connect('/Users/mixassio/Documents/megafon.db')
c = conn.cursor()
c.execute("CREATE TABLE debitors3 (num INTEGER, name1 CHAR, name2 CHAR, name3 CHAR, name4 CHAR, date_create DATE, creater CHAR, groups CHAR, field1 CHAR, field2 CHAR, field3 CHAR, inn CHAR, field4 CHAR, kpp CHAR, field5 CHAR, field6 CHAR)")
for line in my_list2:
  c.execute('insert into debitors3 values (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)', line)
conn.commit()


f = open('text5.txt', 'w')
for index in my_list2:
    f.write(''.join(index) + '\n')
f.close()"""



