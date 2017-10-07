import os, re
import chardet
import codecs

import sqlite3

if os.path.exists('./KNA1.txt'):
    with open('./KNA1.txt', 'rb') as file_text:
        char_type = chardet.detect(file_text.read())['encoding']
    with codecs.open('./KNA1.txt', 'rb', encoding=char_type) as file_text:
        #print(file_text.read(351))
        list_ka = [line.strip('')  for line in file_text]

my_list = []
my_list2 = []
my_set = set()
for line in list_ka:
    #[number * number for number in numbers]
    my_list2.append(line.split('\t')[:-1])
"""
for line in my_list2:
    print(line)
"""

dict_count = {}
for line in my_list2:
    #list2 = [c for c in line]
    try:
        dict_count[len(line)] += 1
    except KeyError:
        dict_count[len(line)] = 1
    #my_set.add(len(line))
#{0: 3, 52: 260442, 13: 3, 38: 3, 6: 1, 10: 1, 34: 1, 5: 1, 46: 1, 53: 1}
print(dict_count)





for i, line in enumerate(my_list2):
    if len(line) < 45:
        list_dop = [';' for i in range(0,45 - len(line))]
        #print(len(line), line, len(list_dop), list_dop)
        my_list2[i].extend(list_dop)
        #print(len(my_list2[i]), my_list2[i])
    elif len(line) > 45:
        #print(len(line), line)
        for j in range(0, len(line) - 45):
            my_list2[i].pop()
        #print(len(my_list2[i]), my_list2[i])


for line in my_list2:
    for i, st in enumerate(line):
        line[i] = re.sub('""', '"', st)
        line[i] = re.sub('       ', ' ', st)

for line in my_list2:
    for i, st in enumerate(line):
        line[i] = re.sub('""', '"', st)
        line[i] = re.sub('  ', ' ', st)

for line in my_list2:
    for i, st in enumerate(line):
        line[i] = re.sub('""', '"', st)
        line[i] = re.sub('  ', ' ', st)

for line in my_list2:
    for i, st in enumerate(line):
        line[i] = re.sub('""', '"', st)
        line[i] = re.sub('  ', ' ', st)

"""for line in my_list2:
    for i in line:
        if bool(re.findall('  ', i)): print('bs', line)


"""
conn = sqlite3.connect('./megafon.db')
c = conn.cursor()
c.execute("CREATE TABLE kna1 (KUNNR CHAR, LAND1 CHAR, NAME1 CHAR, NAME2 CHAR, ORT01 CHAR, PSTLZ CHAR, REGIO CHAR, SORTL CHAR, STRAS CHAR, TELF1 CHAR, TELFX CHAR, XCPDK CHAR, ADRNR CHAR, MCOD1 CHAR, MCOD2 CHAR, MCOD3 CHAR, BBSNR CHAR, KNRZA CHAR, KTOKD CHAR, LIFNR CHAR, LOCCO CHAR, NAME3 CHAR, NAME4 CHAR, ORT02 CHAR, PSTL2 CHAR, COUNC CHAR, CITYC CHAR, RPMKR CHAR, SPERR CHAR, SPRAS CHAR, STCD1 CHAR, STCD2 CHAR, TELBX CHAR, TELF2 CHAR, TELTX CHAR, TELX1 CHAR, VBUND CHAR, STKZN CHAR, KTOCD CHAR, STCDT CHAR, STCD3 CHAR, STCD4 CHAR, STCD5 CHAR, PSON1 CHAR, PSON2 CHAR)")
for line in my_list2:
    c.execute("insert into kna1 values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", line)
conn.commit()

"""
f = open('text5.txt', 'w')
for index in my_list2:
    f.write(''.join(index) + '\n')
f.close()"""



