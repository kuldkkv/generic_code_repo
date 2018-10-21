#!/usr/bin/env python

import mysql.connector
import csv

load_file = '../inp/test_data.csv'
conn = mysql.connector.connect(user='stg', password = 'point007',
				host='35.200.172.25', database='stgdb')

print ('connected to db')

cur = conn.cursor()

sql = '''Insert into stg_inbound (
C1, C2, C3, C4, C5, C6, C7, C8, C9, C10, C11, C12, C13, C14, C15, C16,
C17, C18, C19, C20, C21, C22, C23, C24, C25, C26, C27
)
values (
%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
%s, %s, %s, %s, %s
)
'''
#cur.prepare(sql)
n = 0
with open(load_file) as csvfile:
	csvreader = csv.reader(csvfile)
	for row in csvreader:
		n += 1
		cur.execute(sql, row)
		if n%10000 == 0:
			conn.commit()
			print('loaded ' + str(n) + ' lines.')

print('total ' + str(n) + ' lines loaded.')
conn.commit()
cur.close()
conn.close()

