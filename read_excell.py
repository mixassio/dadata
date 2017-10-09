import xlrd
rb = xlrd.open_workbook('./test_excell1.xls',formatting_info=True)
sheet = rb.sheet_by_index(0)
my_list_od = []
for rownum in range(11, sheet.nrows):#read first page with OD
    row = sheet.row_values(rownum)
    my_dict = {
        'id':int(row[0]),
        'name':row[1],
        'group':row[2],
        'inn':row[3],
        'okpo':row[4],
        'kpp':row[5],
        'ogrh':row[6],
        'ofk':row[7],
        'rbs':row[8],
        'upk':row[9],
        'okato':row[10]
    }
    if my_dict['name']:
        my_list_od.append(my_dict)
sheet = rb.sheet_by_index(1)
my_list_br = []
for rownum in range(10, sheet.nrows):#read second page with BR
    row = sheet.row_values(rownum)
    if row[1] == '': row[1] = '0001'
    my_dict = {
        'id':int(row[0]),
        'id_num':row[1],
        'bik_ofk': row[2],
        'ls_br': row[3],
        'RU_bik': row[4],
        'ofk_br': row[5]
    }
    if my_dict['bik_ofk']:
        my_list_br.append(my_dict)

for key,val in enumerate(my_list_od): #Add BR into list with OD
    val.update(my_list_br[key])


for v in my_list_od:
    print(v)
for v in my_list_br:
    print(v)
print(my_list_od)