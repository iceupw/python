# 导入MySQL驱动:
import mysql.connector
import sys  
import xlwt 
import datetime  

sheet_name = 'building'  
out_path = 'one.xls'
# 注意把password设为你的root口令:
conn = mysql.connector.connect(user='',
    password='',
    host='',
    database='')
cursor = conn.cursor()
cursor.execute('select * from users where id =1')
# cursor.scroll(0,mode='absolute')  
results = cursor.fetchall()  
fields = cursor.description  
# print(values)
# 关闭Cursor和Connection:

conn.close()

workbook = xlwt.Workbook()  
sheet = workbook.add_sheet(sheet_name,cell_overwrite_ok=True)  

for field in range(0,len(fields)):  
    sheet.write(0,field,fields[field][0])  

row = 1  
col = 0  
for row in range(1,len(results)+1):  
    for col in range(0,len(fields)):  
        sheet.write(row,col,u'%s'%results[row-1][col])  

workbook.save(out_path)

