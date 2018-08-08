# 导入MySQL驱动:
import mysql.connector
import sys  
import xlwt 
import datetime 
import os

sheet_name = 'building'  
out_path = '导出'+datetime.datetime.now().strftime('%Y-%m-%d')+'.xls'
print(out_path)
is_exists = os.path.exists(out_path)

"""查看文件是否存在"""
if  is_exists:
    print('已存在，删除')
    os.unlink(out_path)

# 链接mysql
conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='root',
    database='test',
    port='3306'
    )

cursor = conn.cursor()

sql = "show tables"

cursor.execute(sql)
# cursor.scroll(0,mode='absolute')  
results = cursor.fetchall()  
fields = cursor.description  
# print(values)
# 关闭Cursor和Connection:

conn.close()

print(results)
# 制定表格
workbook = xlwt.Workbook()  
sheet = workbook.add_sheet(sheet_name,cell_overwrite_ok=True)  

#表头
for field in range(0,len(fields)):  
    sheet.write(0,field,fields[field][0])  
# 内容
row = 1  
col = 0 

for row in range(1,len(results)+1):  
    for col in range(0,len(fields)):  
            sheet.write(row,col,u'%s'%results[row-1][col])

#输出文件 
print(workbook.save(out_path))

