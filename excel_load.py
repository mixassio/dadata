import xlrd
import datetime
import sqlite3

DATE_TODAY = datetime.date.today()
NAME_FILE = 'test2.xls'
rb = xlrd.open_workbook(NAME_FILE,formatting_info=True)
sheet = rb.sheet_by_index(0)
my_list_od = []
for rownum in range(11, sheet.nrows):#read first page with OD
    row = sheet.row_values(rownum)
    my_dict = {
        'id': row[0],
        'name':row[1],
        'group':row[2],
        'inn':row[3],
        'okpo':row[4],
        'kpp':row[5],
        'ogrn':row[6],
        'ofk':row[7],
        'rbs':row[8],
        'upk':row[9],
        'okato':row[10]
    }
    if my_dict['name']:
        my_list_od.append(my_dict)
sheet = rb.sheet_by_index(1)
my_list_br = []
i = 1
for rownum in range(10, sheet.nrows):#read second page with BR
    row = sheet.row_values(rownum)
    if row[1] == '': row[1] = '0001'
    my_dict = {
        'id': row[0],
        'id_num':row[1],
        'bik_ofk': row[2],
        'ls_br': row[3],
        'RU_bik': row[4],
        'ofk_br': row[5],
        'date_dl': DATE_TODAY,
        'name_file': NAME_FILE
    }
    if my_dict['bik_ofk']:
        my_list_br.append(my_dict)


if len(my_list_br) > 0:
    for key,val in enumerate(my_list_od): #Add BR into list with OD
        val.update(my_list_br[key])
else:
    for key,val in enumerate(my_list_od): #Add BR into list with empty od
        val.update({'id_num': ''})
        val.update({'bik_ofk': ''})
        val.update({'ls_br': ''})
        val.update({'RU_bik': ''})
        val.update({'ofk_br': ''})
        val.update({'date_dl': DATE_TODAY})
        val.update({'name_file': NAME_FILE})

#print(my_list_od)
conn = sqlite3.connect('./KA.db')
c = conn.cursor()

#c.execute("DROP TABLE  applications")
#c.execute("CREATE TABLE applications (id CHAR, short_name CHAR, group_KA CHAR, inn CHAR, okpo CHAR, kpp CHAR, ogrn CHAR, ofk CHAR, rbs CHAR, upk CHAR, okato CHAR, id_num CHAR, bik_ofk CHAR, ls_br CHAR, RU_bik CHAR, ofk_br CHAR, date_load CHAR, name_file CHAR)")

for row in my_list_od:
    print(row)
    c.execute("insert into applications values ( ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", list(row.values()))

conn.commit()