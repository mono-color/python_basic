import csv
import cx_Oracle

conn = cx_Oracle.connect('usedcar'
                         , 'oracle'
                         , 'localhost:1521/XE'
                         , encoding='utf-8')
curs = conn.cursor()
printHeader = True  # include column headers in each table output
sql = "SELECT * FROM sell_history"
curs.execute(sql)
for row_data in curs:
    print(row_data)
    f_name = "sell_history.csv"
    outputFile = open(f_name, 'w')  # 'wb'
    output = csv.writer(outputFile, dialect='excel')
    sql2 = "select * from sell_history"
    curs2 = conn.cursor()
    curs2.execute(sql2)
    if printHeader:  # add column headers if requested
        cols = []
        for col in curs2.description:
            cols.append(col[0])
        output.writerow(cols)
    for row_dat in curs2:  # add table rows
        output.writerow(row_dat)
    outputFile.close()
