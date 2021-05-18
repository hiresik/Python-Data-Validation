    
import pandas as pd
import csv
import numpy as np
from datetime import datetime
import time
import re

r='C:\Docs\Lab 4\Data\stemp_for_date.csv'
w='C:\Docs\Lab 4\Data\stemp_for_date_out.csv'



txt='''\
Jan 19, 1990
January 19, 1990
Jan 19,1990
01/19/1990
01/19/90
1990
Jan 1990
January1990'''

import datetime as dt

fmts = ('%Y','%b %d, %Y','%b %d, %Y','%B %d, %Y','%B %d %Y','%m/%d/%Y','%m/%d/%y','%b %Y','%B%Y','%b %d,%Y')

parsed=[]
for e in txt.splitlines():
    for fmt in fmts:
        try:
           t = dt.datetime.strptime(e, fmt)
           parsed.append((e, fmt, t)) 
           break
        except ValueError as err:
           pass

# check that all the cases are handled        
success={t[0] for t in parsed}
for e in txt.splitlines():
    if e not in success:
        print e    

for t in parsed:
    print '"{:20}" => "{:20}" => {}'.format(*t) 

    


with open(r, 'r') as source:
    with open(w, 'w') as result:
        writer = csv.writer(result, lineterminator='\n')
        reader = csv.reader(source)
        # headers = reader.fieldnames()
        # writer.writerow(["PAX_ID","FLIGHT_NUMBER","OPERATION_DATE_GMT","REC_LOCATOR","ORIGIN","DESTINATION","CABIN_CLASS"])
        source.readline()
        for row in reader:
            # print row
            # ts0 = """+row[1]+"""
            ts = row[2]
            # ts1 = row[5]
            # # ts2 = row[7]
            # # ts3 = row[8]
            # # ts4 = row[9]

            print ts
            # ts = datetime.strptime(ts, '%H%M').strftime("%H:%M")
            # ts1 = datetime.strptime(ts1, '%H%M').strftime("%H:%M")

            # print ts
            
            # ts2 = datetime.strptime(ts2, '%d-%b-%y').strftime("%Y-%m-%d")
            # ts3 = datetime.strptime(ts3, '%d-%b-%y').strftime("%Y-%m-%d")
            # ts4 = datetime.strptime(ts4, '%d-%b-%y').strftime("%Y-%m-%d")
            # ts5=str(ts4)
            # ts6 = ts5.replace("1975", "2075")
            # ts7 = datetime.strptime(ts6, "%Y-%m-%d").strftime("%Y-%m-%d")
                        
                
            # if ts != "" or ts1!= "":
            # #  # or ts1 != "" or ts2 !="" or ts3 !="" or ts4 !="" :
            # #     # row[1]=ts0
            # row[2] = ts 
            # row[5] = ts1
            # #     # row[7] = ts2 
                # row[8] = ts3
                # row[9] = ts7  
            # if (ts!='2018-03-02'):
            writer.writerow(row)


source.close()
result.close()

count = 0
with open(r, 'rb') as count_file:
    csv_reader = csv.reader(count_file)
    for row in csv_reader:
        count += 1

print "Source Count ", count

aftermerge = 0
with open(w, 'rb') as count_file:
    csv_reader = csv.reader(count_file)
    for row in csv_reader:
        aftermerge += 1

print "Output count ",aftermerge